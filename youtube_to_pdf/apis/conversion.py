import logging

from flask_restplus import Namespace, fields, Resource, abort

from youtube_to_pdf.classes.video import ManagedApp
from youtube_to_pdf.models.video import Video
from youtube_to_pdf.parsers import conversion as conversion_parsers

api = Namespace("conversion", description="Conversion operations")

api_app = api.model(
    "App", {
        "youtube_url": fields.String(
            required=True,
            description="Youtube video URL",
            example="https://www.youtube.com/watch?v=<id>"
        ),
        "description": fields.String(
            required=False,
            description="Youtube video description"
        ),
        "md5sum": fields.String(
            required=False,
            description="File md5sum"
        ),
        "video_path": fields.String(
            required=False,
            description="Video path on system"
        ),
        "report_path": fields.String(
            required=False,
            description="Report path on system"
        ),
        "pdf_path": fields.String(
            required=False,
            description="PDF path on system"
        )
    }
)


def get_video_info(video: Video):
    return {
        "youtube_url": video.url,
        "description": video.description,
        "md5sum": video.md5sum,
        "video_path": video.video_path,
        "report_path": video.report_path,
        "pdf_path": video.pdf_path,
    }

# Write Endpoints
@api.route("/upload")
class Upload(Resource):
    @api.expect(conversion_parsers.get_parser_adder())
    @api.marshal_with(api_app, code=201, description="Successfully uploaded")
    @api.response(404, "URL not found")
    @api.response(422, "Unprocessable file")
    @api.response(503, "Service Unavailable")
    @api.response(504, "Gateway timeout")
    def post(self):
        parser = conversion_parsers.get_parser_adder()
        args = parser.parse_args()

        if args.url is not None:
            logging.debug("Youtube URL received! Starting ManagedApp...")
        else:
            abort(code=400, error="ERROR-400-1", status=None,
                  message="Direct download url must be provided")

        # create Video dataclass
        video = Video(url=args.url)

        # init and run ManagedApp
        managed_app = ManagedApp(video)
        video = managed_app.run()

        return get_video_info(video), 201


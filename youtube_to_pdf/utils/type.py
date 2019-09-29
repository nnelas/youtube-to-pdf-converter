import hashlib
import re

import requests


def url(value):
    try:
        if re.match(r"http(?:s)?://", value) is None:
            value = "http://" + value

        response = requests.head(value, timeout=2)
        if response.status_code != 405:  # do not reject 405 as a GET may work
            response.raise_for_status()  # raise exception if no success
        return value
    except requests.exceptions.ConnectionError:
        raise ValueError("Provided value is not an URL or connection error")
    except requests.RequestException:
        raise ValueError("Could not perform a successful request "
                         "with the provided URL")


def get_file_md5sum(path):
    hash_md5 = hashlib.md5()
    with open(path, "rb") as f:
        block_size = 128 * hash_md5.block_size
        for chunk in iter(lambda: f.read(block_size), b''):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

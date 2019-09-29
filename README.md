# youtube-to-pdf-converter
Converts Youtube videos to PDF

## Why

Basically, this started because my girlfriend was complaining that she had a teacher 
who converted class slides into a video and they were only available on Youtube. 

Since there's no actual tool to retrieve those slides (printscreens are not an option haha), 
with the help of some frameworks (eg.: pytube), youtube-to-pdf-converter does the following:
- Download video from URL
- Stores frames every second
- Compare pixels difference between two frames
- Joins all slides to a single pdf
- Generate some reports with comparison analysis

## Requirements

- Install Python (although that's probably installed already on your system)

- Install pipenv: https://pipenv.readthedocs.io/en/latest/install/#installing-pipenv 
(you may need to add $HOME/.local/bin to $PATH and reboot for pipenv to be recognized as a system command)

- Install all Python library dependencies on the project's root directory:
```
$ pipenv install
```

Note: all project paths are defined inside `settings` package

## How to Use

- Run the following command on your machine:
```
$ pipenv run python converter.py
```

- Open your browser go to `localhost:5050`

- Insert URL and wait. When finished, you'll have all files paths on API response

## Contributions
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. 

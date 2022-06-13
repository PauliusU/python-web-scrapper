# python-web-scrapper

[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/PauliusU/balance_checker/blob/master/LICENSE)

Practical Project 1 (PP1) for Artificial Intelligence studies to
solidify Python basics by practicing.

<!-- TOC -->
* [python-web-scrapper](#python-web-scrapper)
  * [Usage](#usage)
      * [Automatic launch](#automatic-launch)
      * [Manual launch](#manual-launch)
  * [Requirements](#requirements)
  * [Optional requirements (to be done later)](#optional-requirements--to-be-done-later-)
<!-- TOC -->

## Usage

#### Automatic launch
For Windows installation just **run automatic setup script** in Git Bash:
```bash
bash <(curl -s https://raw.githubusercontent.com/PauliusU/python-web-scrapper/master/setup.sh)
```

#### Manual launch

1. Clone this repo:
```bash
git clone https://github.com/PauliusU/python-web-scrapper.git
```

2. Navigate into project:
```bash
cd python-web-scrapper/
```

3. Ensure pipenv is installed:
```bash
pip install --upgrade pipenv --user
```

4. Install dependencies:
```bash
pipenv install
```

5. Activate virtual environment:
```bash
pipenv shell
```

6. Navigate `/bin` folder:
```bash
cd bin/
```

7. Download [ChromeDriver](https://sites.google.com/chromium.org/driver/) (WebDriver for Chrome)
```bash
curl https://chromedriver.storage.googleapis.com/102.0.5005.61/chromedriver_win32.zip -L -o driver.zip
```

8. Unzip ChromeDriver
```bash
unzip driver.zip
```

9. Navigate back to project root folder:
```bash
cd ..
```

10. Run project:
```bash
python ./src/python-web-scrapper/main.py
```

## Requirements

- [ ] Scrape one or more websites, that are publicly available - it can be a minimal project, or
you can go as in depth as you like.
- [ ] It must scrape at least 2 kinds pages with navigation either in depth or breadth (e.g.:
items page + item page) - this is the minimal requirement to get a positive grade.
- [X] You can use any library / framework, but if you use bs4, selenium, requests-html please use
recommended python project structure.
- [X] It must contain a config file - you decide what parameters need to be configurable, simple
options: url, selectors, port, logging level, etc.
- [X] It must log errors to a centralized file - at least one log file, for example main.log.
- [X] Code is hosted in GitHub (can be private, but please invite the teacher as a collaborator to
verify the project) with at least 3 commits, containing readme file with launch instructions
(document how to launch the project easily), requirements.txt (or equivalent).

## Optional requirements (to be done later)

- [ ] Write some unit tests (pytest)
- [ ] Incorporate excel file processing
- [ ] Save values to a database
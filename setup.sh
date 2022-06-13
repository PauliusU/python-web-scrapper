git clone https://github.com/PauliusU/python-web-scrapper.git
cd python-web-scrapper/
pip install --upgrade pipenv --user
pipenv install
pipenv shell
cd drivers/
curl https://chromedriver.storage.googleapis.com/102.0.5005.61/chromedriver_win32.zip -L -o driver.zip
unzip driver.zip
cd ..
python ./src/python-web-scrapper/main.py

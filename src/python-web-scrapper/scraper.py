import logging
import os
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def scrape_site(config) -> None:
    """ Scrapes website using provided settings """
    try:
        logging.info(f"Loading driver path from config")
        project_root = Path(__file__).parent.parent.parent
        driver_path = os.path.join(project_root, 'drivers',
                                   config["scraping"]["driver_path"])

        logging.info(f"Setting up webdriver")
        service = ChromeService(driver_path)
        options = webdriver.ChromeOptions()

        with webdriver.Chrome(service=service, options=options) as driver:
            logging.info(f'Getting {config["scraping"]["url"]}')
            driver.get(config["scraping"]["url"])

            logging.info(f"Loading selectors from from config")
            selector_title = config["scraping"]["selector_title"]
            selector_announcement = config["scraping"]["selector_announcement"]

            logging.info(f"Waiting for the page to load")
            logging.info(driver.title)
            delay = 20
            WebDriverWait(driver, delay).until(
                expected_conditions.text_to_be_present_in_element(
                    (By.CSS_SELECTOR, selector_title),
                    config["scraping"]["page_title_text"]
                )
            )

            announcements = driver.find_elements(By.CSS_SELECTOR,
                                                 selector_announcement)
            owner_phones = {}

            for announcement in announcements:
                print(announcement)

            for phone in owner_phones:
                print(f"phone : {phone}")
    except Exception as err:
        logging.error(f'Scrapping error {err}')

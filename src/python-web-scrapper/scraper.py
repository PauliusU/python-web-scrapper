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
        logging.info(f'Loading scraping configuration (URL, selectors, etc.)')
        base_url = config['scraping']['base_url']
        pages_to_scrape = config['scraping']['pages_to_scrape']
        page_title_text = config['scraping']['page_title_text']
        page_title_selector = config['scraping']['page_title_selector']
        selector_title = config['scraping']['selector_title']
        selector_price = config['scraping']['selector_price']

        project_root = Path(__file__).parent.parent.parent
        driver_path = os.path.join(project_root, 'drivers',
                                   config['scraping']['driver_path'])

        cars = {}

        logging.info('Setting up webdriver')
        service = ChromeService(driver_path)
        options = webdriver.ChromeOptions()

        with webdriver.Chrome(service=service, options=options) as driver:
            for page_index in range(0, pages_to_scrape):
                url = f'{base_url}{page_index + 1}'
                logging.info(f'Getting {url}')
                driver.get(url)

                logging.info(f'Waiting for the page to load')
                logging.info(driver.title)

                delay = 20
                WebDriverWait(driver, delay).until(
                    expected_conditions.text_to_be_present_in_element(
                        (By.CSS_SELECTOR, page_title_selector),
                        page_title_text
                    )
                )

                elements_with_titles = driver.find_elements(By.CSS_SELECTOR,
                                                            selector_title)
                elements_with_prices = driver.find_elements(By.CSS_SELECTOR,
                                                            selector_price)

                for i in range(0, len(elements_with_titles)):
                    unique_key = f'[{page_index + 1}:{i + 1}] {elements_with_titles[i].text}'
                    cars[unique_key] = \
                        elements_with_prices[i].text

        for car_title in cars:
            print(f'{car_title}: {cars[car_title]}')
        logging.info(f'Number of cars: {len(cars)}')
    except Exception as err:
        logging.error(f'Scrapping error {err}')

import os

import pytest

from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
os.environ['GH_TOKEN'] = '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'


@pytest.fixture()
def create_chrome_browser():
    driver_chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver_chrome.maximize_window()
    yield driver_chrome
    driver_chrome.quit()


@pytest.fixture()
def create_firefox_browser():
    driver_firefox = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver_firefox.maximize_window()
    yield driver_firefox
    driver_firefox.quit()


@pytest.fixture()
def create_edge_browser():
    driver_edge = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
    driver_edge.maximize_window()
    yield driver_edge
    driver_edge.quit()
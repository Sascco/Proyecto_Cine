from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


class BrowserManager:
    def __init__(self):
        self.driver = None

    def get_driver(self):
        options = Options()
        options.add_argument("--headless=new")  # modo headless moderno
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )
        self.driver.maximize_window()
        return self.driver

    def quit_driver(self):
        if self.driver:
            self.driver.quit()
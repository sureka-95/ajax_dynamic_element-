# import By module to locate the elements
# import webdriverwait  used to wait for an element to meet certain condition
#  Expected condition as EC i.e condition used with waits
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# define a class for population page with 2 usage load, count
class PopulationPage:
    # assign the webpage address as URL
    URL = "https://www.theworldcounts.com/challenges/planet-earth/state-of-the-planet/world-population-clock-live"

# define constructor to initialize the driver
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


# define method to load page by self and browser get the webpage
    def load_page(self):
        self.driver.get(self.URL)

#define population count mehtod
    def get_population_count(self):
        #defines the xpath to locate the population ticker
        xpath = "//div[@class='counter-ticker is-size-2-mobile']"
        # element to wait until xpath is located
        element = self.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
       #get the text and replace with integer and returns it
        #strip string method used to remove white space from string
        text = element.text.replace(",", "").strip()
        return int(text)

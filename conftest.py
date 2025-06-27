import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def driver():
    # create chrome browser configuration options
    options = webdriver.ChromeOptions()
    # chrome to open in full screen mode
    options.add_argument("--start-maximized")
    # launches browser with given options
    driver = webdriver.Chrome(options=options)

# pauses the fixture and gives the driver to your test
    yield driver

# check if driver is still alive before trying to quit it
    if driver:  # Check if driver is still valid
        try:
            driver.quit()  # Clean up properly
        except Exception as e:
            print(f"⚠️ Error during driver quit: {e}")

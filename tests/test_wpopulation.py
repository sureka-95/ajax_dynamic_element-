import time
import pytest
import signal
from pages.population_page import PopulationPage

stop_test = False

# Signal handler to catch Ctrl+C
def signal_handler(sig, frame):
    global stop_test
    stop_test = True
    print("\n Test stopping by user (Ctrl+C).")


signal.signal(signal.SIGINT, signal_handler)


# Pytest fixture for page setup
@pytest.fixture
def population_page(driver):
    page = PopulationPage(driver)
    page.load_page()
    return page


# test function uses fixtures uses population_page object
def test_population_live_count(population_page):
    print(" population live count. Press Ctrl+C to stop...\n")

    try:
        # fetch current population value from the page
          population = population_page.get_population_count()
          print(f" Population: {population}")
          captured = True

# wait 1 second for 10 times
          for i in range(10):
              time.sleep(1)
              print(f"Population . {population}")
            # keyboard interrupt
    except KeyboardInterrupt:
                print("\n Interrupted")

 # finally got the test finisshedd
    finally:
        print("\n Test finished.")
        assert captured, "No population data captured."

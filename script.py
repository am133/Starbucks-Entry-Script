import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_autoinstaller
from dotenv import load_dotenv
import time

# Load environment variables from .env file
load_dotenv()

# User credentials and form details
USERNAME = os.getenv("STARBUCKS_USERNAME")
PASSWORD = os.getenv("STARBUCKS_PASSWORD")
FIRST_NAME = os.getenv("STARBUCKS_FIRST_NAME")
LAST_NAME = os.getenv("STARBUCKS_LAST_NAME")
EMAIL = os.getenv("STARBUCKS_EMAIL")

def setup_driver():
    print("Setting up driver...")
    options = Options()
    brave_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
    options.binary_location = brave_path

    options.add_argument('--start-maximized')
    chromedriver_autoinstaller.install()
    return webdriver.Chrome(options=options)

def wait_and_find_element(driver, by, value, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((by, value))
    )

def wait_and_find_elements(driver, by, value, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_all_elements_located((by, value))
    )

def login(driver):
    try:
        print("Navigating to landing page...")
        driver.get("https://www.starbucksforlife.ca/landing")
        time.sleep(5)

        print("Looking for sign-in link...")
        sign_in_link = wait_and_find_element(
            driver,
            By.XPATH,
            "//a[span[text()='Sign in and play']]"
        )
        print("Found the link by text content")
        sign_in_link.click()

        time.sleep(3)
        print("Waiting for login form...")

        print("Entering username...")
        username_field = wait_and_find_element(driver, By.ID, 'username')
        username_field.send_keys(USERNAME)

        print("Entering password...")
        password_field = wait_and_find_element(driver, By.ID, 'password')
        password_field.send_keys(PASSWORD)

        print("Clicking sign in...")
        sign_in_btn = wait_and_find_element(
            driver,
            By.XPATH,
            "//button[@type='submit']"
        )
        sign_in_btn.click()

        print("Waiting for redirect...")
        WebDriverWait(driver, 20).until(
            lambda d: d.current_url == "https://www.starbucksforlife.ca/dashboard"
        )
        print(f"Redirect successful: Current URL: {driver.current_url}")

        print("Dashboard detected. Waiting for 10 seconds before next logic...")
        time.sleep(10)

        return True

    except Exception as e:
        print(f"Login error: {str(e)}")
        print(f"Current URL after error: {driver.current_url if driver else 'No driver available'}")
        driver.save_screenshot("login_error.png")
        raise

def fill_form(driver):
    try:
        print("Navigating to the form page...")
        driver.get("https://www.starbucksforlife.ca/oamoe")

        print("Waiting for the loading screen to disappear...")
        WebDriverWait(driver, 20).until_not(
            EC.presence_of_element_located((By.CLASS_NAME, "loading-screen"))
        )
        print("Loading screen disappeared. Proceeding with form interaction.")

        print("Selecting game type...")
        game_select = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "game"))
        )
        select = Select(game_select)
        select.select_by_value("transaction")

        form_fields = {
            'first_name': FIRST_NAME,
            'last_name': LAST_NAME,
            'email': EMAIL
        }

        for field_id, value in form_fields.items():
            element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, field_id))
            )
            element.clear()
            element.send_keys(value)

        survey_questions = ['oamoe-q1-a1', 'oamoe-q2-a1', 'oamoe-q3-a1']
        for question_id in survey_questions:
            question = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, question_id))
            )
            question.click()

        print("Submitting the form...")
        submit_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))
        )
        submit_button.click()

        print("Form submitted successfully.")
        time.sleep(5)

    except Exception as e:
        print(f"Form fill error: {str(e)}")
        driver.save_screenshot("form_error.png")
        raise

def main():
    driver = None
    try:
        driver = setup_driver()

        if login(driver):
            print("Waiting before navigating to form page...")
            time.sleep(10)
            fill_form(driver)

        print("Script completed successfully")
    except Exception as e:
        print(f"Script failed: {str(e)}")
        if driver:
            driver.save_screenshot("error_screenshot.png")
    finally:
        if driver:
            driver.quit()

if __name__ == "__main__":
    main()

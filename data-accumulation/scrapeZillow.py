import fnmatch

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

import json
from time import sleep

import undetected_chromedriver as uc
from fake_useragent import UserAgent

options = webdriver.ChromeOptions()

options.add_argument(f"user-agent={UserAgent.random}")
options.add_argument("--window-size=1920x1080")
options.add_argument("--verbose")
#options.add_argument("--headless")

driver = uc.Chrome(options=options)

def get_by_id(driver, element_id):
    return WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.ID, element_id))
    )

def get_child_elements(parent_element):
    return parent_element.find_elements(By.XPATH, './*')  # Returns immediate children

def click_button(button):
    button.click()

def get_ids_from_webpage(url):
    driver.get(url)
    
    try:
        # Wait until the body is loaded or any specific element
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, 'body'))
        )
        
        # Find all elements with IDs
        elements_with_ids = driver.find_elements(By.XPATH, '//*[@id]')  # All elements that have an 'id' attribute

        # Extract IDs
        ids = [el.get_attribute('id') for el in elements_with_ids]
        
        return ids

    except Exception as e:
        print(f"An error occurred: {e}")
        return []


def enter_text(input_field, text):
    # Use ActionChains to click and enter the prompt
    actions = ActionChains(driver)
    actions.click(input_field).send_keys(text).perform()

def get_elements_by_id_pattern(driver, id_pattern):
    # Wait for all elements to be present
    elements = WebDriverWait(driver, 3).until(
        EC.presence_of_all_elements_located((By.XPATH, "//*"))
    )

    #print(elements)

    # Filter elements based on the fnmatch pattern
    matched_elements = [el for el in elements if fnmatch.fnmatch(el.get_attribute('id'), id_pattern)]

    print(matched_elements)
    return matched_elements

def getZillowPriceEstimate(address):

    # Add headless mode to run without opening the browser window
    # Note to self: comment out if you want to see the browser window
    #options.add_argument("--headless")

    # 1 percent of home worth per month for rent
    
    data = {}

    try:
        url = "https://zillow.com"
        driver.get(url)
        
        # Inputting address
        print("Entering address")
        address_entry = get_elements_by_id_pattern(driver, '__c11n_*6')
        
        if address_entry:
            enter_text(address_entry[0], address)
            print("Entered address")
        else:
            print("Address entry not found")
            return data

        # Wait for button(s) to be available
        print("Waiting for buttons")
        sleep(2)  # Adjust as needed; replace with a proper wait if possible

        # Refetch the button elements
        button_elements = get_elements_by_id_pattern(driver, '__c11n_*6')
        if button_elements:
            children = get_child_elements(button_elements[0])
            if len(children) >= 2:
                print("Clicking buttons")
                click_button(children[0])  # Assume this is the correct button
                click_button(children[1])  # Assume this is the correct button
            else:
                print("Not enough child elements found")
                return data
        else:
            print("Button elements not found")
            return data

        # Wait for the response to load
        sleep(3)  # Replace with proper wait for loading if needed

    except Exception as e:
        print(f"Issue getting Zillow data: {e}")

    return data
    


if __name__ == "__main__":
    address = "8905 19th pl SE, Lake Stevens, WA"
    response = getZillowPriceEstimate(address=address)
    print(response)
    


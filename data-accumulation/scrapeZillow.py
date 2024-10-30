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
options.add_argument("--headless")

driver = uc.Chrome(options=options)

def get_by_id(driver, element_id):
    return WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, element_id))
    )

def get_child_elements(parent_element):
    return parent_element.find_elements(By.XPATH, './*')  # Returns immediate children

def click_button(button_id):
    button = get_by_id(driver, button_id)
    button.click()

def enter_text(input_id, text):
    input_field = get_by_id(input_id)
    input_field.clear()  # Clear existing text if necessary
    input_field.send_keys(text)

def getFreeChatResponse(instructions, example, input):

    # Add headless mode to run without opening the browser window
    # Note to self: comment out if you want to see the browser window
    #options.add_argument("--headless")

    try:
        
        # Getting chatGPT website
        driver.get("https://zillow.com")
        
        # Getting 
        addressEntry = get_by_id(driver, "__c11n_d5w6")
        enter_text(addressEntry)

        sleep(3)

    except:
        print("issue getting zillow data")

    return extract_json(response)
    


if __name__ == "__main__":
    instructions = "get from description whether a building is a residential apartment, house, hotel, or neither (denoted by APT, HOU, HOT, NA respectively), how many dwellings, how many bedrooms in each dwelling, and whether its labelled as low income. If any info unavailable from description, label null"
    example = "{type:'APT', lowIncome: false, dwellings:12, bedrooms:null}"
    input = "townhouse in new ampsterdam for low income family with 3 bedrooms"

    response = getFreeChatResponse(instructions=instructions, example=example, input=input)
    print(response)
    


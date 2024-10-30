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


# Add headless mode to run without opening the browser window
# Note to self: comment out if you want to see the browser window
options.add_argument("--headless")

# Starting up the web driver used to control chrome
driver = uc.Chrome(options=options)


def find_response_content(driver, response_text):
    try:
        # Wait for both <p> and <code> elements to be present
        elements = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//p | //code'))
        )
        
        # Search for elements containing the specific text
        response_contents = []
        for element in elements:
            if response_text in element.text:
                response_contents.append(element.text)
        
        return response_contents

    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def click_send_button(driver):
    try:
        # Wait for the button to become clickable
        send_button = WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="send-button"]'))
        )
        send_button.click()
        print("Button clicked successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

def enter_prompt(driver, prompt_text):
    try:
        # Wait for the editable div to be present
        editable_div = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.ID, 'prompt-textarea'))
        )
        
        # Clear any existing text (optional)
        editable_div.clear()
        
        # Use ActionChains to click and enter the prompt
        actions = ActionChains(driver)
        actions.click(editable_div).send_keys(prompt_text).perform()
        print("Prompt entered successfully.")
        
    except Exception as e:
        print(f"An error occurred: {e}")

def getFreeChatResponse(instructions, example, input):

    extracted = {}
    
    try:

        # Getting chatGPT website
        driver.get("https://chatgpt.com")

        # Enter the prompt text
        prompt_text = f"Write in JSON format only (no additional text or explanation) : {instructions} : format like RESPONSE_(number of outputs returned by you, starting with 1) . Example being (for second of your outputs) RESPONSE_2 => {example}. REMEMBER THE ARROW WITH =>. If any not in the description, say null for that part like: lowincome:null. ENCLOSE IN DOUBLE QUOTES THE JSON ELEMENTS. Do so single line and in code window. Here is the question : '{input}' "

        enter_prompt(driver=driver, prompt_text=prompt_text)

        # Click the send button
        click_send_button(driver=driver)

        sleep(3)

        # Get the response GPT response
        response = find_response_content(driver=driver, response_text="RESPONSE_1")
        print(response)

        # Close the driver after use
        sleep(2)

        def extract_json(data_list):
            # Assuming the input is a list with one string
            if data_list:
                # Split the string to isolate the JSON part
                json_str = data_list[0]
                print(json_str)
                split = json_str.split(' => ', 1)
                print(split)
                json_str = split[1]
                print(json_str)
                # Parse the JSON string into a dictionary
                return json.loads(json_str)
            return None
        
        extracted = extract_json(response)
        
    except:
        print("Error parsing response from GPT, trying again")

    return extracted
    


if __name__ == "__main__":
    instructions = "get from description whether a building is a residential apartment, house, hotel, or neither (denoted by APT, HOU, HOT, NA respectively), how many dwellings, how many bedrooms in each dwelling, and whether its labelled as low income. If any info unavailable from description, label null"
    example = "{type:'APT', lowIncome: false, dwellings:12, bedrooms:null}"
    input = "townhouse in new ampsterdam for low income family with 3 bedrooms"

    response = getFreeChatResponse(instructions=instructions, example=example, input=input)
    print(response)

    instructions = "get from description whether a building is a residential apartment, house, hotel, or neither (denoted by APT, HOU, HOT, NA respectively), how many dwellings, how many bedrooms in each dwelling, and whether its labelled as low income. If any info unavailable from description, label null"
    example = "{type:'APT', lowIncome: false, dwellings:12, bedrooms:null}"
    input = "townhouse in new ampsterdam for low income family with 3 bedrooms"

    response = getFreeChatResponse(instructions=instructions, example=example, input=input)
    print(response)
    


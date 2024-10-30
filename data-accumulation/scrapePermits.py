from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.by import By



options = Options()
options.add_argument("--window-size=1920x1080")
options.add_argument("--verbose")

import json

def write_to_json(file_name, **kwargs):
    try:
        # Write the provided variables (key-value pairs) to a JSON file
        with open(file_name, 'w') as json_file:
            json.dump(kwargs, json_file, indent=4)
        print(f"Successfully written to {file_name}")
    except Exception as e:
        print(f"Error writing to JSON file: {str(e)}")

# Add headless mode to run without opening the browser window
options.add_argument("--headless")

# Starting up the web driver used to control chrome
driver = webdriver.Chrome(options=options)

# 
driver.get("https://permits.cob.org/eTRAKiT/Search/permit.aspx")

sleep(1)

def print_all_ids(driver):
    try:
        # Get all elements in the document
        elements = driver.find_elements_by_xpath("//*")  # Select all elements
        ids = [element.get_attribute("id") for element in elements if element.get_attribute("id")]  # Get IDs
        if ids:
            print("IDs in the document:")
            for id in ids:
                print(id)
        else:
            print("No IDs found in the document.")
    except Exception as e:
        print(f"Error retrieving IDs - {str(e)}")

# Function to click a button with a specific ID
def click_button_by_id(driver, element_id):
    try:
        button = driver.find_element(By.ID, element_id)
        button.click()
        print(f"Clicked button with ID: {element_id}")
        return True
    except Exception as e:
        print(f"Error clicking button with ID: {element_id} - {str(e)}")
        return False

# Function to enter text into a field with a specific ID
def enter_text_by_id(driver, element_id, input_text):
    try:
        input_field = driver.find_element(By.ID, element_id)
        input_field.clear()  # Clear the field before entering text
        input_field.send_keys(input_text)
        print(f"Entered text into element with ID: {element_id}")
    except Exception as e:
        print(f"Error entering text into element with ID: {element_id} - {str(e)}")

# Function to get inner HTML from an element with a specific ID
def get_inner_html_by_id(driver, element_id):
    try:
        element = driver.find_element(By.ID, element_id)
        inner_html = element.get_attribute('innerHTML')
        print(f"Inner HTML from element with ID {element_id}: {inner_html}")
        return inner_html
    except Exception as e:
        print(f"Error retrieving inner HTML from element with ID: {element_id} - {str(e)}")
        return None
    
def wait_for_element_by_custom_id(driver, prefix, suffix):
    try:
        # Wait for an element with an ID that starts with prefix and ends with suffix
        element = WebDriverWait(driver, 1).until(
            EC.visibility_of_element_located((By.XPATH, f"//*[starts-with(@id, '{prefix}') and substring(@id, string-length(@id) - string-length('{suffix}') + 1) = '{suffix}']"))
        )
        inner_html = element.get_attribute('innerHTML')
        print(f"Inner HTML from element with ID prefix:{prefix} suffix:{suffix}: {inner_html}")

        return inner_html
    except Exception as e:
        print(f"Error waiting for element with prefix '{prefix}' and suffix '{suffix}': {str(e)}")
        return None

def click_element_by_class_and_text(driver, class_name, inside):
    try:
        # Find all elements with the specified class
        elements = driver.find_elements(By.CLASS_NAME, class_name)
        
        # Loop through elements to find the one with the desired text
        for element in elements:
            if element.text == inside:
                element.click()
                print(f"Clicked on element with class '{class_name}' and text '{inside}'")
                return True
        print(f"No element found with class '{class_name}' and text '{inside}'")
        return False
    except Exception as e:
        print(f"Error finding or clicking element with class '{class_name}' and text '{inside}' - {str(e)}")
        return False
    
def get_child_elements(parent_element):
        try:
            # Find all child elements inside the parent element
            child_elements = parent_element.find_elements(By.XPATH, "./*")
            
            # Return the list of child elements
            return child_elements
        except Exception as e:
            print(f"Error getting child elements: {str(e)}")
            return []

def get_child_elements_by_id(driver, element_id):
    
    try:
        parent_element = driver.find_element(By.ID, element_id)
        
        # Get the child elements
        children = get_child_elements(parent_element)
        inners = []

        # Print the tag names of the child elements
        for child in children:
            inner_html = child.get_attribute('innerHTML')
            inners.append(inner_html)
            
            print(inner_html)
            
        return inners
    except Exception as e:
        print(f"Error in example usage: {str(e)}")
        return []

def get_child_elements_by_custom_id(driver, prefix, suffix):
    try:
        # Wait for a parent element with an ID that starts with prefix and ends with suffix
        parent_element = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.XPATH, f"//*[starts-with(@id, '{prefix}') and substring(@id, string-length(@id) - string-length('{suffix}') + 1) = '{suffix}']"))
        )

        # Get the child elements of the found parent element
        children = parent_element.find_elements(By.XPATH, "./*")  # Direct children of the parent
        inners = []

        # Collect and print the inner HTML of the child elements
        for child in children:
            inner_html = child.get_attribute('innerHTML')
            inners.append(inner_html)
            print(inner_html)

        return inners

    except Exception as e:
        print(f"Error finding elements with prefix '{prefix}' and suffix '{suffix}': {str(e)}")
        return []

# print all ids available to us
print_all_ids(driver=driver)

# enter login username
enter_text_by_id(driver=driver, element_id='cplMain_txtPublicUserName', input_text='jacknelsongardner')
# enter login passkey
enter_text_by_id(driver=driver, element_id='cplMain_txtPublicPassword', input_text='Xfiles1!')
# press button to login
click_button_by_id(driver=driver, element_id='cplMain_btnPublicLogin')


# taken to page for searching 

for i in range(70, 9999):
    
    number_str = str(i).zfill(4)  # Converts the number to a string and pads with leading zeros
    print(number_str)
        
    # enter id of next 
    enter_text_by_id(driver=driver, element_id='cplMain_txtSearchString', input_text=f'BLD2024-{number_str}')
    # enter search button 
    click_button_by_id(driver=driver, element_id='ctl00_cplMain_btnSearch')

    sleep(2)

    # click on the resulting row
    if not click_button_by_id(driver=driver, element_id='ctl00_cplMain_rgSearchRslts_ctl00__0'):
        # if the resulting row doesn't exist, we break early
        print(number_str)
        break 

    sleep(5)
    # taken to page with item information
    # Get the entire HTML of the page
    html = driver.page_source

    # Save the HTML content to a file
    with open("page_source.html", "w", encoding='utf-8') as file:
        file.write(html)
    print("HTML content saved to 'page_source.html'.")


    # get permit info 
    permit_type = wait_for_element_by_custom_id(driver=driver, prefix='cplMain_ctl', suffix='_lblPermitType')

    permit_description = wait_for_element_by_custom_id(driver=driver, prefix='cplMain_ctl', suffix='_lblPermitDesc')
    permit_status = wait_for_element_by_custom_id(driver=driver, prefix='cplMain_ctl', suffix='_lblPermitStatus')

    permit_apply_date = wait_for_element_by_custom_id(driver=driver, prefix='cplMain_ctl', suffix='_lblPermitAppliedDate')
    permit_approve_date = wait_for_element_by_custom_id(driver=driver, prefix='cplMain_ctl', suffix='_lblPermitApprovedDate')

    permit_issued_date = wait_for_element_by_custom_id(driver=driver, prefix='cplMain_ctl', suffix='_lblPermitIssuedDate')
    permit_finaled_date = wait_for_element_by_custom_id(driver=driver, prefix='cplMain_ctl', suffix='_lblPermitFinaledDate')
    permit_expiration_date = wait_for_element_by_custom_id(driver=driver, prefix='cplMain_ctl', suffix='_lblPermitExpirationDate')


    # click on additional info tab
    click_element_by_class_and_text(driver=driver, class_name='rtsTxt', inside='Site Info')


    # getting address
    address_street = wait_for_element_by_custom_id(driver=driver, prefix='cplMain_ctl', suffix='_hlSiteAddress')
    address_state = wait_for_element_by_custom_id(driver=driver, prefix='cplMain_ctl', suffix='_lblSiteCityStateZip')
    address_full = address_street + " " + address_state

    # getting lot info
    lot_info = wait_for_element_by_custom_id(driver=driver, prefix='cplMain_ctl', suffix='_lblSectionTwpRng')

    # click on contacts tab 
    click_element_by_class_and_text(driver=driver, class_name='rtsTxt', inside='Contacts')

    tally = 0
    contacts = []

    while True:
        # getting contact info chart
        contact = get_child_elements_by_custom_id(driver=driver, prefix='ctl00_cplMain_ctl', suffix=f'_rgContactInfo_ctl00__{tally}')


        if contact:
            # filing contact info
            contact_role = contact[0]
            contact_company = contact[1]
            contact_phone = contact[2]
            contact_email = contact[3]

            contact_address_street = contact[4]
            contact_address_state = contact[5]
            contact_address_full = contact_address_street + ' ' + contact_address_state

            contact_info = {
                'role':contact_role,
                'company':contact_company,
                'phone':contact_phone,
                'email':contact_email,
                'street':contact_address_street,
                'state':contact_address_state,
                'address':contact_address_full
            }

            contacts.append(contact_info)
            
            # increase tally to go to next contact
            tally = tally + 1
        else:
            break
    
    write_to_json(f'data/bellingham/BLD/2024-{number_str}.json', type=permit_type, apply_date=permit_apply_date, approve_date=permit_approve_date, description=permit_description, expiration_date=permit_expiration_date, finaled_date=permit_finaled_date, issued_date=permit_issued_date, address=address_full, status=permit_status, contact=contacts)

    # resetting process from search step
    driver.get("https://permits.cob.org/eTRAKiT/Search/permit.aspx")


sleep(1)



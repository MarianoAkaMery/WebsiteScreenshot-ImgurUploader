import requests
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import base64

def screenshot_to_imgur():
    """
    Takes a screenshot of a given website and uploads it to Imgur.
    """
    
    # Set up the Chrome web driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    # Navigate to the desired website
    driver.get('YOUR_WEBSITE_URL')  # Replace with your website URL
    sleep(4)  # Pause to let the website load completely
    
    # Capture the screenshot and save it
    screenshot_path = "screen/screenshot.png"
    driver.get_screenshot_as_file(screenshot_path)
    driver.quit()
    
    # Convert the screenshot to a base64 string
    with open(screenshot_path, "rb") as image_file:
        base64_string = base64.b64encode(image_file.read()).decode()
    
    # Upload the image to Imgur
    imgur_endpoint = "https://api.imgur.com/3/image"
    headers = {'Authorization': 'Client-ID YOUR_IMGUR_CLIENT_ID'}  # Replace with your Imgur Client ID
    response = requests.post(imgur_endpoint, headers=headers, data={'image': base64_string})
    image_url = json.loads(response.text)['data']['link']

    print(f"Here you can find your image URL: {image_url}")

# Run the function
screenshot_to_imgur()

import requests
import json
from discord_webhook import DiscordWebhook, DiscordEmbed
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import base64

def screenshot_to_imgur_discord():
    """
    Takes a screenshot of a given website, uploads it to Imgur,
    and then sends it as an embed to a Discord webhook.
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
    
    # Send the image to Discord via a webhook
    webhook_url = "YOUR_DISCORD_WEBHOOK_URL"  # Replace with your Discord webhook URL
    webhook = DiscordWebhook(url=webhook_url)
    embed = DiscordEmbed(title="Your Image is here", description="Coded by Mery", color=0xFF0000)
    embed.set_footer(text="WebhookTitle", icon_url="YOUR_FOOTER_ICON_URL")  # Replace with your footer icon URL
    embed.set_timestamp()
    embed.set_image(url=image_url)
    webhook.add_embed(embed)
    webhook.execute()

# Run the function
screenshot_to_imgur_discord()

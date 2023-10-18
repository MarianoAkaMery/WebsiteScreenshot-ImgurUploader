import requests
import json
import base64

def upload_image_to_imgur():
    """
    Uploads a local image file to Imgur.
    """
    
    # Define the path to your image file
    image_path = "screen/screenshot.png"
    
    # Convert the image to a base64 string
    with open(image_path, "rb") as image_file:
        base64_string = base64.b64encode(image_file.read()).decode()
    
    # Upload the image to Imgur
    imgur_endpoint = "https://api.imgur.com/3/image"
    headers = {'Authorization': 'Client-ID YOUR_IMGUR_CLIENT_ID'}  # Replace with your Imgur Client ID
    response = requests.post(imgur_endpoint, headers=headers, data={'image': base64_string})
    image_url = json.loads(response.text)['data']['link']

    print(f"Here you can find your image URL: {image_url}")

# Run the function
upload_image_to_imgur()

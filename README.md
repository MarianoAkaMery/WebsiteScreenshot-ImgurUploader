# WebsiteScreenshot-ImgurUploader

Automate the process of capturing screenshots from websites, uploading images to Imgur, and optionally sending images directly to Discord!

## Features

- **Website Screenshot Capture**: Easily take screenshots of any specified website.
- **Imgur Uploader**: Seamlessly upload both captured screenshots and local image files to Imgur.
- **Discord Integration**: Optionally send your images directly to a Discord channel using webhooks.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [Capture & Upload](#capture--upload)
  - [Local Image to Imgur](#local-image-to-imgur)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/MarianoAkaMery/WebsiteScreenshot-ImgurUploader.git
   ```

2. Navigate to the directory:

   ```bash
   cd WebsiteScreenshot-ImgurUploader
   ```

3. (Optional) It's recommended to set up a virtual environment:

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows, use `env\Scripts\activate`
   ```

4. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Capture & Upload

To capture a screenshot of a website and upload it to Imgur:

```bash
python screenshot_to_imgur.py
```

### Local Image to Imgur

To upload a local image to Imgur:

```bash
python file_to_imgur.py
```

## Configuration

Before running the scripts, make sure to replace placeholders in the code:

- `YOUR_WEBSITE_URL`: The website you wish to capture a screenshot of.
- `YOUR_IMGUR_CLIENT_ID`: Your Imgur API client ID for uploading images.
- `YOUR_DISCORD_WEBHOOK_URL`: (Optional) Your Discord webhook URL if you want to send images to Discord.

## Contributing

Contributions are welcome! Please read the [contributing guidelines](CONTRIBUTING.md) to get started.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

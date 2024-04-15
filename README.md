# Nullspace LLC - Example Raspberry Pi Timelapse Script

This Python script facilitates the automated process of capturing an image on a Raspberry Pi, uploading it to a cloud storage in [null-space.xyz](https://null-space.xyz), and then deleting the image from the local filesystem to manage storage efficiently.

## Steps Overview

1. **Obtain Image URL**: Initially, the script contacts an API endpoint provided by null-space.xyz to fetch a URL and necessary fields for securely uploading an image. This request includes an authorization header using an API key.

2. **Capture Image**: In this step, the script is intended to interface with the Raspberry Pi's camera to capture an image. This function can be replaced with different camera interaction code.

3. **Upload Image**: With the captured image, the script uploads it using the image URL to the designated upload endpoint.

4. **Delete Local Image**: The script deletes the image from the Raspberry Pi to clear storage space and keep the system ready for the next operation.

## Installation and Setup

### Prerequisites
Ensure Python and pip are installed on your Raspberry Pi. Python 3 is recommended.

### Install Required Libraries
Install all necessary Python libraries using the provided `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Add your API key and Timelapse ID
Insert your API_KEY from the 'Account' page on [null-space.xyz](https://null-space.xyz) at the top of `upload.py`
The timelapse id is up for you to decide.

### Setup a Cron Job on the PI to run the script
```bash
crontab -e

# Add this cron job schedule to the file
*/10 4-22 * * * /usr/bin/python3 /home/pi/upload.py

# */10 = every 10 minutes, 4-22 = every hour from 4 AM to 10 PM inclusive, * * * = every day of month, every month, every day
```
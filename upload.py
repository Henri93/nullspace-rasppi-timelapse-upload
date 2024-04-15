import requests
import os
import time
from picamera2 import Picamera2

timelapse_id = "my-sick-timelapse"
api_key = "YOUR_API_KEY"

def get_upload_url_and_auth():
    """
    Makes a request to the specified API endpoint to get a pre-signed URL and additional fields.
    """
    headers = {'Authorization': api_key}
    response = requests.get(f"https://api.null-space.xyz/image-url?timelapse-id={timelapse_id}", headers=headers)
    response.raise_for_status()
    data = response.json()['body']
    return data['url'], data['fields']

def capture_image(file_path):
    """
    Image capturing
    """
    picam2 = Picamera2()
    camera_config = picam2.create_still_configuration(main={"size": (1920, 1080)})
    picam2.configure(camera_config)
    picam2.start()
    picam2.capture_file(file_path)
    time.sleep(2) # give a litte wait before closing the camera
    picam2.close()

def upload_image(url, fields, file_path):
    """
    Uploads an image to a given pre-signed URL using additional fields required by S3.
    The POST request uses multipart/form-data encoding.
    """
    with open(file_path, 'rb') as file:
        files = {'file': ('tmp_image.jpg', file, 'image/jpeg')}
        # Include all authorization fields from the upload URL response
        response = requests.post(url, data=fields, files=files)
        response.raise_for_status()

def cleanup_image(file_path):
    """
    Deletes an image from the local file system.
    """
    os.remove(file_path)

def main():
    image_path = 'tmp_image.jpg'
    
    try:
        # Step 1: Get image upload URL and authorization
        url, fields = get_upload_url_and_auth()
        
        # Step 2: Capture image
        capture_image(image_path)
        
        # Step 3: Upload the image
        upload_image(url, fields, image_path)

        print("Image captured and uploaded successfully.")
    except Exception as e:
        print(f"An error occurred during upload: {e}")
    finally:
        # Step 4: Cleanup the image from local filesystem
        cleanup_image(image_path)
        print("Image has been deleted from local storage.")

if __name__ == '__main__':
    main()

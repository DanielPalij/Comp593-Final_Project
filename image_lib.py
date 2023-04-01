import requests
import os
from sys import argv
import ctypes
'''
Library of useful functions for working with images.
'''
def main():
    # TODO: Add code to test the functions in this module
   
    image_filename = argv[0]
    
    image_path = os.path.join(os.environ["TEMP"], image_filename)

    image_url = 'https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__340.jpg'
    image_data = download_image(image_url)
    save_image_file(image_data, image_path)
    set_desktop_background_image(image_path)
    
    return

def download_image(image_url):
    """Downloads an image from a specified URL.

    DOES NOT SAVE THE IMAGE FILE TO DISK.

    Args:
        image_url (str): URL of image

    Returns:
        bytes: Binary image data, if succcessful. None, if unsuccessful.
    """
    
    resp_msg = requests.get(image_url)
    # Check whether the download was successful
    
    if resp_msg.status_code == requests.codes.ok:
    # Extract binary file content from response message
        image_content = resp_msg.content
        print('Download Complete')
        return image_content
    else:
        print('Download Incomplete')
        return None

def save_image_file(image_data, image_path):
    """Saves image data as a file on disk.
    
    DOES NOT DOWNLOAD THE IMAGE.

    Args:
        image_data (bytes): Binary image data
        image_path (str): Path to save image file

    Returns:
        bytes: True, if succcessful. False, if unsuccessful
    """
    try:
        with open(image_path, 'wb') as file:
            file.write(image_data)
            print('saved')
        return True 
    except:
        return False
    
    

def set_desktop_background_image(image_path):
    """Sets the desktop background image to a specific image.

    Args:
        image_path (str): Path of image file

    Returns:
        bytes: True, if succcessful. False, if unsuccessful        
    """
    try:
        ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 0)
        return True
    except:
        print('Error Setting Background')
        return False


def scale_image(image_size, max_size=(800, 600)):
    """Calculates the dimensions of an image scaled to a maximum width
    and/or height while maintaining the aspect ratio  

    Args:
        image_size (tuple[int, int]): Original image size in pixels (width, height) 
        max_size (tuple[int, int], optional): Maximum image size in pixels (width, height). Defaults to (800, 600).

    Returns:
        tuple[int, int]: Scaled image size in pixels (width, height)
    """
    ## DO NOT CHANGE THIS FUNCTION ##
    # NOTE: This function is only needed to support the APOD viewer GUI
    resize_ratio = min(max_size[0] / image_size[0], max_size[1] / image_size[1])
    new_size = (int(image_size[0] * resize_ratio), int(image_size[1] * resize_ratio))
    return new_size

if __name__ == '__main__':
    main()
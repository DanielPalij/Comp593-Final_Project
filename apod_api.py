'''
Library for interacting with NASA's Astronomy Picture of the Day API.
'''
import requests
from sys import argv

apod_url = 'https://api.nasa.gov/planetary/apod'
api_key = 'xmXuRKXZNZkoJSGzL1X3PbZjvdbBm0YzJ2rE60lh'

def main():
    # TODO: Add code to test the functions in this module
    return

def get_apod_info(apod_date):
    """Gets information from the NASA API for the Astronomy 
    Picture of the Day (APOD) from a specified date.

    Args:
        apod_date (date): APOD date (Can also be a string formatted as YYYY-MM-DD)

    Returns:
        dict: Dictionary of APOD info, if successful. None if unsuccessful
    """
    apod_params = {
            'api_key' : api_key,
            'date' : apod_date,
            'thumbs' : 'True'
    }
      
    
    resp_msg = requests.get(f'{apod_url}',params=apod_params)
    print(resp_msg.json())
    if resp_msg.status_code == requests.codes.ok:
        return  resp_msg.json()
    else:
        return None

def get_apod_image_url(apod_info_dict):
    """Gets the URL of the APOD image from the dictionary of APOD information.

    If the APOD is an image, gets the URL of the high definition image.
    If the APOD is a video, gets the URL of the video thumbnail.

    Args:
        apod_info_dict (dict): Dictionary of APOD info from API

    Returns:
        str: APOD image URL
    """
    print(apod_info_dict)
    media = apod_info_dict['media_type']
    if media == 'image':
        return apod_info_dict['hdurl']
    
    elif media == 'video':
        return apod_info_dict['thumbnail_url']
    
    else:
        return ValueError(f"Unsupported media type '{media}'")

if __name__ == '__main__':
    main()
"""фото потрiбно розпарсити i потiм за допомогою додаткових
 запитiв скачати i зберiгти цi фото як локальнi файли mars_photo1.jpg , mars_photo2.jpg"""

import requests
from requests.exceptions import HTTPError, ConnectionError, MissingSchema

url_basic = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
params = {'sol': 1000, 'camera': 'fhaz', 'api_key': 'DEMO_KEY'}

try:
    response = requests.get(url_basic, params=params)
    response.raise_for_status()  # raises HTTPError in case of status_codes != 2xx

    data = response.json()  # JSON answer as Python dict
    photos_info = data.get("photos", None)

    if photos_info is None:
        raise ValueError("No Photo info was loaded")
    else:
        for i, item in enumerate(photos_info, start=1):
            img_url = item.get("img_src", None)

            try:
                img_response = requests.get(img_url)
                img_response.raise_for_status()

                img_file_name = "mars_photo" + str(i) + ".jpg"
                with open(img_file_name, "wb") as img:
                    img.write(img_response.content)

            except HTTPError as he:
                print(f"There is a HTTP error occurred :{he.response}")
                print(f"{he.__repr__()}\n")
            except ConnectionError as ce:
                print(f"There is a Connection error occurred: {ce.__repr__()}\n")
            except MissingSchema as msch:
                print(f"Cannot retrieve any data due to invalid or incomplete URL: {msch}")
            except Exception as exc:
                print(f"There is an error occurred: {exc.__repr__()}\n")



except Exception as e:
    print(f"An exception was caught: {repr(e)}")

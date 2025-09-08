"""написати код який використовуючи модуль request зробить через POST upload якогось зображення на сервер,
 за допомогою GET отримає посилання на цей файл и потiм за допомогою DELETE зробить видалення файлу з сервера"""
import requests
from requests.exceptions import HTTPError, ConnectionError
import os

def decorator_for_handling_errors(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except HTTPError as he:
            print(
                f"There is a HTTP error occurred :{he.response}, while attempting to {kwargs.get('action')} {kwargs.get('file_name')}")
            print(f"{he.__repr__()}\n")
        except ConnectionError as ce:
            print(
                f"There is a Connection error occurred, while attempting to {kwargs.get('action')} {kwargs.get('file_name')}")
            print(f"{ce.__repr__()}\n")
        except Exception as exc:
            print(
                f"There is an error for the file {kwargs.get('file_name')} occurred, while attempting to {kwargs.get('action')}")
            print(f"{exc.__repr__()}\n")

    return wrapper


@decorator_for_handling_errors
def upload_files(url, upl_file, **kwargs):
    with open(upl_file, 'rb') as img:
        files_to_upload = {'image': (upl_file, img, 'image/jpeg')}

        response = requests.post(url, files=files_to_upload)
        response.raise_for_status()
        print(response.status_code, response.json())


@decorator_for_handling_errors
def download_files(url, file_to_download, **kwargs):
    content_type = ['image', 'text']
    loaded_file_name = "loaded_" + file_to_download

    for ct in content_type:
        headers1 = {'Content-Type': ct}
        response1 = requests.get(url, headers=headers1)
        response1.raise_for_status()

        if response1.status_code == 200:
            if ct == content_type[0]:
                with open(loaded_file_name, 'wb') as loaded:
                    loaded.write(response1.content)
            elif ct == content_type[1]:
                print(response1.json())


@decorator_for_handling_errors
def delete_files(url, file_to_del, **kwargs):
    response2 = requests.delete(url)
    response2.raise_for_status()
    if response2.status_code == 200:
        print(response2.json())

    downloaded_file_name = "loaded_" + file_to_del
    if os.path.exists(downloaded_file_name):
      os.remove(downloaded_file_name)
    else:
      print(f"The file {downloaded_file_name} does not exist")


images = ['cherry.jpeg', 'apples.jpeg']
BASE_URL = "http://127.0.0.1:8080/"
# POST files
for i in images:
    post_url = BASE_URL + "upload"
    upload_files(post_url, i, action="upload", file_name=i)

# GET files
for i in images:
    geturl = BASE_URL + f"image/{i}"
    download_files(geturl, i, action='download', file_name=i)

# DELETE files
for i in images:
    deleteurl = BASE_URL + f"delete/{i}"
    delete_files(deleteurl, i, action='delete', file_name=i)

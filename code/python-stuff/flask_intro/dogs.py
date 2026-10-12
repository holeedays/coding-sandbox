import requests
from requests import Response
from .utils import create_file

def get_dogs() -> list[str]:
    response = requests.get("https://dog.ceo/api/breeds/image/random/2")
    return response.json()["message"]


def get_dogs_local() -> list[str]:
    # holds all the local files 
    dog_img_file_paths: list[str] = []

    img_count: int = 4
    url: str = "https://dog.ceo/api/breeds/image/random" + f"/{img_count}"
    response: Response = requests.get(url)
    dog_imgs: list[str] = response.json()["message"]
    for i, img in enumerate(dog_imgs):
        raw_img_bytes: bytes = requests.get(img).content
        file_name: str = f"dog_{i}.jpg"

        # the reason for using the flask intro header is because im treating flas_intro dir as a module and I'm calling it from
        # python-stuff director (the parent directory)
        file_path: str = "flask_intro/static/" + file_name

        # create the file
        create_file(raw_img_bytes, file_path)

        # append the created file path to our dog_img_file_paths
        dog_img_file_paths.append(file_name)

    return dog_img_file_paths
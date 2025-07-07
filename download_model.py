import gdown
import os

os.makedirs("models",exist_ok=True)


def download_model(file_id,name):
    
    url = f"https://drive.google.com/uc?id={file_id}"
    gdown.download(url,f"models/{name}")


download_model("165IPUEwUbukYadd-0nkRMUlML9H4mp0p","plant.pth")
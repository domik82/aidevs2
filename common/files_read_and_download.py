from urllib.parse import urlparse

import requests
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}


def download_file(url: str, path: str = './', retries: int = 5, timeout: int = 30) -> None:
    for i in range(retries):
        try:
            response = requests.get(url, headers=headers, timeout=timeout)
            response.raise_for_status()
            filename = get_file_name(url)
            with open(f'{path}/{filename}', 'wb') as f:
                f.write(response.content)
        except (requests.exceptions.RequestException, IOError):
            if i == retries - 1:
                raise
            else:
                time.sleep(2 ** i)


def read_file_contents(filepath: str) -> str:
    with open(filepath, 'r') as f:
        contents = f.read()
    return contents


def get_file_name(url: str) -> str:
    return urlparse(url).path.split("/")[-1]

import os
import requests
import urllib.parse


def get_dir_all_full_path(target_dir):
    file_full_paths = []
    for root, dirs, files in os.walk(target_dir, topdown=False):
        for name in files:
            current_file_full_path = os.path.join(root, name)
            file_full_paths.append(current_file_full_path)
    return file_full_paths


def addslashes(strings):
    if isinstance(strings, bytes):
        strings = strings.decode("utf-8")
    not_allow_chars = ["\\", '"', "'", "\0", ]
    for i in not_allow_chars:
        if i in strings:
            strings = strings.replace(i, '\\' + i)
    return strings


def url_encode(target_url):
    return urllib.parse.quote_plus(target_url)


def url_decode(target_url):
    return urllib.parse.unquote_plus(target_url)


def save_image(image_url, file_full_path):
    try:
        response = requests.get(image_url)
        with open(file_full_path, "wb") as fh:
            fh.write(response.content)
    except Exception as error:
        print(error)
        pass

    return file_full_path if os.path.exists(file_full_path) else False


if __name__ == '__main__':
    target_dir = os.getcwd()

    file_full_paths = get_dir_all_full_path(target_dir)

    print(file_full_paths)

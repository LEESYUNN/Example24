import os


def get_dir_all_full_path(target_dir):
    file_full_paths = []
    for root, dirs, files in os.walk(target_dir, topdown=False):
        for name in files:
            current_file_full_path = os.path.join(root, name)
            file_full_paths.append(current_file_full_path)
    return file_full_paths


if __name__ == '__main__': 

    target_dir = os.getcwd()

    file_full_paths = get_dir_all_full_path(target_dir)

    print(file_full_paths)


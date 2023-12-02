import os
import shutil

files = []


def collect_media_files(path):
    # List all files and directories in the current path
    contents = os.listdir(path)

    # Iterate through each item in the directory
    for item in contents:
        item_path = os.path.join(path, item)

        # Check if the current item is a directory
        if os.path.isdir(item_path):
            # If it's a "media" folder, collect file paths
            if item.lower() == 'media':
                collect_files_in_media_folder(item_path)
            else:
                # Recursively call the function for subdirectories
                collect_media_files(item_path)


def collect_files_in_media_folder(media_path):
    # List all files in the "media" folder
    media_contents = os.listdir(media_path)

    # Iterate through each file in the "media" folder
    for media_item in media_contents:
        media_item_path = os.path.join(media_path, media_item)

        # Check if the current item is a file
        if os.path.isfile(media_item_path):
            # Add the full path to the files array
            files.append(media_item_path)


def copy_file(src_path, dest_path):
    try:
        # Copy the file from src_path to dest_path
        shutil.copy(src_path, dest_path)
        print(f"File copied successfully from {src_path} to {dest_path}")
    except FileNotFoundError:
        print(f"Error: {src_path} not found.")
    except PermissionError:
        print(f"Error: Permission denied to copy {src_path} to {dest_path}")
    except Exception as e:
        print(f"Error: {e}")


# Example usage:
if __name__ == '__main__':
    collect_media_files(os.getcwd())
    collected = os.path.join(os.getcwd(), 'colected_media')
    try:
        os.mkdir(collected)
    except FileExistsError:
        pass
    # Print the collected file paths
    for file_path in files:
        file_name = os.path.split(file_path)[-1]
        copy_file(file_path, os.path.join(collected, file_name))

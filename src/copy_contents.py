import os
import shutil

def remove_public_content(root_dir):
    dir_content = os.listdir(root_dir)

    if not dir_content:
        return

    for item in dir_content:
        full_path = root_dir + "/" + item
        if os.path.isfile(full_path):
            os.remove(full_path)
        else:
            shutil.rmtree(full_path)
    return 

def copy_content(current_dir, copied):
    dir_content = os.listdir(current_dir)

    for item in dir_content:
        full_path = current_dir + "/" + item
        if os.path.isdir(full_path):

            if full_path not in copied:
                copy_content(full_path, copied)

        elif os.path.isfile(full_path):
            filename = os.path.basename(full_path)
            
            directories = full_path.replace(item, "")
            nested_dirs = directories.replace("./static", "")
            if nested_dirs != "/":
                destination_path = os.path.join("./public/" + nested_dirs, filename)
                os.makedirs("./public/" + nested_dirs, exist_ok=True)
                shutil.copy(full_path, destination_path)
            else:
                shutil.copy(full_path, "./public")
            copied.append(full_path)
    return copied



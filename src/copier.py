import os 
import shutil

def copy_content_to_public(src_dir):
    dest_dir = "./public"
    
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
    os.makedirs(dest_dir, exist_ok=True)

    copier(src_dir, dest_dir)


def copier(src_dir, dest_dir):
    if os.path.isfile(src_dir):
        os.makedirs(os.path.dirname(dest_dir), exist_ok=True)
        shutil.copy(src_dir, dest_dir)
    else:
        for name in os.listdir(src_dir):
            src_path = os.path.join(src_dir, name)
            dest_path = os.path.join(dest_dir, name)
            copier(src_path, dest_path)
    

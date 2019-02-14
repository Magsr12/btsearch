import os

def clean_pyc_files():
    current_dir = os.getcwd()
    for file in os.listdir(current_dir):
        if '.pyc' in file:
            os.remove(file)
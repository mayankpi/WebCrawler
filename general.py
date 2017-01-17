import os

def create_new_project(directory):
    if not os.path.exists(directory):
        print("creating directory")
        os.makedirs(directory)

create_new_project('mayankwebcrawler')
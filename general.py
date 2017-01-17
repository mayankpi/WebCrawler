import os

def create_project_dir(directory):
    if not os.path.exists(directory):
        print("creating directory")
        os.makedirs(directory)

#create_project_dir('mayankwebcrawler')


#creating queued and crawled files
def create_data_file(project_name, base_url):
    queue = project_name + "/queue.txt"
    crawled = project_name + "/scrawled.txt"
    if not os.path.isfile(queue):
        write_file(queue,base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')

#creating new file
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()

#add more urls to the existing file
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data,"\n")

#delete the contents of the given file
def delete_file_content(path):
    with open(path, 'w'):
        pass
import pkg_resources
import os

installed_packages = pkg_resources.working_set
installed_packages_list = sorted(["%s" % (i.key) for i in installed_packages])

current_directory = os.getcwd()

listInPIP = set()

for root, dirs, files in os.walk(current_directory):
    for file in files:
        if file.endswith('.py'):
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding="utf-8") as file:
                content = file.read()
            for listPiP in installed_packages_list:
                if str(listPiP) in str(content):
                    listInPIP.add(listPiP)

with open('requirements.txt', 'w') as req_file:
    for package in listInPIP:
        req_file.write(package + '\n')

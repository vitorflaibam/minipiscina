import sys
import os
import re

class WrongNumberOfArgs(Exception):
    pass

def create_list():
	with open("settings.py", "r") as settings:
		data_list = []
		for line in settings:
			data_list.append([(x.strip(" \n\"")) for x in line.split('=', 1)])
	return dict(data_list) 


def render_template(file_name, dic):
    with open(file_name) as file:
        content = file.read()
        for key, val in dic.items():
            content = content.replace("{%s}" % key, val)
        with open(os.path.splitext(file_name)[0] + ".html", "w") as new_file:
            new_file.write(content)

if __name__ == "__main__":
    try:
        if (len(sys.argv) != 2):
            raise WrongNumberOfArgs
        file_name = sys.argv[1]
        if (not file_name.endswith(".template")):
            print("Extension not supported", file = sys.stderr)
            exit(1)
        elif not os.path.isfile(file_name):
            print("404: File not found", file = sys.stderr)
            exit(1)
        settings_dic = create_list()
        render_template(file_name, settings_dic)
    except WrongNumberOfArgs:
        print("Wrong number or arguments")
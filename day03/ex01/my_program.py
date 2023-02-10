from local_lib import path

# The Python program you must create is a composition of your choice that must however observe these constrainsts:
# • Its extension must be .py because it’s a Python.

# • It must import the path.py module from the location where this library has been
# installed thanks to the previous script.

# • It must create a folder and a file inside this folder, write something in this file and
# then read and display its content.
# • It must respect the specific rules of the day

def path_file():
    path.Path("files/").rmtree()
    folder = path.Path("files/")
    folder.mkdir(mode= 0o777)
    file_path  = folder / "file.test"
    file_path.write_file("Hello, 42")
    print(file_path.read_text())


if __name__ == "__main__":
    path_file()
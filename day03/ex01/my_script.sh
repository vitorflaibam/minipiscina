#!/bin/sh

pip --version
pip install --target=local_lib --force-reinstall git+https://github.com/jaraco/path.git > installation.log

./my_program.py
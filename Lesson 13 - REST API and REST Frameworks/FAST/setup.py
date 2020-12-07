from distutils.core import setup
import os, sys
import docutils.io

setup(
    # app name
    name='RestAPI',
    # app version
    version='0.0.1',
    url="0.0.0.0/8080",
    # Application author details:
    author='Denem Orhun',
    author_email='denemorhun@gmail.com',
    # packages=['FAST',],
    license='Creative Commons Attribution license',
    long_description=open(os.path.join(sys.path[0], "README.txt")).read()
)
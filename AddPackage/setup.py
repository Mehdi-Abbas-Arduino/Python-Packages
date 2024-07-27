from setuptools import setup , find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'A basic ADD Package'
LONG_DESCRIPTION = 'A basic ADD Package long description'

setup(
    name= "Add"
    version=VERSION
    author= "Mehdi-Programmer"
    author_email="askmehdiabbas@gmail.com"
    description=DESCRIPTION
    long_description_content_type= "text/markdown"
    long_description=LONG_DESCRIPTION
    packages=find_packages()
    install_requires =[]
    keywords=['pyhton','add','sum','diff']
    classifiers={
        "Development_status : Ready to be used",
        "Audience : Developers",
        "Programming_language : Python - 3",
        "Operating-System : Microsoft-Windows"
    }
)
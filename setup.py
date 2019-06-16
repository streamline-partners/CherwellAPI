#!/usr/bin/env python

import setuptools
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), "r") as readme_file:
    long_description = readme_file.read()

setuptools.setup(
    name='CherwellAPI',
    version='1.3.1',
    author='Streamline Partners PTY Ltd',
    author_email='david.graupner@streamlinepartners.com.au',
    description='A Python library wrapper, abstracting the Cherwell REST API',
    url='',
    packages=setuptools.find_packages(),
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
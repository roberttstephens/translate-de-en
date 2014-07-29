#!/usr/bin/env python3
import os
from setuptools import setup

def read(fname):
    """
    Read a file in this directory.
    """
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="translate_de_en",
    version="0.1",
    author="Robert Tyler Stephens",
    author_email="roberttstephens@gmail.com",
    description=("Determine the miles per week for a hal higdon program."),
    license="GNU General Public License v3",
    url="https://github.com/roberttstephens/translate_de_en",
    packages=['translate_de_en'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
    ],
    install_requires=[
        'pyxdg'
    ],
    entry_points={
        'console_scripts': [
            'translate_de_en = translate_de_en.translate_de_en:main',
        ]
    },
)

import json
from os import path
from glob import glob
from setuptools import setup, find_packages


def get_requirements():
    requirements_fn = path.join(path.dirname(__file__), 'requirements.txt')
    with open(requirements_fn, 'r') as fh:
        requirements = [str(x).strip() for x in fh.readlines()]
    return requirements


def get_version(module_name):
    version_fn = path.join(module_name, "version.py")
    with open(version_fn) as fp:
        version = float(fp.readlines()[0].strip().split('=')[1].replace(' ', ''))
    return version


def get_data_files():
    data_files = ['README.md']
    if path.isdir("conf"):
        data_files.extend(glob(path.join("conf", "*")))
    return data_files


module_name = 'fastapi_sentiment'
version = get_version(module_name)

setup(
    name='fastapi-sentiment',
    version=version,
    description='Sentiment analysis API via FastAPI',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering"
    ],
    url='https://github.com/aagnone3/fastapi-sentiment',
    author='Anthony Agnone',
    author_email='anthonyagnone@gmail.com',
    entry_points={
        "console_scripts": [
            "serve=fastapi_sentiment.main:main"
        ]
    },
    packages=find_packages(exclude=['*.test', 'test']),
    install_requires=get_requirements(),
    zip_safe=False,
    data_files=[('share/{}'.format(module_name), get_data_files())]
)

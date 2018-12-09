import setuptools
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="tgclient",
    packages=setuptools.find_packages(),
    version='1.5.2',
    description='Telegram Bot Api Client',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='amirhossein faridvand',
    author_email='amirfaridvand@gmail.com',
    url='https://github.com/amir1379/tgclient',
    install_requires=['urllib3'],
    keywords='telegram bot api',
    license='GPL2',
    classifiers=[
        'Programming Language :: Python :: 3'
    ]
)

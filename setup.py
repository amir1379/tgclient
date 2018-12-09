import setuptools
from setuptools import setup


setup(
    name="tgclient",
    packages=['tgclient'],
    version='1.5.2',
    description='Telegram Bot Api Client',
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

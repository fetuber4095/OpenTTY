from setuptools import setup, find_packages

setup(
    name='opentty',
    version='1.5',
    author='Mr. Lima',
    author_email='felipebr4095@gmail.com',
    description='The OpenTTY is a Terminal Emulator created tottaly in python based-on Unix-Like Shells',
    long_description=open("README.md", "r").read(),
    long_description_content_type='text/markdown',
    url='https://github.com/fetuber4095/OpenTTY',
    packages=['.'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.11',
    ],
    keywords='python package, emulator, windows, linux, shell, project, posix, unix',
    install_requires=[
        
    ],
)

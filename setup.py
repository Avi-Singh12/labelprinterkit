from setuptools import setup, find_packages

with open('README.md', 'r') as readme:
    README_TEXT = readme.read()

setup(
    name="brother-label-printer",
    version="0.0.5",
    description="A library for creating and printing labels",
    use_scm_version=True,
    long_description=README_TEXT,
    long_description_content_type="text/markdown",
    url="https://github.com/Avi-Singh12/labelprinterkit.git",
    author="Avi Singh",
    author_email="singhavi@umich.edu",
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    license='Apache License, Version 2.0',
    keywords='',
    packages=find_packages(),
    install_requires=[
        'pillow',
        'pyusb',
        'packbits',
        'pyserial',
        'qrcode'
    ],
    python_requires='>=3.9'
)

# setup.py

from setuptools import setup, find_packages

setup(
    name="saha-sdk",
    version="0.1.0",
    description="Python SDK for the Saha Robotik REST API",
    author="Saha Robotik",
    author_email="support@saharobotik.com",
    url="https://github.com/saharobotik/saha-sdk-python",
    packages=find_packages(include=['saha_sdk', 'saha_sdk.*']),
    install_requires=[
        "requests>=2.0.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.7',
)

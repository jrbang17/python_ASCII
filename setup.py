from setuptools import setup, find_packages

setup(
    name="ascii_nametag",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pyfiglet",
    ],
    author="Your Name",
    author_email="your_email@example.com",
    description="A simple package to generate ASCII name tags",
)
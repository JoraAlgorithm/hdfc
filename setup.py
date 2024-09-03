from setuptools import setup, find_packages

setup(
    name="hdfc-extended",
    version="0.1.0",
    author="jorawar singh",
    author_email="jorawar.singh.capgemini.com",
    description="A extended package for HDFC Bank services",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/jorawarsinghcapgemini/hdfc-extended.git",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "requests",
        "numpy"
    ],
)


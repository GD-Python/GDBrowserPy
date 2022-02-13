
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="GDBrowserPy", 
    version="0.0.1",
    author="mel0n7",
    description="Use GDBrowserAPI with Python",
    # long_description=long_description,
    long_description_content_type="text/markdown",
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url="https://github.com/mel0n7/GDBrowserPy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
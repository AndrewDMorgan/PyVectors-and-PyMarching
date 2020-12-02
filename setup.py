import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="AndrewDMorgan",
    version="0.0.1",
    author="AndrewDMorgan",
    author_email="andrewdagamer741@gmail.com",
    description="Advanced Vector Types in Python3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AndrewDMorgan/PyVectors-and-PyMarching#readme",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tradier",
    version="0.0.1",
    author="Jeffrey Hu",
    author_email="jeffreyhu555@gmail.com",
    description="python client for connecting with tradier",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jeffhu1/python-tradier",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=["requests"],
)

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyratebay-gp2112",
    version="0.0.1",
    author="Guilherme Paixao",
    author_email="guipaixao2000@gmail.com",
    description="A python module for The Pirate Bay's API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gp2112/pyratebay",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Unlicense License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
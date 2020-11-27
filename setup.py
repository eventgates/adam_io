import setuptools
import version

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="adam_io",
    version=version.__version__,
    author="Kemal Çelikel",
    author_email="kcelikel@eventgates.com",
    description="ADAM 6050-D REST API Python Wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://adam-io.readthedocs.io/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="backoff_retry",
    version="0.0.1",
    author="Douglas Morais",
    author_email="msantos.douglas@gmail.com",
    description="Retry strategies for backoff",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/douglasmoraisdev/backoff_retry",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
	install_requires=[
        'backoff'
    ]    
)
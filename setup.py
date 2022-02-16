import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="test_py",
    version="1.0.0",
    author="Leonard Bruns",
    author_email="roym899@gmail.com",
    description="Minimalistic Python package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/roym899/test_py",
    py_modules=["test_py"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)

from setuptools import setup

with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

setup(
    name="pycolorprint",
    version="0.0.0",
    author="Jeongwon Song",
    author_email="jeongwon412@gmail.com",
    description="Colorful print formatter",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/jsong336/pycolorprint",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    package_data={"":[""]},
)
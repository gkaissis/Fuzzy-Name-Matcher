from distutils.core import setup
from setuptools import find_packages

setup(
    name="Fuzzy Name Matcher",
    version="0.1.0",
    author="Georgios Kaissis, Friederike Jungmann",
    author_email="",
    packages=find_packages(include=["fuzzy.*"]),
    scripts="fuzzy.py",
    url="",
    license="LICENSE.MD",
    description="Fuzzy Name Matcher.",
    long_description=open("README.MD").read(),
    install_requires=open("requirements.txt").read(),
    python_requires=">=3.7",
)

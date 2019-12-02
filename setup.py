from setuptools import setup, find_packages

setup(
    name="Fuzzy Name Matcher",
    version="0.1.0",
    author="Georgios Kaissis, Friederike Jungmann",
    author_email="",
    packages=find_packages(),
    url="https://github.com/gkaissis/Fuzzy-Name-Matcher",
    license="LICENSE.MD",
    description="Fuzzy Name Matcher.",
    long_description=open("README.MD").read(),
    install_requires=["fuzzywuzzy==0.17.0", "pandas==0.25.1", "python-Levenshtein==0.12.0", "tqdm==4.39.0"],
    python_requires=">=3.7",
)

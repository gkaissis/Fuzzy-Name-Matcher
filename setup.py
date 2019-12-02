from distutils.core import setup

setup(
    name="Fuzzy Name Matcher",
    version="0.1.0",
    author="Georgios Kaissis, Friederike Jungmann",
    author_email="",
    packages="",
    scripts="fuzzy.py",
    url="",
    license="LICENSE.MD",
    description="Fuzzy Name Matcher.",
    long_description=open("README.MD").read(),
    install_requires=open("requirements.txt").read(),
    python_requires="3.7",
)

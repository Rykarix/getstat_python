from setuptools import find_packages, setup

setup(
    name="getstat_python",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "ada_url==1.15.3",
        "coloredlogs==15.0.1",
        "lxml==5.3.0",
        "numpy==2.1.2",
        "pandas==2.2.3",
        "pydantic==2.9.2",
        "requests==2.32.3",
        "rich==13.9.2",
        "typing_extensions==4.12.2",
    ],
)

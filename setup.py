from setuptools import find_packages, setup

setup(
    name="getstat",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "ada_url>=1.15",
        "numpy>=2.0",
        "pandas>=2.0",
        "pydantic>=2.0",
        "requests>=2.0",
        "typing_extensions>=4.0",
    ],
)

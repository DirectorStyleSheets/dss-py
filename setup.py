from setuptools import setup, find_packages

setup(
    name='dss',
    version='0.0.0',
    packages=find_packages(),
    install_requires=[
        'pydantic>=1.10.0',
        'elevenlabs>=1.9.0',
    ],
)
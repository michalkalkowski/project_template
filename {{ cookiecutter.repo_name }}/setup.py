import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="{{ cookiecutter.python_module_name }}",
    description="{{ cookiecutter.description }}",
    author="{{ cookiecutter.author_name }}",
    author_email="{{ cookiecutter.author_email }}",
    packages=find_packages(exclude=['data', 'references', 'output', 'notebooks']),
    long_description=read('README.md'),
    license='MIT'
)

from setuptools import setup, find_packages
from pathlib import Path
from typing import List

requirements: List[str] = Path("requirements.txt").open().read().splitlines()
packages: List[str] = find_packages()

setup(
    name='gcl',
    version='0.01',
    description='An implementation of the Guided Cost Learning algorithm.',
    url='https://github.com/ahadjawaid/guided-cost-learning',
    author='Ahad Jawaid',
    install_requires=requirements,
    python_requires='>=3.10, <3.11',
    packages=packages
)
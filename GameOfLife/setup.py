from setuptools import setup, find_packages
import os

def read_requirements():
    requirements_path = os.path.join(os.path.dirname(__file__), 'requirements.txt')
    with open(requirements_path, 'r') as f:
        return f.read().splitlines()
    
setup(
    name="game_of_life",
    version="1.0.0",
    description="A Game of Life python simulation",
    author="Jonas Kemi",
    packages=find_packages(),
    install_requires=read_requirements(),
    python_requires=">=3.7",
)
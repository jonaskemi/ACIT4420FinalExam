from setuptools import setup, find_packages
import os

def read_requirements():
    """Read requirements from requirements.txt file"""
    requirements_path = os.path.join(os.path.dirname(__file__), 'requirements.txt')
    with open(requirements_path, 'r') as f:
        return f.read().splitlines()
    
setup(
    name="smart_courier",
    version="1.0.0",
    description="A courier delivery management system",
    author="Jonas Kemi",
    packages=find_packages(),
    install_requires=read_requirements(),
    python_requires=">=3.7",
)
from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [i.replace('\n', '') for i in requirements]

    return requirements

setup(
name = 'Investment Prediction',
version = '1.0.1',
author = 'Navanish',
author_email = 'navanishpandey17@gmail.com',
packages = find_packages(),
install_requires = get_requirements('requirements.txt')
)

  





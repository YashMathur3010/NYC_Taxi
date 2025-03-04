from setuptools import find_packages
from setuptools import setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(requirements_file: str) -> List[str]: 
      '''
      This function returns the list of packages required to be installed
      '''
      requirements = []
      with open(requirements_file) as req_file:
            requirements = req_file.readlines()
            requirements = [req.replace('\n', '') for req in requirements]

            if HYPHEN_E_DOT in requirements:
                  requirements.remove(HYPHEN_E_DOT)
      
      return requirements

setup(name = 'NYC_Taxi',
      version = '0.0.1',
      author = 'Yash Mathur',
      author_email = 'yash.mathur0701@gmail.com',
      packages = find_packages(),
      install_requires = get_requirements('requirements.txt'))
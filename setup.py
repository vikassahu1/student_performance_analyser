from setuptools import find_packages,setup
from typing import List

HYPHEN = '-e .'

def get_requirements(file_path)->List[str]:
    '''
        This funtcion will give the list of requirements from txt file.
    '''
    req = []
    with open(file_path) as file_obj:
        req = file_obj.readlines()
        req = [r.replace("\n","") for r in req]

        if HYPHEN in req:
            req.remove(HYPHEN)  

        return req


setup(
    name='mlprojects',
    version='0.0.1',
    author='Vikas Kumar Sahu',
    author_email='2003vikas0906@gmail.com',
    packages=find_packages('requirements.txt'),
    install_requires = ['pandas','numpy','seaborn']
)
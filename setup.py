from setuptools import find_packages,setup
from typing import List

IGNORE='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if IGNORE in requirements:
            requirements.remove(IGNORE)
    
    return requirements

setup(
name='mlproject',
version='0.0.1',
author='waqar',
author_email='waqarhdr134@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)
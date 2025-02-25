from setuptools import find_packages,setup
from typing import List


def get_requirement(file_path:str)->List[str]:
    requirement=[]
    with open (file_path) as file_obj:
        requirement=file_obj.readlines()
        requirement=[req.replace("\n","") for req in requirement]
        
        return requirement
        


setup(
     name='ML PROJECT',
     version='0.0.1',
     author='Sujata',
     author_email="datasciencelearning64@gmail.com",
     install_requires=get_requirement('requirement.txt'),
     packages=find_packages()
)
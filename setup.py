from setuptools import find_packages,setup
from typing import List

Hypen_e_dot= '-e .'
def get_requirements(file_path:str)->List[str]:
    #This function will return the list of requirements
    requirements=[]
    with open(file_path) as file_obj:
        requirements= file_obj.readlines()
        [req.replace ("\n","") for req in requirements]
        
        if Hypen_e_dot in requirements:
            requirements.remove(Hypen_e_dot)



setup(
    name='Mini_Project',
    version='0.0.1',
    Author= 'Manikandan',
    Auther_mail= 'mani1756067@gmail.com',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires= get_requirements('requirements.txt')
    )


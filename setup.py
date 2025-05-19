from setuptools import find_packages,setup
from typing import List

HYPHON_E_DOT = "-e ."

def get_requirements(filepath:str)->List[str]:      #filepath can be any file or folder
    requirements=[]

    with open(filepath) as file_obj:
        requirements=file_obj.readlines()
        requirements=[i.replace("\n","") for i in requirements]

        if HYPHON_E_DOT in requirements:
            requirements.remove(HYPHON_E_DOT)


setup(name='Salary-Prediction-End-To-End-ML-Project-With-Deployment',
      version='0.0.1',
      description='machine learning:end to end project',
      author='Priyanka Yadav',
      author_email='priyankadsyadav2@gmail.com',
      packages=find_packages(),
      install_requires = get_requirements("requirements.txt")
      
)


#!/usr/bin/env python

#from distutils.core import setup
import os
from setuptools import setup
# from pip.req import parse_requirements

# This method of pulling in req.txt is deprecated: https://github.com/pypa/pip/issues/2286#issuecomment-68285791
# parse_requirements() returns generator of pip.req.InstallRequirement objects
# install_reqs = parse_requirements('requirements.txt', session=False)
# reqs = [str(ir.req) for ir in install_reqs]

packages = [(root, [os.path.join(root, f) for f in files])
    for root, dirs, files in os.walk('packages')]

setup(name='pvdm',
      version='0.0.1',
      description='Paragraph vector distributed memory',
      author='Brian Lee Yung Rowe',
      author_email='rowe@zatonovo.com',
      url='http://www.pez.ai',
      packages=['pez'],
      include_package_data=True,
      data_files=packages,
      scripts=['bin/train','bin/predict'],
      install_requires=[
        'numpy==1.12.0b1',
        'scipy==0.18.1',
        'gensim',
      ]
     )

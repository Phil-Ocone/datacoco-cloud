import os
import re
from setuptools import setup, find_packages


def get_version():
    version_file = open(os.path.join("datacoco_cloud", "__version__.py"))
    version_contents = version_file.read()
    return re.search('__version__ = "(.*?)"', version_contents).group(1)


setup(
    name="datacoco-cloud",
    packages=find_packages(exclude=["tests*"]),
    version=get_version(),
    license="MIT",
    description="common code for AWS Cloud Services",
    long_description=open("README.rst").read(),
    author="Equinox Fitness",
    url="https://github.com/equinoxfitness/datacoco-cloud",
    install_requires=[
      'requests==2.20.0',
      'gevent==1.3.7',
      'boto3==1.9.203'
    ],
)


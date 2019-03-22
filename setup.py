from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='mypackage',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='git@github.com:Caylin911/mypackage.git',
    author='Caylin Gabriel',
    author_email='caylingab@gmail.com'
)

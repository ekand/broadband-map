from setuptools import find_packages, setup

setup(
    name='src',
    packages=find_packages(),
    version='0.1.0',
    description='a project to analyze broadband internet acces in the US',
    author='Erik Kristofer Anderson',
    license='MIT', install_requires=['pandas', 'numpy']
)

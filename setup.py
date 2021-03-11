from setuptools import setup


setup(
    name='ApplyTimezone',
    url='https://github.com/Mahrkeenerh/ApplyTimezone',
    author='Samuel Buban',
    author_email='samuelbuban@gmail.com',
    packages=['applyTimezone'],
    install_requires=['dateutil'],
    version='1.0',
    license='MIT',
    description='A package to convert to UTC time',
    long_description=open('README.md').read()
)

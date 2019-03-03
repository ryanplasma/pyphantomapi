from setuptools import setup

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pyphantomapi',
    version='0.1.3',
    description='Python Wrapper for the Splunk Phantom API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ryanplasma/pyphantomapi',
    download_url='https://github.com/ryanplasma/pyphantomapi/archive/0.1.3.tar.gz',    author='Ryan Plas',
    author_email='ryan@wordplas.com',
    license='MIT',
    packages=['pyphantomapi'],
    install_requires=[
        'requests'
    ]
)

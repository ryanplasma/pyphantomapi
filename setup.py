from setuptools import setup

setup(
    name='pyphantomapi',
    version='0.1',
    description='Python Wrapper for the Splunk Phantom API',
    url='https://github.com/ryanplasma/pyphantomapi',
    author='Ryan Plas',
    license='MIT',
    packages=['pyphantomapi'],
    install_requires=[
        'requests'
    ]
)

from setuptools import setup

setup(
    name='pyphantomapi',
    version='0.1.2',
    description='Python Wrapper for the Splunk Phantom API',
    url='https://github.com/ryanplasma/pyphantomapi',
    download_url='https://github.com/ryanplasma/pyphantomapi/archive/0.1.2.tar.gz',    author='Ryan Plas',
    author_email='ryan@wordplas.com',
    license='MIT',
    packages=['pyphantomapi'],
    install_requires=[
        'requests'
    ]
)

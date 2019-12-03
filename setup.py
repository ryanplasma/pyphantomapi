from setuptools import setup


def readme():
    """print long description"""
    with open('README.md') as f:
        return f.read()


setup(
    name='pyphantomapi',
    version='0.2.0',
    description='Python Wrapper for the Splunk Phantom API',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/ryanplasma/pyphantomapi',
    download_url='https://github.com/ryanplasma/pyphantomapi/archive/0.1.4.tar.gz',
    author='Ryan Plas',
    author_email='ryan@wordplas.com',
    license='MIT',
    packages=['pyphantomapi'],
    install_requires=['requests'])

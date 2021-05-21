from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='python-tools',
    url='https://github.com/noorzeea/python-tools',
    author='Davide Nurzia',
    author_email='davide.nurzia@gmail.com',
    # Needed to actually package something
    packages=['python-tools'],
    # Needed for dependencies
    install_requires=['datetime'],
    # *strongly* suggested for sharing
    version='0.0.1',
    # The license can be anything you like
    license='MIT',
    description='Package with various tools for various things',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)
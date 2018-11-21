"""
setup.py
"""

from setuptools import setup, Extension


setup(name='mypackage',
      version='0.0.1',
      description='Python Distribution Utilities',
      author='Sabry Moustafa',
      author_email='sabrygad@buffalo.edu',
      packages=['mypackage'],
      scripts=['scripts/mypackage'],
      )


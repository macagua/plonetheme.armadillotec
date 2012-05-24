# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='plonetheme.armadillotec',
      version=version,
      description='An installable Diazo theme for Plone 4.1',
      long_description=open('README.rst', 'rb').read()+'\n'+
                       open(os.path.join("docs", "INSTALL.txt")).read()+'\n'+
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        'Framework :: Plone',
        'Framework :: Plone :: 4.1',
        'Framework :: Zope2',
        'Framework :: Zope3',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        ],
      keywords='web zope plone diazo theme armadillotec cms',
      author='Leonardo J. Caballero G.',
      author_email='leonardocaballero@gmail.com',
      url='https://github.com/macagua/plonetheme.armadillotec',
      license='GPL',
      packages=find_packages(),
      namespace_packages=['plonetheme'],
      include_package_data=True,
      install_requires=[
          'setuptools',
          'plone.app.theming',
      ],
      entry_points={
          'z3c.autoinclude.plugin': 'target = plone',
      }
)

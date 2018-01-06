# -*- coding: utf-8
from setuptools import setup

setup(
        name='robots-txt-cli',
        author='ques0942',
        url='https://github.com/ques0942/robots-txt-cli',
        description='command line tool for robots.txt',
        license='MIT',
        py_modules=['robotstxt', ],
        scripts=['robotstxt.py', ],
        install_requires=['fire', ],
        entry_points={
            'console_scripts': ['robots-txt-cli=robotstxt:main', ],
            },
        )


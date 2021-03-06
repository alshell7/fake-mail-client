# -*- coding: utf-8 -*-

import sys
import os

from setuptools import setup, find_packages
from fake_mail_client import version

CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))

def get_readme():
    readme_path = os.path.abspath(os.path.join(CURRENT_DIR, 'README.rst'))
    if os.path.exists(readme_path):
        with open(readme_path) as fp:
            return fp.read()
    return ""


extra_opts = {"packages": find_packages(exclude=["tests", "tests.*"])}
if "test" in sys.argv or "nosetests" in sys.argv:
    extra_opts['packages'] = find_packages()

setup(
    name='fake-mail-client',
    version=version.version_str(),
    url='https://github.com/srault95/fake-mail-client', 
    description='Mail Tools for SMTP load testing',
    long_description=get_readme(),
    author='Stéphane RAULT',
    license='BSD',
    author_email='stephane.rault@radicalspam.org',
    keywords=['testing', 'mail', 'smtp'],
    classifiers=[
        'Topic :: Communications :: Email',
        'Development Status :: 4 - Beta',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'License :: OSI Approved :: BSD License',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators'
    ],
    include_package_data=True,
    zip_safe=False,
    use_2to3=True,
    install_requires=[
        'Faker>=0.7.0',
        'arrow',
        'click',
        'PyYAML',
        'tablib'
    ],
    extras_require = {
        'gevent': ['gevent>=1.0'],
    },
    entry_points={
      'console_scripts': [
        'fake-mailer = fake_mail_client.runner:main',
      ],
    },
    tests_require=[
        'nose>=1.0',
        'coverage>=3.7.1',
        'flake8'
    ],      
    test_suite='nose.collector',
    **extra_opts
)

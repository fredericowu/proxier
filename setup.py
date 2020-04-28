#!/usr/bin/env python
import os
import sys
from codecs import open
from setuptools import setup
from setuptools.command.test import test as TestCommand

here = os.path.abspath(os.path.dirname(__file__))


class PyTest(TestCommand):
    def run_tests(self):
        import pytest

        errno = pytest.main(["-n", "1"])
        sys.exit(errno)


packages = ['proxier']

requires = [
    'requests>=2.23.0',
    'wheel',
]

test_requirements = [
    'pytest-httpbin==0.0.7',
    'pytest-cov',
    'pytest-mock',
    'pytest-xdist',
    'pytest>=3',
    'requests_mock',
]

about = {}
with open(os.path.join(here, 'proxier', '__version__.py'), 'r', 'utf-8') as f:
    exec(f.read(), about)

with open('README.md', 'r', 'utf-8') as f:
    readme = f.read()
with open('HISTORY.md', 'r', 'utf-8') as f:
    history = f.read()

setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__description__'],
    long_description=readme,
    long_description_content_type='text/markdown',
    author=about['__author__'],
    author_email=about['__author_email__'],
    url=about['__url__'],
    packages=packages,
    package_dir={'proxier': 'proxier'},
    include_package_data=True,
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*",
    install_requires=requires,
    license=about['__license__'],
    zip_safe=False,
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ],
    cmdclass={'test': PyTest},
    tests_require=test_requirements,
    project_urls={
        'Documentation': 'http://proxier.readthedocs.io',
        'Source': 'https://github.com/fredericowu/proxier',
    },
)

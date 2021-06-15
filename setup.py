# -*- coding: utf-8 -*-

"""
setuptools module for project.

python setup.py install
"""

# pylint: disable=line-too-long

import setuptools

setuptools.setup(
    name="shotlast",
    version="0.1.1",
    url="https://github.com/caglartoklu/shotlast",

    author="Caglar Toklu",
    author_email="caglartoklu@gmail.com",

    description="Watches clipboard and automatically saves any new images/text/files.",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=[
        "colorama",
        "click",
        "Pillow",
        "PySimpleGUI",
    ],

    # https://pypi.org/classifiers/
    classifiers=[
        'Development Status :: 4 - Beta',
        # 'Framework :: PIL',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # 'Programming Language :: Python :: 3.4', pathlib requires 3.5
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],

    entry_points={
        'console_scripts': ['shotlast=shotlast:main'],
    },

    # test_suite='nose2.collector.collector',
    # tests_require=['nose2'],

    include_package_data=True,
    zip_safe=False,
)

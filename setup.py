#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='pylfu',
    version='0.1.1',
    author='fengyun',
    author_email='rfyiamcool@163.com',
    packages=find_packages(),
    url='https://github.com/rfyiamcool',
    description='python Lfu cache service ',
    long_description=open('README.rst').read(),
    install_requires=['IPy==0.81'],
    license='MIT'
)

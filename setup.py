#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

description = """
PostgreSQL json field support for Django.
"""

setup(
    name="django-pgjson",
    version="0.4.0",
    url="https://github.com/djangonauts/django-pgjson",
    license="BSD",
    platforms=["OS Independent"],
    description=description.strip(),
    author="Andrey Antukh",
    author_email="niwi@niwi.be",
    keywords="django, postgresql, pgsql, json, field",
    maintainer="Andrey Antukh",
    maintainer_email="niwi@niwi.be",
    packages=find_packages(),
    include_package_data=False,
    install_requires=[
        "Django>=5.2,<5.3",
        "psycopg2-binary>=2.9.0",
    ],
    python_requires=">=3.10",
    zip_safe=False,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Framework :: Django",
        "Framework :: Django :: 5.2",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Internet :: WWW/HTTP",
    ]
)

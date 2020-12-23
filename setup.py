#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages
from variant_intersections import __version__

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = ['pandas', 'upsetplot', 'matplotlib', 'plotly']

test_requirements = ['pytest>=3', ]

setup(
    author="Finlay Maguire",
    author_email='finlaymaguire@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    description="Script to generate interactive plots of the intersections "
                "of detected variants",
    entry_points={
        'console_scripts': [
            'var_intersect_plot=variant_intersections.cli:main',
        ],
    },
    install_requires=requirements,
    license="GNU General Public License v3",
    include_package_data=True,
    keywords='variant_intersections',
    name='variant_intersections',
    packages=find_packages(include=['variant_intersections']),
    setup_requires=requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/fmaguire/variant_intersections',
    version=__version__,
    zip_safe=False,
)

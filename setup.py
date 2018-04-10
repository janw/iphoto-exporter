"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    requirements = f.read().splitlines()

setup(
    name='iphoto_exporter',
    version='0.0.3',
    description='Simple exporter for master images from iPhoto Libraries',

    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',

    url='https://github.com/janwh/iphoto-exporter',
    author='Jan Willhaus',
    author_email='mail@janwillhaus.de',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: System Administrators',
        'Operating System :: MacOS :: MacOS X',
        'Topic :: System :: Recovery Tools',

        # Pick your license as you wish
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='iphoto photos.app exporter',  # Optional

    py_modules=["iphoto_exporter"],
    python_requires='>=3',
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'iphoto_exporter = iphoto_exporter:main',
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/janwh/iphoto-exporter/issues',
        'Funding': 'https://liberapay.com/janw',
        'Say Thanks!': 'https://saythanks.io/to/janwh',
        'Source': 'https://github.com/janwh/iphoto-exporter/',
    },
)
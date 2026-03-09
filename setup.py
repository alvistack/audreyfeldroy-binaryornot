from setuptools import setup

setup(
    name='binaryornot',
    version='0.6.0',
    description='Ultra-lightweight pure Python package to check if a file is binary or text.',
    author_email='Audrey Roy Greenfeld <aroy@alum.mit.edu>',
    maintainer_email='Audrey Roy Greenfeld <aroy@alum.mit.edu>',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: 3.14',
        'Typing :: Typed',
    ],
    entry_points={
        'console_scripts': [
            'binaryornot = binaryornot.check:main',
        ],
    },
    packages=[
        'binaryornot',
        'binaryornot.data',
    ],
    package_dir={'': 'src'},
)

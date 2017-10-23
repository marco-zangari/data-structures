"""Setup module for data-structures package."""
from setuptools import setup

setup(
    name='data-structures',
    description='A package for python data structures.',
    package_dir={'': 'src'},
    author=['Marco Zangari', 'Gabriel Meringolo'],
    author_email=['', 'gabriel.meringolo@gmail.com'],
    py_modules=[''],
    install_requires=[],
    extras_require={
        'testing': ['pytest', 'pytest-cov', 'pytest-watch', 'tox'],
        'development': ['ipython']
    },
    entry_points={
        'console_scripts': [
        ]
    }
)

from setuptools import setup, find_packages

setup(
    name = 'flasktrack',
    version = '1.0.0',
    author = 'stupidcomputer',
    author_email = 'ryan@beepboop.systems',
    url = 'https://git.beepboop.systems/stupidcomputer/flasktrack',
    description = 'simple phonetracking thing',
    license = 'GPLv3',
    packages=["flasktrack"],
    classifiers = (
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux",
    ),
    zip_safe = False
)

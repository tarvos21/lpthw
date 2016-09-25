try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
        'discription': 'My Project',
        'author': 'DuBing',
        'url': 'www.dubing.com',
        'download_url': 'www.dubing.com/download',
        'author_email': 'tarvos21@live.com',
        'version': '1.0',
        'install_requires': ['nose'],
        'packages': ['NAME'],
        'scripts': [],
        'name': 'DuBing Project'
        }

setup(**config)

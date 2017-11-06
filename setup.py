from distutils.core import setup

with open('README.md','r') as long_desc:
    README = long_desc.read()

with open("requirements.txt", "r") as reqs:
    requirements = reqs.readlines()

setup(
    name = 'hackinguis',
    version = '0.0.1',
    url = 'https://github.com/mondeja/hackinguis',
    download_url = 'https://github.com/mondeja/hackinguis/archive/master.zip',
    author = 'Álvaro Mondéjar <mondejar1994@gmail.com>',
    author_email = 'mondejar1994@gmail.com',
    license = 'BSD License',
    packages = ['human_mouse'],
    description = 'Library to perform human-like GUI inputs.',
    long_description = README,
    keywords = ['human', 'mouse', 'gui'],
    install_requires = requirements,
    
)
from distutils.core import setup

with open('README.md','r') as long_desc:
    README = long_desc.read()

with open("requirements.txt", "r") as reqs:
    requirements = reqs.readlines()

setup(
    name = 'human_mouse',
    version = '0.0.1',
    url = 'https://github.com/mondeja/human_mouse',
    download_url = 'https://github.com/mondeja/human_mouse/archive/master.zip',
    author = 'Álvaro Mondéjar <mondejar1994@gmail.com>',
    author_email = 'mondejar1994@gmail.com',
    license = 'BSD License',
    packages = ['human_mouse'],
    description = 'Library to perform human mouse inputs.',
    long_description = README,
    keywords = ['human', 'mouse'],
    install_requires = requirements,
    
)
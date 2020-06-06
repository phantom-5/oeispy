from setuptools import setup,find_packages

classifiers=['Development Status :: Alpha',
             'Intended Auidence :: Education',
             'Operating System :: Microsoft :: Windows :: Windows 10',
             'License :: OSI Approved :: MIT License',
             'Programming Language :: python :: 3']

setup(
    name='oeispy',
    version='0.0.1',
    description='Simple Python Library for OEIS',
    Long_description=open('README.md').read()+'\n\n'+open('CHANGELOG.txt').read(),
    url='https://github.com/phantom-5/oeispy',
    author='Rudra M Biswal',
    author_email='rickrudra@gmail.com',
    License='MIT',
    classifiers=classifiers,
    keywords='oeis',
    packages=find_packages(),
    intall_requires=['requests']


)
import pele_platform
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
ext_modules = []
cmdclass = {}
# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
     long_description = f.read()

setup(
    name="pele_platform",
    version=pele_platform.__version__,
    description='Automatic platform to launch PELE',
    long_description=long_description,
    url="https://github.com/NostrumBioDiscovery/pele_platform",
    author='Daniel Soler',
    author_email='daniel.soler@nostrumbiodiscovery.com',
    packages=find_packages(exclude=['docs', 'tests', 'tests.data']),
    package_data={"pele_platform/AdaptivePELE/atomset": ['*.pxd'], "pele_platform/AdaptivePELE/freeEnergies/": ['*.pyx']},
    include_package_data=True,
    install_requires=["AdaptivePELE", "frag_pele>=2.1.1", "lib_prep", "PPPele==1.0.4", "PlopRotTemp==1.0.1", "PyYAML", "fpdf", "scikit-learn>0.2", "pillow", "scipy", "matplotlib", 
       "biopython", "pandas", "pytest", "cython", "numpy"],    
    cmdclass=cmdclass,
    ext_modules=ext_modules  # accepts a glob pattern
)

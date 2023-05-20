from setuptools import setup, find_packages


# Setting __version__
__version__ = '0.0.0'

# Parsing requirements
with open('requirements.txt', 'r') as f:
    requirements = f.readlines()

setup(
    name='pulltube',
    version=__version__,
    description='Terminal based application to download YouTube videos',
    long_description=open('README.md').read(),
    author='Aavache',
    author_email='aaron.valero@outlook.com',
    entry_points={
        'console_scripts': [
            'pulltube = src.cli:cli',
        ],
    },
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.5.0',
    setup_requires=['wheel']
)

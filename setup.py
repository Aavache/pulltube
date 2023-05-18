from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

# setting __version__
__version__ = '0.0.0'
with open('terminal/__init__.py') as f:
    exec(f.readline().strip())

# Parsing requirements
with open('requirements.txt', 'r') as f:
    requirements = f.readlines()

setup(
    name='pulltube',
    version=__version__,
    description='Terminal based application to download YouTube videos',
    long_description=long_description,
    author='Aavache',
    author_email='aaron.valero@outlook.com',
    packages=find_packages(include=['terminal', 'cli.*']) + ['incl'],
    package_dir={'incl': 'sdk'},
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'incl = cli.cli:cli',
        ],
    },
    install_requires=requirements,
    python_requires='>=3.5.0',
    setup_requires=['wheel']
)

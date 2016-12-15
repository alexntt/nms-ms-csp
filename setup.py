from setuptools import setup, find_packages

setup(
    name='nms-ms-csp',
    version='0.0.1',
    description='Library to access Microsoft Customer Support Portal',
    packages=find_packages(),
    install_requires=['requests'],
    extras_require={
        'dev': ['ipython', 'ipdb'],
    },
)


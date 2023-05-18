from setuptools import setup

setup(
    name='crewco_api',
    version='0.1',
    packages=['crewco_api'],
    entry_points={
        'console_scripts': [
            'myapi = crewco_api.main:main'
        ]
    },
)

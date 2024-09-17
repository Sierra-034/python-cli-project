from setuptools import setup

setup(
    name='yourscript',
    version='0.1.0',
    py_modules=['my_module'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'cli = my_module:hello',
        ],
    },
)
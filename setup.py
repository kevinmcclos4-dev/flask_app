from setuptools import setup, find_packages

setup(
    name="flask_app",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'flask==3.0.2',
        'pytest==8.0.2',
        'pytest-flask==1.3.0',
        'pytest-cov==4.1.0',
        'gunicorn==21.2.0',
    ],
) 
from setuptools import find_packages, setup

setup(
    name='orango',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    description='A Python SDK for the Orango API',
    author='Orango AI',
    author_email='hello@orango.ai',
    url='https://github.com/Orango-AI/orango-py',  # Update with your repo URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

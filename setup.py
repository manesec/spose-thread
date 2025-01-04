from setuptools import setup, find_packages

def read_requirements(file_path):
    with open(file_path, 'r') as f:
        return [line.strip() for line in f if line and not line.startswith('#')]

setup(
    name='spose', 
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'spose=src.spose:main_function', 
        ],
    },
    install_requires=read_requirements('requirements.txt'),
    python_requires='>=3.6', 
    author='aancw mod by manesec', 
    author_email='mane@manesec.com',  
    description='Squid Pivoting Open Port Scanner',
    long_description=open('README.md').read(),  
    long_description_content_type='text/markdown', 
    url='https://github.com/manesec/spose-thread',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)

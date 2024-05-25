from setuptools import setup, find_packages

setup(
    name='foldertemplate',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click',
        'cookiecutter'
    ],
    entry_points='''
        [console_scripts]
        foldertemplate=foldertemplate.cli:generate
    ''',
    author='Your Name',
    author_email='your.email@example.com',
    description='A Python package to generate prefixed hierarchical folder structures.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/foldertemplate',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

from setuptools import setup, find_packages

setup(
    name='dataengx',
    version='0.1.0',
    description='Data engineering tools for CSV, Parquet, JSONL conversions with CLI.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Samuel Mana-ay',
    author_email='manaaysamuel@gmail.com',
    url='https://github.com/yourusername/dataengx',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'pyarrow',
        'duckdb'
    ],
    entry_points={
        'console_scripts': [
            'dataengx=cli.main:main'
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)

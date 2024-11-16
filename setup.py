from setuptools import setup, find_packages

# Read dependencies from requirements.txt
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="cryptopulse",
    version="0.1",
    description="CryptoPulse: A model for cryptocurrency next-day price forecasting using market sentiments and macroeconomic data",
    author="Amit Kumar, Dr. Taoran Ji",
    author_email="akumar3@islander.tamucc.edu, taoran.ji@tamucc.edu",
    url="https://github.com/Sequential-Analytics-Lab/SAL-CryptoPulse.git",
    packages=find_packages(),
    install_requires=requirements,  # Load dependencies from requirements.txt
    entry_points={
        'console_scripts': [
            'cryptopulse=cryptopulse.main:main',  # Single run
            'cryptopulse_batch=cryptopulse.batch_processor:batch_process',  # Batch processing
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

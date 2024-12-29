from setuptools import setup, find_packages

setup(
    name="ft_package",
    version="0.0.1",
    description="A sample test package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/eagle/ft_package",
    author="eagle",
    author_email="eagle@42.fr",
    license="MIT",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.6",
)

from setuptools import setup, find_packages
import os
import simple_cache_admin

def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ""

setup(
    name="django-simple-cache-admin",
    version=simple_cache_admin.__version__,
    author="kf",
    author_email="7kfpun@gmail.com",
    url="https://github.com/7kfpun/django-simple-cache-admin",
    license="MIT",
    description=" ".join(simple_cache_admin.__doc__.splitlines()).strip(),
    long_description=read("README.md"),
    install_requires=[
        "Django>=1.6",
    ],
    packages=find_packages(exclude=['*.tests', '*.tests.*']),
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Internet :: WWW/HTTP :: Site Management",
    ],
)

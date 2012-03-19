from setuptools import setup, find_packages
from statsdpy import __version__ as version

install_requires = []
try:
    import eventlet
except ImportError:
    install_requires.append("eventlet")
try:
    import json
except ImportError:
    install_requires.append("simplejson")
try:
    import tempodb
except ImportError:
    install_requires.append("tempodb")

name = "statsdpy"

setup(
    name=name,
    version=version,
    author="Florian Hines",
    author_email="syn@ronin.io",
    description="statsdpy",
    license="Apache License, (2.0)",
    keywords="statsd",
    url="http://github.com/pandemicsyn/statsdpy",
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.6',
        'Environment :: No Input/Output (Daemon)',
        ],
    install_requires=install_requires,
    scripts=['bin/statsdpy-server']
    )

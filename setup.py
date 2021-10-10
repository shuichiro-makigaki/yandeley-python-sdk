from setuptools import setup

__version__ = None
with open('yandeley/version.py') as f:
    exec(f.read())

setup(
    name='yandeley',
    version=__version__,
    packages=['yandeley', 'yandeley.models', 'yandeley.resources'],
    url='http://dev.mendeley.com',
    license='Apache',
    author='Mendeley',
    author_email='api@mendeley.com',
    description='Python SDK for the Mendeley API',

    install_requires=[
        'arrow==0.5.0',
        'future==0.14.3',
        'memoized-property==1.0.2',
        'requests==2.5.1',
        'requests-oauthlib==0.4.2',
        'oauthlib==0.7.2'
    ],

    tests_require=[
        'pytest==2.6.4',
        'vcrpy==1.2.0'
    ],

    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ]
)

from distutils.core import setup

setup(
    name='checklib',
    packages=['checklib'],
    package_data={
        'checklib': ['resources/*']
    },
    version='0.5.1',
    license='MIT',
    description='Library for convenient checker writing',
    author='Roman Nikitin',
    author_email='nikrom.prog@gmail.com',
    url='https://github.com/pomo-mondreganto/',
    download_url='https://github.com/pomo-mondreganto/checklib/archive/v_0.5.1.tar.gz',
    keywords=['AD', 'CTF', 'checker'],
    install_requires=[
        'requests',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)

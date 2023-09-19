from distutils.core import setup

setup(
    name="checklib",
    packages=["checklib"],
    package_data={"checklib": ["resources/*"]},
    version="0.7.0",
    license="MIT",
    description="Library for convenient checker writing",
    author="Roman Nikitin",
    author_email="nikrom.prog@gmail.com",
    url="https://github.com/pomo-mondreganto/",
    download_url="https://github.com/pomo-mondreganto/checklib/archive/v_0.7.0.tar.gz",
    keywords=["AD", "CTF", "checker"],
    install_requires=[
        "requests",
        "portalocker",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)

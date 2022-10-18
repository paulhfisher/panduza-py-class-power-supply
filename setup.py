from setuptools import setup, find_packages
from setuptools.command.install import install

VERSION = '0.0.1'
DESCRIPTION = 'Panduza Python MetaDrivers for Power Supplies'
LONG_DESCRIPTION = 'The Panduza '

class CustomInstallCommand(install):
    def run(self):
        install.run(self)

# Setting up
setup(
    name="panduza_drv_power_supply",
    version=VERSION,
    author="Panduza Team",
    author_email="panduza.team@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    cmdclass={'install': CustomInstallCommand},

    # install_requires=['panduza_platform', 'pyserial'],

    # keywords=['python', 'first package'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)

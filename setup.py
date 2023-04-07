from setuptools import find_packages, setup
setup(
    name='u8488a-driver4usrp-calibration',
    packages=find_packages(include=['u8488a']),
    version='0.1.0',
    description='Keysight U8488A Powermeter Driver for USRP Power Calibration',
    author='Anil Gurses',
    author_email='agurses@ncsu.edu',
    license='MIT',
    install_requires=[],
    setup_requires=['pyvisa', 'pyusb', 'pyserial'],
)
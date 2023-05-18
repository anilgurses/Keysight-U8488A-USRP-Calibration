from setuptools import find_packages, setup
setup(
    name='u8488a',
    packages=find_packages(),
    version='0.1.0',
    description='Keysight U8488A Powermeter Driver for USRP Power Calibration',
    author='Anıl Gürses',
    author_email='agurses@ncsu.edu',
    license='MIT',
    install_requires=[],
    setup_requires=['pyvisa', 'pyvisa-py', 'pyusb', 'pyserial'],
)

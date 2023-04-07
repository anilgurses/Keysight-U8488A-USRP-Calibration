## USRP Calibrator Driver for Keysight U8488A 

Custom driver for USRP calibration. `uhd_power_cal.py` scripts is installed with UHD installation. Instruction is given below,

```
$ cd /usr/local/lib/uhd/utils/
$ uhd_power_cal.py --meas-dev visa -o import=u8488a
```

Note: Waveform generation is not implemented since U8488A is a power meter. 


Contact: <agurses[at]ncsu.edu>


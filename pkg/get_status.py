"""
get_status.py : get interface status
"""
__author__ = "Jerin Johns"
__contact__ = "L00187577@atu.ie"
__copyright__ = "Copyright $YEAR, JJ"
__date__ = "28NOV24"
__deprecated__ = False
__license__ = "GPLv3"
__status__ = "test"
__version__ = "1"

import telnetlib


def get_interface_status(tnob):
    #enable
    tnob.write(b"enable\n")
    # get data and Exit gracefully
    tnob.write(b"sh ip interface brief\n")
    tnob.write(b"exit\n")
    # save we got
    outswitch = (tnob.read_all().decode('ascii'))
    return outswitch


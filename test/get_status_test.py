"""
get_status_test.py : test get interface status
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


HOST = "192.168.1.21"
password = "jj"

tn = telnetlib.Telnet(HOST)
tn.read_until(b"Password: ")
tn.write(password.encode('ascii') + b"\n")


def get_interface_status(tnob):
    #enable
    tnob.write(b"enable\n")
    # get data and Exit gracefully
    tnob.write(b"sh ip interface brief\n")
    tnob.write(b"exit\n")
    # save we got
    outswitch = (tnob.read_all().decode('ascii'))
    return outswitch

output = get_interface_status(tn)

print (output)
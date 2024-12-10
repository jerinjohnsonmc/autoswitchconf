"""
connect.py : connect to switch via telnet
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
from mypaths import SWITCH_SETTINGS as switch_settings
import settings.switch as settings

def cnct():
    tn = telnetlib.Telnet(settings.HOST["SWITCH_IPv4"])
    tn.read_until(b"Password: ")
    tn.write(settings.HOST["TELNET_PASS"].encode('ascii') + b"\n")
    return tn
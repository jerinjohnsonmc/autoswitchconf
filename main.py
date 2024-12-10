"""
main.py : main programme to get status of interfaces in a cisco switch, switch settings to be saved in /settings/switch.py
"""
__author__ = "Jerin Johns"
__contact__ = "L00187577@atu.ie"
__copyright__ = "Copyright $YEAR, JJ"
__date__ = "28NOV24"
__deprecated__ = False
__license__ = "GPLv3"
__status__ = "test"
__version__ = "1"

import pkg.connect as swcnct
import pkg.get_status as get_sts
import pkg.parse_status as prse


#connects switch
tn = swcnct.cnct()

#gets names and status of interfaces

out_switch = get_sts.get_interface_status(tn)


# parse output of switch for relevant data
interfaces = prse.parse_interface_status(out_switch)

#print output
for interface, status in interfaces:
    print (f"Interface: {interface}, Status: {status}")






"""
parse_status.py : parse interface status
"""
__author__ = "Jerin Johns"
__contact__ = "L00187577@atu.ie"
__copyright__ = "Copyright $YEAR, JJ"
__date__ = "28NOV24"
__deprecated__ = False
__license__ = "GPLv3"
__status__ = "test"
__version__ = "1"

def parse_interface_status(output):
    # Split the output into lines
    lines = output.strip().splitlines()

    interface_data = []
    start_parsing = False

    for line in lines:
        # check if line starts with sh ip interface brief and start parsing
        if line.startswith("Switch21>sh ip interface brief") and not start_parsing:
            start_parsing = True
            continue  
            
        if line.startswith("Switch21>exit"):
            break
        # Once parsing starts, process the remaining lines
        if start_parsing:
            #split lines in to columns
            columns = line.split()
            #extract interface (1st column) and status (5th column)
            
            interface = columns[0]
            
            status = columns[4]
            interface_data.append((interface, status))

    return interface_data

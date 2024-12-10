"""
mypaths.py : path variables
"""
__author__ = "Jerin Johns"
__contact__ = "L00187577@atu.ie"
__copyright__ = "Copyright $YEAR, JJ"
__date__ = "28NOV24"
__deprecated__ = False
__license__ = "GPLv3"
__status__ = "test"
__version__ = "1"

from pathlib import Path

PROJECT_ROOT = Path(__file__).parent
SWITCH_SETTINGS = str(PROJECT_ROOT / "settings/switch.py")
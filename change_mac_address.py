###############
# Udemy Security Testing with Python
###############

https://github.com/rocket7/pysec.git

###############################################
# IMPORT MODULES
###############################################
import re
import subprocess
import optparse
import os
import platform


###############################################
# DEFINE VARIABLES
###############################################
# DEFAULTS - iMac
interface = "p2p0"
#interface = ""
#orig_mac_addr = "0a:30:62:5d:be:f2"
new_mac_addr = "" # = "00:11:22:33:44:55"
#new_mac_addr = ""
#verify_new_mac = ""


################################################
# VERIFY OS TYPE IS LINUX
################################################
def check_os():
    if platform.system() == 'Linux' || 'Darwin':
        return True
    else:
        return False





################################################
# DEFINE CHANGE_MAC FUNCTION WITH TWO PARAMETERS
################################################
def change_mac(interface, new_mac_addr):
    # SECURITY ISSUE USING SHELL=TRUE
    # subprocess.call("ifconfig down", shell=True)

    #BETTER WAY TO RUN SUBPROCESS WITH LIST
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw ether", new_mac_addr])
    subprocess.call(["ifconfig", interface, "up"])

    print("[+] Changing interface for " + interface + " to " + new_mac_addr)


################################################
# VERIFY MAC CHANGED
################################################
def get_current_mac(interface, new_mac_addr):
    # SECURITY ISSUE USING SHELL=TRUE
    # subprocess.run("ifconfig down", shell=True)
    #BETTER WAY TO RUN SUBPROCESS WITH LIST
    #CHECK_OUTPUT RETURNS STRING
    ifconfig_result = subprocess.getoutput("ifconfig " + interface)
    ifconfig_result2 = subprocess.check_output(["ifconfig", interface]) # Returns NONE TYPE type if nothing captured - USE str(aaa) to cast to STRING

    #regx2 = re.compile('\w\w:\w\w:\w\w:\w\w:\w\w:\w\w')
    mac_address_search_result = re.search(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w', ifconfig_result)
    if new_mac_addr == mac_address_search_result.group(0):
        print("[+] MAC Address changed successfully")
    else:
        print("[-] MAC Address change could not be verified")
    print("[+] Verified interface for " + interface + " is changed to " + new_mac_addr)

###############################################
# CMD LINE PARSER FUNCTION
###############################################
def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="interface to change mac")
    parser.add_option("-m", "--mac", dest="new_mac_addr", help="set new mac address")
    #interface = options.interface
    #new_mac_addr = options.new_mac_addr
    #return parser.parse_args()

    (options, arguments) = parser.parse_args()
    if parser.parse_args().count() != 2:
        parser.error("[-] Missing all the required arguments")
    elif not options.interface:
        parser.error("[-] Please specify an interface using -i")
    else:
        parser.error("[-] Please specify a mac address using -m")
    return options


#Commented because not using command line
#options = get_arguments()

####################################################
# Validation - PYTHEX.ORG
####################################################

valid_interfaces = ("en0", "en1", "p2p0")

#REGEX TO TEST FOR VALID MAC ADDRESS -\w\w:\w\w:\w\w:\w\w:\w\w:\w\w
regx = re.compile('[0-9A-F][0-9A-F]:[0-9A-F][0-9A-F]:[0-9A-F][0-9A-F]:[0-9A-F][0-9A-F]:[0-9A-F][0-9A-F]:[0-9A-F][0-9A-F]')



####################################################
# USER INPUT
####################################################
# ASK FOR USER INPUT (RAW_INPUT FOR PYTHON 2)
def prompt_interface():
    valid_interface = False
    while valid_interface == False:
        interface = input("Enter interface > ")
        if interface in valid_interfaces:
            valid_interface = True
            break
        else:
            valid_interface = False
            print("Invalid interface")

def prompt_mac():
    valid_mac = False
    while valid_mac == False:
        new_mac_addr = input("Enter new MAC address > ")
        if regx.match(new_mac_addr):
            #print("valid regex - break loop")
            valid_mac = True
            break
        else:
            valid_mac = False
            print("Invalid MAC address")


####################################################
# CALL CHANGE MAC FUNCTION
####################################################

#change_mac(interface, new_mac_addr)

if check_os() == True:
    get_current_mac(interface, new_mac_addr)



#subprocess.call("ls;pwd", shell=True)

#ether_raw  = "ifconfig p2p ether|grep ether"

# CMD FORWARDSLASH to Add COMMENT




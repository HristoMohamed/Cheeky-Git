from email.MIMEText import MIMEText
from subprocess import Popen, PIPE
import re
import math
import os
import smtplib
from Daemon import Daemon
import scapy


class ValidWiFiMachine():

    WIRELESS_SYS = "/sys/class/net/"
    WPA_SUPPLICANT = "/var/run/wpa_supplicant.pid"
    has_interface = 0
    has_wpa_supplicant = 0
    installed_wireless_stack = 0
        
    def find_if_wireless_device_exists(self):
        all_network_devices = os.walk(WIRELESS_SYS).next()[1]
        for network_device in all_network_devices:
            if os.path.exists(WIRELESS_SYS+network_device+"\wireless"
                self.has_interface = 1
                return

    def search_for_wireless_interface(self):
        if os.path.exists(WIRELESS_SYS):
            self.has_interface = 1  

    def search_for_running_wpa_supplicant(self):
        if os.path.exists(WPA_SUPPLICANT):
            self.has_wpa_supplicant = 1

class TestWiFiConnection():
    
    WIRELESS_SYS = "/sys/class/net/"    
    

    wireless_interfaces = []
    interface_name = 0
    list_of_networks = 0
    number_of_wireless_devices = 0
    available_points = 0
    set_interface(self):
    
    def find_wireless_interfaces(self):
        all_network_devices = os.walk(WIRELESS_SYS).next()[1]
        for network_device in all_network_devices:
            if os.path.exists(WIRELESS_SYS+network_device+"\wireless"):
                self.wireless_interfaces.append(network_device)
                self.number_of_wireless_devices = self.number_of_wireless_devices +1
    
    def set_interface_name(self):
        self.interface_name = self.wireless_devices[self.number_of_wireless_devices]
        self.number_of_wireless_devices = self.number_of_wireless_devices -1    
    
    def prepare_wireless_device_for_monitoring_mode(self):
                
 
#    get_list_of_all_available_points(self):
         
         

#TODO think of a better name dammit
def main_function():
	#DOES STUFF?








class CheekyGitDaemon(Daemon):
    def run(self):
        while True:
            #daemon starter funcheck_quota()

if __name__ == "__main__":
    try:
        daemon = CheekyGitDaemon('/var/run/cheeky_git.pid')
    except:
        try:
            daemon = CheekyGitDaemon('/run/cheeky_git.pid')
        except:
            try:
                daemon = CheekyGitDaemon('/var/spool/cheeky_git.pid')
            except:
                print "Warning, creating daemon pid in /tmp/"
                daemon = CheekyGitDaemon('/tmp/cheeky_git.pid')
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            daemon.start()
        elif 'stop' == sys.argv[1]:
            daemon.stop()
        elif 'restart' == sys.argv[1]:
            daemon.restart()
        else:
            sys.exit(2)
        print "Unknown command"
        sys.exit(0)
    else:
        print "usage: %s start|stop|restart" % sys.argv[0]
        sys.exit(2)



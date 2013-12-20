from email.MIMEText import MIMEText
from subprocess import Popen, PIPE
import re
import math
import os
import smtplib
from Daemon import Daemon



#TODO think of a better name dammit
def main_function():
	#DOES STUFF?








class QuotaDaemon(Daemon):
    def run(self):
        while True:
            #daemon starter funcheck_quota()

if __name__ == "__main__":
    try:
        daemon = QuotaDaemon('/var/run/cheeky_git.pid')
    except:
        try:
            daemon = QuotaDaemon('/run/cheeky_git.pid')
        except:
            try:
                daemon = QuotaDaemon('/var/spool/cheeky_git.pid')
            except:
                print "Warning, creating daemon pid in /tmp/"
                daemon = QuotaDaemon('/tmp/cheeky_git.pid')
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



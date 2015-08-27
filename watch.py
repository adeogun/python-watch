import os
from os.path import getmtime
import optparse
import subprocess
import sys

def watch():
    'Gets save time of script'
    parser = optparse.OptionParser()
    parser.add_option('-f', '--file')
    options, args = parser.parse_args()
    watch_file = options.file
    last_update_time = getmtime(watch_file)
    
    while True:
    	'Check for change in save time, update save time and run script'
        try:
            '''problem on linux where deleting file causes file not found error temporarily.
             catch exception and continue'''
            if os.path.exists(watch_file) and  getmtime(watch_file) > last_update_time:
                last_update_time = getmtime(watch_file)
                subprocess.call(['python', watch_file])
        except:
            pass
			
if __name__ == '__main__':    
    watch()

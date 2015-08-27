import os
from os.path import getmtime
import optparse

def watch():
	'Gets save time of script'
	parser = optparse.OptionParser()
	parser.add_option('-f', '--file')
	options, args = parser.parse_args()
	watch_file = options.file	
	last_update_time = getmtime(watch_file)	
	
	while True:
		'Check for change in save time, update save time and run script'
		if getmtime(watch_file) > last_update_time:
			last_update_time = getmtime(watch_file)
			os.system(watch_file)
			
if __name__ == '__main__':    
	watch()
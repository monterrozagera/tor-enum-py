import tor_functions
import argparse
import requests
import time
import sys

def enumerate_directories(session, target, wordlist):
	url = target
	directories = wordlist
	tor_session = session
	# fix captcha issue, will attempt to inspect source code for better detection
	consecutive_connection = 0

	try:
		for dir in directories:
			try:
				dir_enum = f"https://{url}/{dir}"
				response = tor_session.get(dir_enum, headers=headers)

				# get how much completed through wordlist
				done = str(int(directories.index(dir) / list_length * 100))

				if response.ok:
					print("Found: ", dir_enum)
					consecutive_connection += 1

					if consecutive_connection > 5:
						print("[!] Captcha detected. \nRefreshing IP...")
						tor_functions.refresh_IP()
						consecutive_connection = 0

			except requests.exceptions.ConnectionError:
				print()
				print("[!] Banned IP")
				time.sleep(0.5)

				tor_functions.refresh_IP()
				print("Refreshing..")
				time.sleep(1)


			# print percentage done
			print(done[0:2], "% done.", end = "\r")
	except KeyboardInterrupt:
		print("Exiting.", end = "\r")
		sys.exit(0)

if __name__ == '__main__':
	banner = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣄⣤⣤⣤⠤⠤⠤⠤⢤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣋⣾⣿⣿⣿⣿⠿⡫⢈⠎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡿⢷⣿⣿⣿⣿⠟⣩⡞⡡⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⣺⡿⣭⣿⣿⡿⢋⣵⣾⠏⡔⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣾⣟⣾⣿⡿⢋⣴⣿⡿⢃⠎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣬⣾⣿⠯⣾⠟⣡⣾⣿⣿⡟⡡⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣔⣙⠿⢿⡑⢩⢥⣾⣿⣿⣿⠟⡐⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⡿⣍⠕⡃⣤⣿⣿⣿⡿⢃⠜⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⢟⠁⠁⢝⣮⣌⠌⠻⠿⣡⢮⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢴⡏⣼⣷⣯⣵⣂⠤⣀⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣾⣿⠟⣡⡾⢁⣿⣿⣿⣿⡷⢢⡜⠁⠀⠐⠏⠁⠁⠉⠂⡄⠀⠀⠀⢀⢔⣵⡟⣸⣿⣿⣿⣿⣿⣿⣷⣾⣥⢒⡤⠀⠀
⠀⠀⠀⠀⠀⣠⣿⠟⣡⣾⡿⢁⣾⣿⣿⣿⢟⠔⡏⢀⢀⢢⠀⠀⣀⡀⣠⣄⠪⡆⣀⣴⣵⣿⡿⢡⣿⣿⣿⣿⣿⣿⣿⠟⣋⡴⡱⠁⠀⠀
⠀⠀⠀⢀⡼⢟⣵⣿⣿⡿⢡⣾⣿⣿⢟⡵⠁⠀⢸⢾⣧⠀⠀⢦⢹⣻⣿⣬⠇⢿⣿⣿⣿⣿⢱⣿⣿⣿⣿⣿⡟⣋⣴⣾⡟⡔⠁⠀⠀⠀
⠀⠀⠠⢊⣴⣿⣿⣿⡿⢡⣿⣿⠟⡥⠋⠀⠀⠀⠈⢷⡝⡀⠀⣌⠰⠝⢟⣺⠷⠘⢿⣿⣿⠃⣼⣿⣿⠟⣋⣴⣾⣿⣿⠟⡜⠀⠀⠀⠀⠀
⠀⠀⢱⢻⣿⣿⣿⡿⢡⣿⠟⡥⠊⠀⠀⠀⠀⠀⠀⠈⠺⢂⡉⠈⠚⢉⠓⢁⡀⠌⠘⠯⡣⢱⠍⢋⣤⣾⣿⣿⣿⣿⢏⠜⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢏⣿⣿⡿⢡⡿⡣⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⡹⣽⣿⣷⣮⡖⡆⠄⢁⠠⢎⣿⣿⣿⣿⣿⣿⢏⠎⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠘⡟⡿⣡⡫⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣔⣿⣿⣿⣿⠟⣏⣻⢈⠨⣐⢌⡻⣿⣿⣿⣿⢃⠊⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠹⣀⠝⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢾⣾⣿⢿⢋⣥⣾⣿⠇⣴⣾⣿⣿⣯⣪⡛⢿⢣⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣻⣧⣿⣿⣿⣿⡏⣺⣿⣿⣿⣿⣿⣿⢗⡨⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⢳⣵⣿⣿⣿⣿⣿⣿⡿⢠⣿⣿⣿⣿⣿⢟⠕⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⢻⣿⣿⣿⣿⣿⣿⢓⣿⣿⣿⡿⢋⠕⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠱⡹⣿⣿⣿⣿⠏⣼⣿⡿⡫⠒⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢞⢿⣿⡟⣸⡿⡯⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢫⡻⢕⠡⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
	"""

	parser = argparse.ArgumentParser()

	parser.add_argument("-w", "--wordlist", action="store", required=True, type=str, help="wordlist to use for enumeration.")
	parser.add_argument("-t", "--target", action="store", required=True, type=str, help="target to enumerate.")
	parser.add_argument("--refreship", action="store_true", required=False, default=False, help="reload new TOR ip.")

	args = parser.parse_args()

	wordlist = args.wordlist
	target = args.target
	refresh_ip = args.refreship

	print(banner)

	if refresh_ip:
		tor_functions.refresh_IP()
		print("[!] Refreshing IP\n")
		time.sleep(1)

	## open wordlist, may use arg.parse
	sub_list = open(wordlist).read()
	directories = sub_list.splitlines()

	# length of list
	list_length = len(directories)

	# connect to tor proxy
	session = tor_functions.tor_connect()

	# get ip
	my_ip = session.get("http://httpbin.org/ip").json().get('origin')

	# create USer-Agent
	headers = {
		'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
	}

	print()
	print("My IP: ")
	print(my_ip)
	print()

	print("[!] Starting enumeration")

	enumerate_directories(session, target, directories)

	# clear previous print()
	sys.stdout.write("\033[K")
	print()
	time.sleep(2)

	print("Finished.")
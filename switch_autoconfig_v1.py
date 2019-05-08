#! /usr/bin/python3

import telnetlib
import getpass

# THIS SCRIPT AUTOMATES THE VLAN CONFIGURATION FOR A CISCO CATALYST SWITCH .

Host = "<your IP ADDRESS>"
user = bytes(input("Enter your username: "), encoding='ascii')
password = bytes(getpass.getpass("Enter Your password: "), encoding='ascii')
tn = telnetlib.Telnet(Host)


def configureDevice():
	vlanID = range(2,35)

		# ENTER GLOBAL CONFIG-MODE
	tn.write(b"conf t" +"\n".encode("ascii"))

	for ID in vlanID:
			# CONVERTING THE INTEGER TO A BYTES OBJECT
		convertedID = bytes(str(ID), encoding='ascii')
		tn.write(b"vlan %b\n" % convertedID)
		tn.read_until(b"#")
		tn.write(b"name VLAN-%b\n" % convertedID)

	tn.write(b"end" + "\n".encode("ascii"))
	tn.write(b"exit" +"\n".encode("ascii"))
	tn.read_all()
	return


def logintoDevice():
# INTIAL LOGEN PHASE
	tn.read_until(b"Username: ")
	tn.write(user + "\n".encode("ascii"))

	if password:
		tn.read_until(b"Password: ")
		tn.write(password + "\n".encode("ascii"))
		tn.write(b"en" + "\n".encode("ascii"))

# PASSWORD TO ENTER ENABLE MODE
		if password:
			tn.read_until(b"Password: ")
			tn.write(password + "\n".encode("ascii"))
			configureDevice()
	return

logintoDevice()

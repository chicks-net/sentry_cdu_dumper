#!/usr/bin/env python

import csv
import optparse
#import pprint
#import os.path
import telnetlib
import sys

# command line options
parser = optparse.OptionParser()
(options, args) = parser.parse_args()

if len(args) != 1:
	parser.error("incorrect number of arguments")

pdu_name = args[0]
print pdu_name
#sys.exit(1)

# dump PDU stats
tn = telnetlib.Telnet(pdu_name)

tn.read_until("Username: ")
tn.write("admn\n")
tn.read_until("Password: ")
tn.write("admn\n")
tn.read_until("Switched CDU:")
tn.write("set option more disabled\n")
tn.read_until("Switched CDU:")
tn.write("ostat all\n")
output = tn.read_until("Switched CDU:")
tn.write("set option more enabled\n")
tn.read_until("Switched CDU:")
tn.write("exit\n")

print "-----------------"
print "-----------------"
print output
print "-----------------"
print "-----------------"

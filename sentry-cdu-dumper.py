#!/usr/bin/env python

import csv
import optparse
#import pprint
#import os.path
import telnetlib
import sys

# command line options
parser = optparse.OptionParser()
parser.add_option("-m", "--match", metavar="REGEX", dest="match",
                  help="match outlet name against REGEX and filter out non-matches")
parser.add_option("-s", "--slave_total", default="False", action="store_true", dest="slave_totals",
                  help="total corresponding master and slave ports such as A12 and B12")
parser.add_option("-t", "--total", default="False", action="store_true", dest="column_totals",
                  help="total numeric columns")

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

#!/usr/bin/env python

import csv
import optparse
#import pprint
#import os.path
import telnetlib
import sys
import os

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
tn = telnetlib.Telnet(pdu_name,23,10)
pdu_pass = os.getenv('PDU_PASS','admn') 
print "connected... logging in with admn/" + pdu_pass

tn.read_until("Username: ")
tn.write("admn\n")
tn.read_until("Password: ")
tn.write(pdu_pass + "\n")

expected = tn.expect(["Switched CDU:","Access denied"],5)
if expected[0] == 0:
	print "logged in..."
else:
	print "login failed!"
	sys.exit(2)

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

# TODO: parse "ostat all" output

# TODO: print all or matching ports

# TODO: totals

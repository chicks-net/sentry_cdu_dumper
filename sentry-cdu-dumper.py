#!/usr/bin/env python

import csv
import optparse
#import pprint
#import os.path
import telnetlib
import sys
import os
import re

# command line options
parser = optparse.OptionParser()
parser.add_option("-m", "--match", metavar="REGEX", dest="match", default="",
                  help="match outlet name against REGEX and filter out non-matches")
parser.add_option("-s", "--slave_total", default="False", action="store_true", dest="slave_totals",
                  help="total corresponding master and slave ports such as A12 and B12")
parser.add_option("-t", "--total", default="False", action="store_true", dest="column_totals",
                  help="total numeric columns")

(options, args) = parser.parse_args()

if len(args) != 1:
	parser.error("incorrect number of arguments")

# TODO: accept multiple PDU arguments
pdu_name = args[0]

# dump PDU stats
tn = telnetlib.Telnet(pdu_name,23,10)
pdu_pass = os.getenv('PDU_PASS','admn') 
print "# connected to " + pdu_name + "... logging in with admn/" + pdu_pass

tn.read_until("Username: ")
tn.write("admn\n")
tn.read_until("Password: ")
tn.write(pdu_pass + "\n")

expected = tn.expect(["Switched CDU:","Access denied"],5)
if expected[0] == 0:
	print "# logged in..."
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

# parse "ostat all" output
lines = output.splitlines();
#print str(len(lines)) + " lines";

ports = {}

for line in lines:
	m = re.match(' *\.[AB][0-9]',line)
	if m:
		#    .B11     TowerB_Outlet11           On         0.00      207.5     0   
		m = re.match(' *\.([AB][0-9]+) +(.*) +(On|Off) +([.0-9]+) +([.0-9]+) +([0-9]+) *',line);
		port_number = m.group(1)
		port_name = m.group(2)
		on_off = m.group(3)
		amps = m.group(4)
		volts = m.group(5)
		watts = m.group(6)
		sortable_port_number = re.sub('x','0',re.sub('^([AB])([\d])$',r"\1x\2",port_number))
		ports[sortable_port_number] =  {
			'name': port_name,
			'port_number': port_number,
			'state': on_off,
			'load': amps,
			'voltage': volts,
			'power': watts
		}

# headings
field_names = ['id', 'outlet_name','status','load_amps','voltage_volts','power_watts']
print "\t". join( field_names )

# print all or matching ports
for sort_port_number in sorted(ports.keys()):
	port = ports[sort_port_number]
	m = re.match('^([AB])',sort_port_number)
	pdu = m.group(1)

	output_line = "\t".join( [
		port['port_number'], port['name'], port['state'],
		port['load'], port['voltage'], port['power']
	] )

	if len(options.match):
		if re.search(options.match,port['name']):
			print output_line
	else:
		print output_line


# TODO: totals

sentry_cdu_dumper
=================

ServerTech Sentry CDU dump power data

Options
-------

`-m` *regex* -- match outlet name against *regex* and filter out non-matches

`-s` -- total corresponding master and slave ports such as A12 and B12

`-t` -- total numeric columns

Environment
-----------

`PDU_PASS` -- PDU password if changed from the default

Examples
--------

	$ export PDU_PASS=your_nondefault_password
	$ ./sentry-cdu-dumper 10.24.0.112 -m rtbd
	id      outlet_name     status  load_amps       voltage_volts   power_watts
	A7      A:rtbdserv-v02-10a      On      0.45    207.8   73
	B7      B:rtbdserv-v02-10a      On      0.30    206.9   43
	$ ./sentry-cdu-dumper 10.24.0.112 -m rtbd -t
	id      outlet_name     status  load_amps       voltage_volts   power_watts
	A7      A:rtbdserv-v02-10a      On      0.43    207.8   71
	B7      B:rtbdserv-v02-10a      On      0.30    206.9   45
	N/A     SUMMED TOTALS   N/A     0.73    414.7   116    
	$ ./sentry-cdu-dumper 10.24.0.112
	# [ full output with no filtering or totals ]

Useful Links
------------

* ServerTech docs: http://www.servertech.com/support/technical_library/cwgcxg-xxxxxxxxxx_pops_switched_cabinet_pdu

python version
--------------

The python version of the dumper script is currently mainly an effort for me to
learn python.  It may lack some features that are working in the Perl version.
But if you can't stand Perl and you don't need all of the features give it a try.

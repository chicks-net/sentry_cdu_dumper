Sentry CDU Dumper
=================

[![GPLv2 license](https://img.shields.io/badge/License-GPLv2-blue.svg)](https://github.com/chicks-net/sentry_cdu_dumper/blob/master/LICENSE)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/chicks-net/sentry_cdu_dumper/graphs/commit-activity)

[ServerTech](https://www.servertech.com/) Sentry CDU dump power data

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
	$ sentry-cdu-dumper 10.24.0.112
	# [ full output with no filtering or totals ]

	$ sentry-cdu-dumper 10.24.0.112 -m rtbd
	id      outlet_name     status  load_amps       voltage_volts   power_watts
	A7      A:rtbdserv-v02-10a      On      0.45    207.8   73
	B7      B:rtbdserv-v02-10a      On      0.30    206.9   43

	$ sentry-cdu-dumper 10.24.0.112 -m rtbd -t
	id      outlet_name     status  load_amps       voltage_volts   power_watts
	A7      A:rtbdserv-v02-10a      On      0.43    207.8   71
	B7      B:rtbdserv-v02-10a      On      0.30    206.9   45
	N/A     SUMMED TOTALS   N/A     0.73    414.7   116    

	$ sentry-cdu-dumper 10.24.0.112 -m 3 -s
	id      outlet_name     status  load_amps       voltage_volts   power_watts
	A3,B3   TowerA_Outlet3,TowerB_Outlet3   On,On   0.78    414.7   122
	A13,B13 TowerA_Outlet13,TowerB_Outlet13 On,On   0       414.4   0
	A23,B23 TowerA_Outlet23,TowerB_Outlet23 On,On   1.64    415.2   324

Useful Links
------------

* [ServerTech docs](https://web.archive.org/web/20140709034458/http://www.servertech.com/support/technical_library/cwgcxg-xxxxxxxxxx_pops_switched_cabinet_pdu/)

python version
--------------

The python version of the dumper script started as an effort for me to improve
my python skills.  It is currently at feature parity with the Perl version, but
only lightly tested.
If you want something with a few months more testing the Perl version is
for you.  But if you hate Perl or like to live on the bleeding edge, try the python
version and let me know how it goes.


sentry_cdu_dumper
=================

ServerTech Sentry CDU dump power data

Options
-------

`-m` *regex* -- match outlet name against *regex* and filter out non-matches

`-t` -- total numeric columns

Examples
--------

Useful Links
------------

* ServerTech docs: http://www.servertech.com/support/technical_library/cwgcxg-xxxxxxxxxx_pops_switched_cabinet_pdu

python version
--------------

The python version if the dumper script is currently mainly an effort for me to learn python.  It lacks the 
features such as command line options that are work in the Perl version.  The python version is less buggy and
faster due to disabling the "more" pager within the Sentry interface.  This will be integreated in the
Perl version RSN.

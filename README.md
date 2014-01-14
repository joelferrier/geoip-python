#geoip-python

---
##Overview
A python script to search [MaxMind geo-ip databases](http://dev.maxmind.com/geoip/legacy/geolite/).

---
##Dependencies

---
This script depends on the open source c library libmaxminddb ( [source](https://github.com/maxmind/libmaxminddb/), [tarball](https://github.com/maxmind/libmaxminddb/releases) ).
Python bindings must also be installed via pip:

	pip install maxminddb
	pip install geoip2
##Installation

---
**TODO:** Automate installation to posix conformant location location

It is recommmended to alias this command to include the location of the GeoLite2 database you wish to use.

You may choose to make this script executable instead of invoking this script with:

	python geoip-python.py ...
	
Make this script executable with chmod.

	chmod +x geoip-python.py

##Usage

---
example usage:

	python geoip-update.py /path/to/database/ 4.2.2.2

help text:

	usage: geoip-find.py [-h] [-v] [-c] database_path ip_address

	positional arguments:
	  database_path  path to a GeoLite2 database
	  ip_address     ipv4 address
	
	optional arguments:
	  -h, --help     show this help message and exit
	  -v, --verbose  increase output verbosity
	  -c, --city     search to city level, use only with a City database


##Recommended Software 

---

[maxmind-geolite-update](https://github.com/snowplow/maxmind-geolite-update) is an open source project that automates updating GeoLite databases and is easily modified to accept GeoLite2 databases

####example maxmind-geolite-update GeoLite2 config:

	[Local]
	download-dir: /usr/local/share/GeoIP/download
	destination-dir: /usr/local/share/GeoIP
	
	[MaxMind]
	uri: http://geolite.maxmind.com/download/geoip/database/ ; Needs trailing slash
	
	[Files]
	file1: GeoLite2-Country.mmdb.gz ; DELETE this line if you are a 	subscriber
	file2: GeoLite2-City.mmdb.gz ; DELETE this line if you are a subscriber 

##License

---
**GPLv3**

Copyright (C) 2014 Joel Ferrier

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

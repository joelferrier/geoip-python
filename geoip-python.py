#!/usr/bin/env python

"""
geoip-python is a python frontend for the freely availible maxmind GeoLite2 databases
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
"""
import argparse
import os
import sys

class ip_lookup:
    __version__ = "0.1"
    arguments = None
    
    # check for dependencies and parse input
    def __init__(self):
        print "geoip-python version: {vers}".format(vers=self.__version__)
        self.arguments = self.parse_args()
        if  self.module_exists("geoip2") and self.module_exists("maxminddb"):
            print "Dependencies Resolves: executing"
        else:
            print "Error: Missing Dependencies"
            print "  Refer to help [-h] for information"
            quit()
    
    # check for dependency
    def module_exists(self,module_name):
        try:
            __import__(module_name)
        except ImportError as e:
            if self.arguments.verbose:
                print type(e)
                print e.args
            return False
        else:
            return True
    
    # verify command line args
    def parse_args(self):
        help_txt = ("valid databases:\n  "
            "Requires an absolute or relative path to GeoLite2 database\n"
            "  GeoLite Databases can be found at:\n"
            "    \"http://dev.maxmind.com/geoip/legacy/geolite/\"\n\n"
            "caveats:\n"
            "  This script depends on the maxmind GeoIP C library"
            " and it's python bindings.\n"
            "  The c source tarball can be downloaded from:\n"
            "    https://github.com/maxmind/libmaxminddb/releases\n"
            "  Installation instructions can be found at:\n"
            "    https://github.com/maxmind/libmaxminddb\n"
            "  Python bindings can be installed with\n"
            "    \"pip install geoip2\"\n"
            "  Additional python dependencies can be installed with \n"
            "    \"pip install maxminddb\"\n\n"
            "license:\n  GPLv3\n")
        parser = argparse.ArgumentParser(description=("Python frontend for"
                 " GeoIP lookups"),
                 formatter_class=argparse.RawDescriptionHelpFormatter,
                 epilog=help_txt)
        parser.add_argument("-v","--verbose",help="increase output verbosity",
                            action="store_true")
        #TODO fix hacky addition to help message
        parser.add_argument("-c","--city",help="search to city level,"+
                            " use only with a City database",
                            action="store_true")
        parser.add_argument("database_path",
                            help="path to a GeoLite2 database")
        parser.add_argument("ip_address",help="ipv4 address")
        
        args = parser.parse_args()
        if args.verbose:
            print "verbose mode: enables"
            print "checking validity of database path"
        if not os.path.exists(args.database_path):
            print "Error: Invalid database path"
            quit()
        return args
    
    def run(self):
        import geoip2.database
        args = self.arguments
        reader = geoip2.database.Reader(args.database_path)
       
        #choose between city or country database based on [-c] flag
        if args.city:
            if args.verbose:
                print "-c flag set: searching to city level"
            try:
                response = reader.city(args.ip_address)
                print "\nip address: {addr} City: {city} Country: {country}".format(
                    addr=args.ip_address,
                    city=response.city.name,
                    country=response.country.name)
                print "Lat: {lat} Long: {long}".format(
                    lat=response.location.latitude,
                    long= response.location.longitude)
            except AttributeError as e:
                print "Error: invalid database"
                print"  Refer to help [-h] for more information"
                if args.verbose:
                    print type(e)
                    print e.args
        else:
            if args.verbose:
                print "-c flag not set: searching to country level"
            try:
                response = reader.country(args.ip_address)
                print "\nip address: {addr} Country: {country}".format(
                addr=args.ip_address,
                country=response.country.name)
            except AttributeError as e:
                print "Error: invalid database"
                print "Refer to help [-h] for more information"
                if args.verbose:
                    print type(e)
                    print e.args

if __name__=="__main__":
    ip_lookup_instance = ip_lookup()
    ip_lookup_instance.run()

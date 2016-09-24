#!/usr/bin/env python

import sys, getopt

from time import sleep
from datetime import date
from colorama import init
from termcolor import cprint
from pyfiglet import figlet_format

init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected

# start
show_section = (len(sys.argv) > 1 and sys.argv[1] or "")
show_all_sections = (show_section == "" and True or False)

# print 'show_section:', show_section
# print 'show_all_sections:', show_all_sections

def my_sleep(time):

	skip_sleep = False
	if skip_sleep:
		return
	else:
		sleep(time)

# helper functions

def divider():

	sys.stdout.write('\r\n\r\n')
	sys.stdout.write(60 * '=')
	sys.stdout.write('\r\n\r\n')

def days_from_bd():

	today = date.today()
	bday = date(1994, 7, 22)

	return (today-bday).days

def centered_string(string):

	total_len = 60
	str_len = len(string)

	fill_symbol = '='
	fill_count = total_len - str_len

	# str_start_index = fill_count / 2 - 1
	# str_finish_index = fill_count / 2 + str_len

	output = '\n' + (fill_count / 2 - 1) * fill_symbol
	output = output + " " + string.upper() + " "
	output = output + (fill_count / 2 - 1) * fill_symbol + '\n'

	return output

def progress_bar():

	for i in range(21):
	    sys.stdout.write('\r')
	    # the exact output you're looking for:
	    sys.stdout.write("importing positive vibes: \t[%-21s] %d%%" % ('='*i, 5*i))
	    sys.stdout.flush()
	    my_sleep(0.05)

	sys.stdout.write('\r\n')




# section functions

def section_heading():
	# section 0 - heading

	print
	progress_bar()
	my_sleep(1)
	print

	hello_friend = figlet_format('hello friend', font='cybermedium')
	# hello_friend = figlet_format('hello friend', font='cybermedium')

	cprint(hello_friend)
	my_sleep(1)
	cprint(centered_string('my name is'), 'green')

	my_sleep(1)
	cprint(figlet_format('OLEG', font='univers'), 'yellow')
	my_sleep(1)
	cprint(figlet_format('KUKIL', font='univers'), 'yellow')
	my_sleep(1)

	cprint(centered_string('and i live on this planet about'), 'blue')

	my_sleep(1)
	cprint(figlet_format('22 years', font='basic'), 'red', attrs=['bold'])
	cprint(centered_string('was borned ' + str(days_from_bd()) + ' days ago'), 'magenta')
	# print days_from_bd()
	my_sleep(1)


def section_introduction():
	# section 1 - introduction
	print "Section 1 - Introduction"

# show all sections and exit

if show_all_sections == True:

	section_heading()
	section_introduction()

	exit


# show single specified section

if show_section == 'heading':
 	section_heading()

if show_section == 'introducion':
 	section_introduction()


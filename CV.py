#!/usr/bin/env python

import sys,time,random

from subprocess import call

from time import sleep
from datetime import date
from colorama import init
from termcolor import cprint, colored
from pyfiglet import figlet_format
from colorama import Fore, Back, Style

init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected

# start
show_section = (len(sys.argv) > 1 and sys.argv[1] or "")
show_all_sections = (show_section == "" and True or False)

typing_speed = 50 #wpm

# print 'show_section:', show_section
# print 'show_all_sections:', show_all_sections

def my_sleep(time):

	skip_sleep = True
	if skip_sleep:
		return
	else:
		sleep(time)

def slow_type(t):
    for l in t:
    	sys.stdout.write(l)
        sys.stdout.flush()
        my_sleep(random.random()*10.0/typing_speed)

    print ''

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

def progress_bar(title):

	print

	for i in range(21):
	    sys.stdout.write('\r')
	    # the exact output you're looking for:
	    sys.stdout.write(title + " -> \t[%-21s] %d%%" % ('='*i, 5*i))
	    sys.stdout.flush()
	    my_sleep(0.05)

	sys.stdout.write('\r\n')
	my_sleep(1)
	print




# section functions

def section_heading():
	# section 0 - heading

	progress_bar("importing positive vibes")

	hello_friend = figlet_format('hello friend', font='cybermedium')
	# hello_friend = figlet_format('hello friend', font='cybermedium')

	cprint(hello_friend)
	my_sleep(3)
	cprint(centered_string('my name is'), 'green')

	my_sleep(1)
	cprint(figlet_format('OLEG', font='univers'), 'yellow')
	my_sleep(2)

	cprint(centered_string('and i live on this planet about'), 'blue')

	my_sleep(1)
	cprint(figlet_format('22 years', font='basic'), 'red', attrs=['bold'])

	my_sleep(1)
	cprint(centered_string('to be precise'), 'magenta')

	my_sleep(1)
	cprint(figlet_format(str(days_from_bd()) + ' days', font='banner'), 'white', attrs=['bold'])

	divider()
	my_sleep(4)

def section_introduction():
	# section 1 - introduction

	progress_bar("collecting old memories")

	section_color = 'green'
	cprint(centered_string('let me introduce myself'), 'cyan')
	my_sleep(2)

	print
	colored_text = colored('I am young web-developer from Precarpathian capital of Ukraine Ivano-Frankivk\'s.', section_color)
	slow_type(colored_text)
	my_sleep(1)

	print
	colored_text = colored('From school age I was interested in the various devices and mechanisms. The movie "Water World" was my favorite at that time.', section_color)
	slow_type(colored_text)
	my_sleep(1)

	print
	colored_text = colored('Was studying in famous College of Electronic Devices from 2009 to 2013 years. ', section_color)
	slow_type(colored_text)
	my_sleep(1)

	print
	colored_text = colored('Then began my journey into the world of internet from creating simple PHP scripts for mobile sites.', section_color)
	slow_type(colored_text)
	my_sleep(1)

	divider()
	my_sleep(3)

def section_work():
	# section 2 - work

	progress_bar("scanning work experience")

	cprint(centered_string('first work in 2013, in company named:'), 'green')

	my_sleep(1)
	cprint(figlet_format('TimTek', font='cybermedium'), 'blue', attrs=['bold'])
	my_sleep(1)

	slow_type('started at:')
	my_sleep(1)
	print
	call(["cal", "-m 1" ,"2013"])

	slow_type('finished at:')
	my_sleep(1)
	print
	call(["cal", "-m 2" ,"2013"])

	cprint(centered_string('what i was doing?'), 'cyan')



# show all sections and exit

if show_all_sections == True:

	call(["cowsay", "let's get it started (ha)"])
	my_sleep(2)

	section_heading()
	section_introduction()
	section_work()

	exit


# show single specified section

if show_section == 'heading':
 	section_heading()

if show_section == 'introducion':
 	section_introduction()

if show_section == 'work':
 	section_work()


#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-

##################################
#  @program        synda
#  @description    climate models data transfer program
#  @copyright      Copyright “(c)2009 Centre National de la Recherche Scientifique CNRS. 
#                             All Rights Reserved”
#  @license        CeCILL (https://raw.githubusercontent.com/Prodiguer/synda/master/sdt/doc/LICENSE)
##################################

"""This module is like 'sdutils' module, except that it doesn't use any other
(synda) module and thus can be used everywhere (even in 'sdtypes' module).
"""

import sys
import os
import re
import argparse

def trace(tracefile,scriptname,status,stdout,stderr):
    with open(tracefile,'a') as fh:
        fh.write("'%s' script returned an error\n"%scriptname)
        fh.write('status=%s\nstdout=%s\nstderr=%s\n'%(status,stdout.rstrip(os.linesep),stderr.rstrip(os.linesep)))

def is_root():
    if os.geteuid() == 0:
        return True
    else:
        return False

def is_daemon():

    # the parent of a daemon is always Init, so check for ppid 1 
    if os.getppid() == 1:

        # note that in some case, some non-daemon also have init as parent
        # so we double check with controlling tty (i.e. daemon have no controlling tty)
        if not os.isatty(sys.stdout.fileno()):
            return True
        else:
            return False

    else:
        return False

def portable_chomp (line):
    """Remove eol."""
    return line.rstrip('\r\n')

def remove_dict_items(di,keys_to_remove):
    for k in keys_to_remove:
        try:
            del di[k]
        except KeyError:
            pass

class DefaultHelpParser(argparse.ArgumentParser): 
    """This class display full help when error occurs (instead of only usage).

    Note
        For more info, see http://stackoverflow.com/questions/3636967/python-argparse-how-can-i-display-help-automatically-on-error
    """
    def error(self, message):
        print_stderr('error: %s'% message)
        self.print_help()
        sys.exit(2)

def print_module_variables(variables):
    """Func used when using a python module to store configuration parameters."""
    li=[]
    for k,v in variables.items():
        if '__' not in k: # prevent display of python system variables
            if k!='li':   # prevent display of this list
                if isinstance(v, (str,int,basestring,float,bool,list, tuple)):
                    li.append("%s=%s"%(k,v))
    li=sorted(li)

    for v in li:
        print v

def url_contains_limit_keyword(url):
    """Check if limit is set."""
    if 'limit=' in url:
        return True
    else:
        return False

def grep(li,pattern):

    if pattern is None:
        return li
    else:
        expr = re.compile(pattern)
        return filter(expr.search,li)

def grep_light(li,pattern):

    if pattern is None:
        return li
    else:
        new_li=[v for v in li if pattern in v]
        return new_li

def print_stdout(msg):
    print msg

def print_stderr(msg=""):
    sys.stderr.write("%s\n"%msg)

def multi_columns_listing(li):
    for a,b,c in zip(li[::3],li[1::3],li[2::3]):
        print '{0:<30}{1:<30}{2:<}'.format(a,b,c)

def union(a, b):
    """Return the union of two lists (and remove duplicate).

    Not used.
    """
    if a==None and b<>None:
        return list(set(b))
    if a<>None and b==None:
        return list(set(a))
    if a==None and b==None:
        return []
    if a<>None and b<>None:
        return list(set(a) | set(b))

def intersect(a, b):
    """Return True if the two lists intersect."""
    if any(i in a for i in b):
        return True
    else:
        return False

def extract_digit(li):
    """This fonction separates pure digit value(s) from 'alum' items.

    Args:
        li (list)

    Not used.
    """
    alum=[]
    digit=[]

    for token in li:
        if token.isdigit():
            digit.append(int(token)) # change the type from string to int
        else:
            alum.append(token)
    
    return (alum,digit)

def split_values(values):


    # cleaning (trim spaces on both ends)
    values=values.strip()


    # build regex
    if ',' in values:
        # delimiter is ','

        r = re.compile('\s*,\s*')
    else:
        # delimiter is ' '

        r = re.compile('\s+')


    # split
    values_list=r.split(values)


    return values_list

def compute_rate(size,duration):
    """Unit: bytes / seconds.

    Not used.
    """
    if duration==0:
        return 0
    else:
        return size / duration

def set_terminal_cursor_visible():
    """Turn on the cursor.

    BEWARE: this send code below on stderr
            ESC[34hESC[?25hESC[34hESC[?25h
    """
    os.system('setterm -cursor on 1>&2') # redirect to stderr to prevent messing with stdout text stream

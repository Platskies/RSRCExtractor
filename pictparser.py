#!/usr/bin/env python

import os
import errno
import re
import struct
import sys
import subprocess

def usage():
    print "Usage: " + sys.argv[0] + ": [--skip-derez] <path to file>"
    sys.exit(1)
    
argc = len(sys.argv)
if argc == 1: usage()
neededargs = 2 if sys.argv[1] != "--skip-derez" else 3
if argc < neededargs: usage()

if neededargs == 2:
    p = subprocess.Popen(["DeRez", "-only", "PICT", sys.argv[1]], \
    			stdout=subprocess.PIPE)
    out = p.communicate()
    if p.returncode != 0:
        sys.exit(p.returncode)

    out = out.split('\n')
else:
    out = open(sys.argv[2], "ru")

try:
    os.mkdir("output")
except OSError as error:
    if error.errno != errno.EEXIST:
        raise

for l in out:
    if len(l) == 1:
        continue
    # start of file
    if re.match('data ', l):
        m = re.search('\'(.*)\' \((.*)\)', l)
        res = m.group(1)
        num = m.group(2)
        print "open %s %s" % (res, num)
        
        filename = res+num
            
        working = open("output/" + filename, "wb")
        for a in range(0, 512):
            s = struct.pack(">B", 0);
            working.write(s)
    # end of file
    elif re.match('\}\;', l):
        working.close()
    # file data
    else:
        cap = re.search(r'^\s*\$\"(.*)\"\s*/\*.*\*/', l)
        if cap is None:
            continue
        data = cap.group(1)
        data = data.translate(None, '"')
        for a in data.split(' '):
            if len(a) != 4:
                continue
            first, second = a[:len(a)/2], a[len(a)/2:]
            pdata = struct.pack(">BB", int(first, 16), int(second, 16))
            working.write(pdata)

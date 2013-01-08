#!/usr/bin/env python

import sys
import os

ls = os.linesep
ddd = "tt.txt"
while True:
	if os.path.exists(ddd):
		print "ERROR: %s already exists" % ddd
	else:
		break

all = []

while True:
	entry = raw_input('> ')
	if entry == '.':
		break
	else:
		all.append(entry)

fobj = open(ddd, 'w')
fobj.writelines(['%s%s'%(x, ls) for x in all])
fobj.close()
print "Done!"

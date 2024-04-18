#!/usr/bin/env python
#
# LaunchBar Action Script
#
import sys
import json
from subprocess import Popen, PIPE

items = []

item = {}
item['title'] = str(len(sys.argv) - 1) + ' arguments passed'
items.append(item)

scpt = '''
    on run {_string}
        set launchbarResult to {}
    end run'''
args = [sys.argv[1]]

p = Popen(['osascript', '-'] + args, stdin=PIPE, stdout=PIPE, stderr=PIPE)
stdout, stderr = p.communicate(scpt.encode('utf-8'))
stdout.decode('utf-8')
print (p.returncode, stdout, stderr)

print json.dumps(items)
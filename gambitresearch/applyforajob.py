#!/usr/bin/env python

import re
import sys
import urllib.request

if __name__ == '__main__':
    ''' Enable cookies  '''
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor())
    urllib.request.install_opener(opener)
    ''' fetch data  '''
    remote = urllib.request.urlopen("http://quiz.gambitresearch.com/")
    data = remote.read()
    remote.close()
    ''' Easy calculation  '''
    regex = re.compile(r'\{(.*)\}')
    expr = regex.search(data.decode("utf-8"))
    ''' re-fetch data '''
    remote = urllib.request.urlopen("http://quiz.gambitresearch.com/job/" + str(eval(expr.group(1))))
    data = remote.read()
    remote.close()
    ''' Write file '''
    if (len(sys.argv) == 1):
        print(data.decode("utf-8"))
    else:
        writefile = open(sys.argv[1], "w")
        writefile.write(data.decode("utf-8") + '\n')
        writefile.close()
print("Done")

# -*- coding: latin-1 -*-
#                    latin-1        
#              utf-8                   ,
# myStr1  0xc4  0xe8       utf-8                  

myStr1 = 'aÄBèC'

myStr2 = 'A\u00c4B\U000000e8C'

myStr3 = 'A' + chr(0xC4) + 'B' + chr(0xE8) + 'C'

import sys
print('Default encoding:', sys.getdefaultencoding())

for aStr in myStr1, myStr2, myStr3:
    print('{0}, strlen={1}, '.format(aStr, len(aStr)), end='')

    bytes1 = aStr.encode()             #    utf-8         .             2   
    bytes2 = aStr.encode('latin-1')    #       1   
   #bytes3 = aStr.encode('ascii')      #             . 0-127        

    print('byteslen1={0}, byteslen2={1}'.format(len(bytes1), len(bytes2)))

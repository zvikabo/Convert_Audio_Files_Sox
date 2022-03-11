"""
This script open file and append string to the file and than close the file
"""
from __future__ import unicode_literals


def main():

    f='C:\\PythonTemp\write2file\write2file.txt'
    g= open(f,'a')
    for i in range(10):
        g.write('{} ddhnfmf,mdfdf,mdsf,mn,mfnmdfnmdnfmdn \n ' .format(i) )
        g.flush()
    g.close()

if __name__=='__main__':
    main()




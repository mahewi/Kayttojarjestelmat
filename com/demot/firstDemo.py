#!/usr/bin/python

import os

if __name__ == '__main__':
        pass

def parentProcess():
        for i in range(3):
                newProcessId = os.fork()
                if newProcessId == 0:
                        childProcess()
                else:
                        writeToFile()

def childProcess():
        writeToFile()
        os._exit(0)

def writeToFile():
        with open(str(os.getpid()) + '.txt', 'w') as fout:
                fout.write('ProcessID: ' + str(os.getpid()) + '\n')
                fout.write('ParentID: ' + str(os.getppid()) + '\n')
                fout.write('Process groupID: ' + str(os.getpgid(os.getpid())) + '\n\n')

parentProcess()
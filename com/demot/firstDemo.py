#!/usr/bin/python

import os

if __name__ == '__main__':
        pass

def fork():
        for i in range(3):
                newProcessId = os.fork()
                if newProcessId == 0:
                        os._exit(0)
                else:
                        processIds = (newProcessId, os.getpid(), os.getpgid(newProcessId))
                        #print "parentID: %d, ProcessID: %d, process groupID: %d" % processIds

                        with open(str(newProcessId) + '.txt', 'w') as fout:
                                fout.write('ProcessID: ' + str(processIds[0]) + '\n')
                                fout.write('ParentID: ' + str(processIds[1]) + '\n')
                                fout.write('Process groupID: ' + str(processIds[2]) + '\n')

fork()
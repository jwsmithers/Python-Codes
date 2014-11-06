#!/usr/bin/env python

##############################
# Joshua Smith		     #
# Joshua.Wyatt.Smith@cern.ch #
##############################

import os
import subprocess


def chunkIt(seq, num):
  avg = len(seq) / float(num)
  out = []
  last = 0.0

  while last < len(seq):
    out.append(seq[int(last):int(last + avg)])
    last += avg

  return out

def Cleanup(numProcs):
	for i in xrange(int(numProcs)): 
		subprocess.Popen("rm -r temp%d"%i,shell=True)

def createLayout(numProcs):
	path, dirs, files = os.walk("/home/jwsmith/HDD/EoverP/DataSets/Merged_Test").next()
        file_count = len(files)
	Lists=chunkIt(files,numProcs)
	for i in xrange(int(numProcs)):
		subprocess.Popen("mkdir temp%d"%i,shell=True)
	for n in xrange(len(Lists)):
		for m in xrange (len(Lists[n])):
        		subprocess.Popen("ln %s/%s temp%d/"%(path,Lists[n][m],int(n)),shell=True)


def run(numProcs):
	createLayout(numProcs)
	for i in xrange(numProcs):
		subprocess.Popen("time main -d ./temp%d -o Output%d.root &"%(i,i),shell=True)
	#Cleanup(numProcs)	
run(4)

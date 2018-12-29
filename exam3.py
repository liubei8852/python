#!/usr/bin/env python

import sys
import math
import argparse
parser=argparse.ArgumentParser(prog='stat python ',usage='%(prog)s [opthions] [value]',description='stat base num!')
parser.add_argument('-i','--in',help='the physical file ',required=True,metavar='')
parser.add_argument('-o','--out',help='the genetic file ',required=True,metavar='')
argv=vars(parser.parse_args())
in_file=argv['in'].strip()
out_file=argv['out'].strip()
f1=open(in_file).readlines()
f2=open(out_file,'w')

for reads in f1:
  #n1=len(reads)
  n1=reads.count("G")
  for i in range (1,n1):
    if (4*i+1>n1):
      break
  n2=4*(i-1)+1
  add=n2%3
  if(add/2==0):
    num=int(math.ceil(n2/3))
  else:
    num=int(n2/3)
  f2.write(str(n1)+"\t"+str(n2)+"\t"+str(num)+"\t"+reads)
f2.close

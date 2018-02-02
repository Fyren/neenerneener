import sys
from ambuild2 import run, util

parser = run.BuildParser(sourcePath=sys.path[0], api='2.1')
parser.Configure()

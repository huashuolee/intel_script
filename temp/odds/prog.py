import argparse
parser = argparse.ArgumentParser()
parser.add_argument("echo",help="echo the string you use here")
parser.add_argument("square", help="display a square of a given number",type = int)
parser.add_argument('-v',"--verbosity", help="increase output verbosity",action='store_true')
args = parser.parse_args()
print args.echo
print args.square**2
print args.verbosity
print args
if args.verbosity:
    print 'verbosity turned on'

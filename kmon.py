#!/usr/bin/env python

import sys

def main(argv):
    try: 
        sys.path.append("./modules")
        import kmon_main
    except Exception, exc:
        print (str(exc))
        print 'Command failed!'
        sys.exit(1)

if __name__ == "__main__":
    main(sys.argv[1:])
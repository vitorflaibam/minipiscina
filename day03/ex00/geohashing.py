import sys
from antigravity import geohash

def run():
    if (len(sys.argv) != 4):
        print("Invalid or empty arguments.")
    else:
        geohash(float(sys.argv[1]), float(sys.argv[2]), sys.argv[3].encode('utf-8'))
        
if __name__ == "__main__":
    run()

#  '''Compute geohash() using the Munroe algorithm.

#     >>> geohash(37.421542, -122.085589, b'2005-05-26-10458.68')
#     37.857713 -122.544543

#     '''
# 37.421542 -122.085589 "b'2005-05-26-10458.68'"

# ymdhms_to_jd.py
#
# Usage: python3 ymdhms_to_jd.py year month day hour minute second
#  Text explaining script usage
# Parameters:
#  arg1: description of argument 1
#  arg2: description of argument 2
#  ...
# Output:
#  A description of the script output
#
# Written by Erika Ashley
# Other contributors: None
#


# import Python modules
# e.g., import math # math module
import sys # argv
import math 

# "constants"
R_E_KM = 6378.137
E_E    = 0.081819221456
# helper functions

## function description
# def calc_something(param1, param2):
#   pass

# initialize script arguments
yr = float('nan') # ECEF origin x-component in km
mth = float('nan') # ECEF origin y-component in km
day = float('nan') # ECEF origin z-component in km
hr = float('nan') # ECEF x-component in km
min = float('nan') # ECEF y-component in km
sec = float('nan') # ECEF z-component in km

# parse script arguments
if len(sys.argv)==7:
  yr = float(sys.argv[1])
  mth = float(sys.argv[2])
  day = float(sys.argv[3])
  hr = float(sys.argv[4])
  min = float(sys.argv[5])
  sec = float(sys.argv[6])
else:
  print(\
   'Usage: '\
   'python3 ymdhms_to_jd.py year month day hour minute second'\
  )
  exit()

# write script below this line
JD=(day-32075)+int(1461*(yr+4800+int((mth-14)/12))/4)+int(367*(mth-2-int((mth-14)/12)*12)/12)-int(3*int((int(yr+4900+(mth-14)/12)/100))/4)
JDmid=JD-0.5
Dfrac=(sec+60*(min+60*hr))/86400
jd_frac=JDmid+Dfrac
print(jd_frac)


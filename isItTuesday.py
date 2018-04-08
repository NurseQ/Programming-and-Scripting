# Script to tell if it is Tuesday
# Programming and scripting 2018 
# Adopted from Ian Mcloughlin

import datetime

if datetime.datetime.today().weekday() == 1:
    print("Yes it is Tuesday")

else:
    print("Not yet Tuesday")

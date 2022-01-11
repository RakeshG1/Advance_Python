######### Method 1 - Create a shell script: And call python file inside it #########
####################################################################################

# Suppose you have python file hello.py
# Create a file called job.sh that contains

# !/bin/bash
# python hello.py

# Make it executable file using
# $chmod +x job.sh 

# Then run it
# $./job.sh

######### Method 2 - Make python itself as a shell executable file #########
############################################################################

# Modify your script hello.py and add this as the first line

# !/usr/bin/env python

# Make it as executable file using

# $chmod +x hello.py

# Then run it
# $ ./hello.py
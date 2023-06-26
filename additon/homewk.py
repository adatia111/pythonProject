import sys, glob, os
# Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']
# Construct a portable wildcard pattern
pattern = os.path.join(hdir,'*')
# TODO: Use the glob.glob() function to obtain the list of filenames
# TODO: use os.path.getsize to find each file's size
# TODO: Add a test to only display files that are not zero length
# TODO: Remove the leading directory name(s) from each filename before you print it -
# using os.path.basename()
# TODO: Use the glob.glob() function to obtain the list of filenames
# use glob to return an array of directories in specified pattern
print(glob.glob(pattern))
# TODO: use os.path.getsize to find each file's size
# create a list from glob.glob(pattern)
list = glob.glob(pattern)
for x in list:
# print x, then the file size
    print(x, os.path.getsize(x))
print('')
print('')
# TODO: Add a test to only display files that are not zero l
import sys
argc = len(sys.argv)

if argc>1:
    print("too many argv")
else:
    where = 'world'
    print("hello",where)

print('goodbye from'+ sys.argv[0])

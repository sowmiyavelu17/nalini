str1='"xxx"'
print str1
if str1[:1].startswith('"'):
    if str1[:-1].endswith('"'):
        print "hi"
    else:
        print  "condition fails"
else:
    print  "bye"   

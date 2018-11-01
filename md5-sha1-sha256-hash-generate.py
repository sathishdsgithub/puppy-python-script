from py_essentials import hashing as hs

inputFile = raw_input("Enter the filename or path: ")

hashmd5sum = hs.fileChecksum(inputFile, "md5")
hashsha1 = hs.fileChecksum(inputFile, "sha1")
hash256 = hs.fileChecksum(inputFile, "sha256")

print "\n"
print "MD5 for the file is: %s" %hashmd5sum
print "\n"
print "MD5 for the file is: %s" %hashsha1
print "\n"
print "MD5 for the file is: %s" %hash256

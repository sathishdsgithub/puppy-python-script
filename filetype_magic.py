# python filetype_magic.py FILE_PATH_DIR

import magic
file_path = raw_input("Enter the file path: ")
print "The filetype is", magic.from_file(file_path)


#~/usr/bin/env python
import sys,os
import pefile
import hashlib
import xlsxwriter


if __name__ == "__main__":

	#Identify specified folder with suspect files
	dir_path = sys.argv[1]

	#Create a list of files with full path
	file_list = []
	for folder, subfolder, files in os.walk(dir_path):
		for f in files:
			full_path = os.path.join(folder, f)
			file_list.append(full_path)

	#Open XLSX file for writing
	file_name = "pefull_output.xlsx"
	workbook = xlsxwriter.Workbook(file_name)
	bold = workbook.add_format({'bold':True})
	worksheet = workbook.add_worksheet()

	#Write column headings
	row = 0
	worksheet.write('A1', 'SHA256', bold)
	worksheet.write('B1', 'Imphash', bold)
	row += 1

	#Iterate through file_list to calculate imphash and sha256 file hash
	for item in file_list:

		#Get sha256
		fh = open(item, "rb")
		data = fh.read()
		fh.close()
		sha256 = hashlib.sha256(data).hexdigest()

		#Get import table hash
		pe = pefile.PE(item)
		ihash = pe.get_imphash()			 

		#Write hashes to doc
		worksheet.write(row, 0, sha256)
		worksheet.write(row, 1, ihash)
		row += 1

	#Autofilter the xlsx file for easy viewing/sorting
	worksheet.autofilter(0, 0, row, 2)
	workbook.close()
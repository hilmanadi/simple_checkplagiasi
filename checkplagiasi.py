import json
import os
import xlsxwriter

row = 1
col = 0	

arr = []
arranyar =[]

pointerr =''

def c_file():
	fl = os.listdir('.')

	for i in fl:
		if i != 'checkplagiasi.py' and i != '.git' !='.xlsx':
			arr.append(i)
	la = len(arr)
	
	for x in arr:
		get_file_data(x,la)

def get_file_data(a,b):
	
	substringfor='for'
	substringif='if'
	substringelse='else'
	substringkurawal1='{'
	substringkurawal2='}'
	substringarr1='['
	substringarr2=']'
	substringdoublequote= '"'
	substringsinglequote="'"
	substringjson = 'json'
	substringclass='class'
	substringreturn='return'

	with open(a, 'r') as content_file:
		content = content_file.read()
		finddoublequote = content.count(substringdoublequote)
		findsinglequote = content.count(substringsinglequote)
		findfor = content.count(substringfor)
		findif = content.count(substringif)
		findelse = content.count(substringelse)
		findkurawal1 = content.count(substringkurawal1)
		findkurawal2 = content.count(substringkurawal2)
		findarr1 = content.count(substringarr1)
		findarr2 = content.count(substringarr2)
		findjson = content.count(substringjson)
		findclass = content.count(substringclass)
		findreturn = content.count(substringreturn)

		if '.py' in a:
			substringdef='def'
			substringimport='import'
			substringelif='elif'

			findelif = content.count(substringelif)
			finddef = content.count(substringdef)
			findimport = content.count(substringimport)

			print '------------   ',a,'------------'
			print 'doublequote : ',finddoublequote
			print 'singlequote : ',findsinglequote
			print 'for',findfor
			print 'if',findif
			print 'else',findelse
			print '{',findkurawal1
			print '}',findkurawal2
			print '[',findarr1
			print ']',findarr2
			print 'json',findjson
			print 'class',findclass
			print 'return',findreturn
			
			print 'elif',findelif
			print 'def',finddef
			print 'import',findimport
			global pointerr
			pointerr = 'python'
			cobadict = {'nama_file':a,substringif:findif,substringfor:findfor,substringelse:findelse,substringkurawal1:findkurawal1,substringkurawal2:findkurawal2,substringarr1:findarr1,substringarr2:findarr2,'singlequote':findsinglequote,'doublequote':finddoublequote,substringjson:findjson,substringclass:findclass,substringreturn:findreturn,substringdef:finddef,substringelif:findelif,substringimport:findimport}
			arranyar.append(cobadict)

		elif '.java' in a:
			substringimport='import'
			substringstring = 'string'
			substringint = 'int'
			substringpublic = 'public'
			substringprivate = 'private'
			substringprotected = 'protected'
			substringvoid = 'void'
			substringfloat = 'float'

			findimport = content.count(substringimport)
			findstring = content.count(substring)
			print '------------   ',a,'------------'
			print 'doublequote : ',finddoublequote
			print 'singlequote : ',findsinglequote
			print 'for',findfor
			print 'if',findif
			print 'else',findelse
			print '{',findkurawal1
			print '}',findkurawal2
			print '[',findarr1
			print ']',findarr2
			print 'json',findjson
			print 'class',findclass
			print 'return',findreturn
			
			print 'import',findimport

		elif '.cpp' in a:
			print 'c'
		elif '.js' in a:
			print 'javascript'
		elif '.go' in a: 
			print 'go'
		elif '.html' in a:
			print 'html'
		elif '.php' in a:
			print 'php'
		else:
			print 'lainnya'
def proc():
	if pointerr == 'python':
		pyexcel()
	elif pointerr =='java':
		javaexcel()
	else:
		print 'lainnya'


def pyexcel():
	wb = xlsxwriter.Workbook('python.xlsx')

	wst = wb.add_worksheet()

	wst.write('A1','Nama File')
	wst.write('B1','Jumlah If')
	wst.write('C1','Jumlah Else')
	wst.write('D1','Jumlah Elif')
	wst.write('E1','Jumlah For')
	wst.write('F1','Jumlah {')
	wst.write('G1','Jumlah }')
	wst.write('H1','Jumlah [')
	wst.write('I1','Jumlah ]')
	wst.write('J1','Jumlah Singlequote')
	wst.write('K1','Jumlah Doublequote')
	wst.write('L1','Jumlah JSON')
	wst.write('M1','Jumlah Class')
	wst.write('N1','Jumlah Return')
	wst.write('O1','Jumlah Def')
	wst.write('P1','Jumlah Import')

	for i in range(len(arranyar)):
		wst.write(row, col, arranyar[i]['nama_file']) 
		wst.write(row, col + 1, arranyar[i]['if']) 
		wst.write(row, col + 2, arranyar[i]['else']) 
		wst.write(row, col + 3, arranyar[i]['elif']) 
		wst.write(row, col + 4, arranyar[i]['for']) 
		wst.write(row, col + 5, arranyar[i]['{']) 
		wst.write(row, col + 6, arranyar[i]['}']) 
		wst.write(row, col + 7, arranyar[i]['[']) 
		wst.write(row, col + 8, arranyar[i][']']) 
		wst.write(row, col + 9, arranyar[i]['singlequote']) 
		wst.write(row, col + 10, arranyar[i]['doublequote']) 
		wst.write(row, col + 11, arranyar[i]['json']) 
		wst.write(row, col + 12, arranyar[i]['class']) 
		wst.write(row, col + 13, arranyar[i]['return']) 
		wst.write(row, col + 14, arranyar[i]['def']) 
		wst.write(row, col + 15, arranyar[i]['import']) 

		global row
		row+=1

	wb.close() 

def javaexcel():
	print 'iki java'
if __name__ == "__main__":
	c_file()
	proc()




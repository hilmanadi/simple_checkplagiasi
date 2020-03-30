import json
import os

arr = []
newarr = []

def c_file():
	fl = os.listdir('.')

	for i in fl:
		if i != 'checkplagiasi.py':
			arr.append(i)

	for x in arr:
		get_file_data(x)

def get_file_data(a):
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
	for i in newarr:
		if i[1]>=9:
			print '>= 9',i[0]
			# print 'a'
		else:
			print '<9',i[0]
	
if __name__ == "__main__":
	c_file()
	proc()




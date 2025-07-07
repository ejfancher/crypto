#!/usr/bin/env python


class thing_with_title:
	def __init__(self, title, thing):
		self.para = []
		self.title=title
		line = thing.readline()
		while line != '':
			self.para.append(line)
			line = thing.readline() 
	def getTitle(self):
		return self.title
	def getNote(self):
		# if u can, try convert a byte array stored in para to a str here and return that
		return self.para


class titled_research_item(thing_with_title):
	def __init__(self, title, item):
		thing_with_title.__init__(self, title, item)
		self.dicts = []
		self._titled_research_item__process()
	def __process(self):
		para = self.para
		k = 0
		for i in range(0, len(self.para)):
			ind =  para[i].find(': ')
			if ind > -1:
				parts = para[i].split(': ')
				parts = [elem.strip() for elem in parts]
				self.dicts.append({parts[0] : parts[1]})
				k += 1
		#todo is this the right name? look for : in byte array
		return k
	def __repr__(self):
		return self.title + '\n' + str(self.para) +'\n' + str(self.dicts)

item = titled_research_item('ExampleCertificateAuthorityPublicKey.pem', open('ExampleCertificateAuthorityPublicKey.pem', 'rt'))

print(item.getTitle())
print(item.getNote())
print(item)


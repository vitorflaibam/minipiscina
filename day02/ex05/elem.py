#!/usr/bin/python3
#from tests import *

class Text(str):
	def __str__(self):
		return super().__str__().replace('<', '&lt;').replace('>', '&gt;').replace('\n', '\n<br />\n').replace('"', '&quot;')

class Elem:
	class ValidationError(Exception):
		def __init__(self):
			super().__init__("Invalid type")

	def __init__(self, tag='div', attr={}, content=None, tag_type='double'):
		if (not (self.check_type(content) or content is None)) or (
			tag_type != "double" and tag_type != "simple"):
			raise self.ValidationError
		  
		self.tag = tag
		self.attr = attr
		self.content = []
		if type(content) == list:
			self.content = content
		elif content is not None:
			self.content.append(content)
		self.tag_type = tag_type

	def __str__(self):
		attribute = self.__make_attr()
		content = self.__make_content()

		if self.tag_type == 'double':
			result = "<{0}>{1}</{0}>".format(self.tag, content)
		elif self.tag_type == 'simple':
			result = "<{0}{1}/>".format(self.tag, attribute)
		return result

	def __make_attr(self):
		result = ''
		for pair in sorted(self.attr.items()):
			result += ' ' + str(pair[0]) + '="' + str(pair[1]) + '"'
		return result

	def __make_content(self):
		if len(self.content) == 0:
			return ""
		result = "\n"
		for elem in self.content:
			if len(str(elem)) != 0:
				result += f"{elem}\n"
		result = "  ".join(line for line in result.splitlines(True))
		if len(result.strip()) == 0:
			return ""
		return result

	def add_content(self, content):
		if not Elem.check_type(content):
			raise Elem.ValidationError
		if type(content) == list:
			self.content += [elem for elem in content if elem != Text('')]
		elif content != Text(''):
			self.content.append(content)

	@staticmethod
	def check_type(content):
		return (
			isinstance(content, Elem) 
			or type(content) == Text 
			or (
				type(content) == list 
				and all(
					[type(elem) == Text or isinstance(elem, Elem) for elem in content])))

def test():
	title = Text('"Hello ground!"')
	header1 = Text('"Oh no, not again!"')
	img_src = {"src": "http://i.imgur.com/pfp3T.jpg"}
	html = Elem(
		"html",
		content=[
			Elem("head", content=Elem("title", content=[title])),
			Elem(
				"body",
				content=[
					Elem("h1", content=[header1]),
					Elem("img", img_src, tag_type="simple"),
				],
			),
		],
	)
	print(html)

if __name__ == "__main__":
	test()
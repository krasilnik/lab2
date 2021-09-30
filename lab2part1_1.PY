class Rectangle:
	def __init__(self, width, length):
		self.__width = 1
		self.__length = 1

	def get_length(self):
		return self.__length

	def get_width(self):
		return self.__width

	def set_length(self, length):
		if length in range(0, 20):
			self.__length = length
		else:
			print("incorrect length")

	def set_width(self, width):
		if width in range(0, 20):
			self.__width = width
		else:
			print("incorrect width")

	def perimeter(self):
		p = 2*(self.__width + self.__length)

	def area(self):
		s = self.__width * self.__length

	def display_info(self):
		print("Length:", self.__length, "\tWidth:", self.__width, "\tArea:", s, "\tPerimeter:", p)
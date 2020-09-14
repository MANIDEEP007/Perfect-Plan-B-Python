'''
Take the following Python code that stores a string:`str = 'Perfect-Plan-B:0.7541'
Use find and string slicing to extract the portion of the string after the colon
character and then use the float function to convert the extracted string
into a floating point number. *
'''
str_obj = 'Perfect-Plan-B:0.7541'
start = str_obj.find(":")
print(float(str_obj[start+1:]))

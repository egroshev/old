print_strings = True
code = """
mystring = "hello"
{0}print (mystring)
eriksstring = "bye"
{0}print (eriksstring)
""".format("" if print_strings else "#")
exec(code)
def format_name(first_name, last_name):
	if len (first_name) > 0 and len(last_name) > 0:
        str1 =  "Name: " + first_name+", "+last_name
        return str1
    elif len (first_name) = 0 and (last_name) > 0:
        return "Name: " + last_name
    elif len first_name > 0 and last_name < 0:
        return "Name: " + first_name
	return "" 

print(format_name("Ernest", "Hemingway"))
# Should be "Name: Hemingway, Ernest"

print(format_name("", "Madonna"))
# Should be "Name: Madonna"

print(format_name("Voltaire", ""))
# Should be "Name: Voltaire"

print(format_name("", ""))
# Should be ""
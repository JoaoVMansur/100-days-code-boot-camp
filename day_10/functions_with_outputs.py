#Functions with outputs
def format_name(f_name, l_name):
    """Take a fist name and last name and format it
    to return the title case version of the name."""
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    
    return f"Hello {formated_f_name} {formated_l_name}"

formated_string = format_name("AnGeLA","yU")

#Just like the 'len()' function for exemple when you use the return inside a function the output 
#result from the code that you wrote for that function will be stored as the function it self
#so after saving the function in a variable the output generated by the funcion can now be used easily

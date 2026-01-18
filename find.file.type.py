def get_type(file):
    filetype = file.split(".")
    filename, fileextn = filetype
    #print (filename)
    #print (fileextn)
    fileextn = fileextn.upper()
    if fileextn == "PDF":
       return "PDF"
    elif fileextn == "DOC":
       return "Word"
    else:
        return "Image"
      


# ----------------------------------------------#
#      Do not modify the test code below        #
# ----------------------------------------------#


def validate(expected, actual):
    assert actual == expected, f"File -> expected {expected} got {actual}"


result = get_type("resume.pdf")
validate(expected="PDF", actual=result)

result = get_type("report.doc")
validate(expected="Word", actual=result)

result = get_type("profile.png")
validate(expected="Image", actual=result)

result = get_type("profile.jpg")
validate(expected="Image", actual=result)

result = get_type("profile.jpeg")
validate(expected="Image", actual=result)

result = get_type("profile.gif")
validate(expected="Image", actual=result)
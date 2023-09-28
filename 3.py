def my_XML_Generator(input, i=0):
    if i >= len(input):
        return ""

    xml = f"{i * '  '}<{input[i]}>\n"
    xml += my_XML_Generator(input, i + 1)
    xml += f"{i * '  '}</{input[i]}>\n"

    return xml

data = ['a', 'b', 'c', 'd', 'e', 'f']
xml = my_XML_Generator(data)
print(xml)

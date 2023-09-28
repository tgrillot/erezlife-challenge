test_data = '<html><body><div><a></a></div></body></html>'
# test_data = '<html><body><div></a></body></html>'
# test_data = '<html><body><div><a></div></a>'


class MyHtmlParser:
    def __init__(self,input):
        self.beginning = ''
        self.end = ''
        self.indentlevel = 0
        self.error = ''
        self.parseHTML(input)

    def parseTag(self,input,start):
        tag = ''
        i = start
        while i < len(input):
            tag += input[i]
            if input[i] == '>':
                break
            i += 1
        return tag, i


    def parseHTML(self,input):
        starttag = ''
        endtag = ''
        inner_content_start = -1
        inner_content_end = -1

        i = 0

        while i < len(input):
            if input[i] == '<':
                if i + 1 < len(input) and input[i + 1] != '/':
                    if starttag == '':
                        starttag, inner_content_start = self.parseTag(input,i)
                elif i + 1 < len(input) and input[i + 1] == '/':
                    endtag, inner_content_end = self.parseTag(input,i)
                    if starttag.strip("</>") != endtag.strip("</>"):
                        endtag = ''
                    else:
                        break
            i += 1

        if endtag == '' or starttag == '':
            self.error = "Error: Invalid html."
            return

        self.beginning += (self.indentlevel * '  ') + starttag + '\n'
        self.end = '\n' + (self.indentlevel * '  ') + endtag + self.end
        self.indentlevel += 1
        inner_content = input[inner_content_start + 1:inner_content_end - len(endtag) + 1]
        if len(inner_content) > 3:
            self.parseHTML(inner_content)       

    @property
    def output(self):
        if self.error == '':
            return self.beginning + self.end
        else:
            return self.error

mhp = MyHtmlParser(test_data)
print(mhp.output)
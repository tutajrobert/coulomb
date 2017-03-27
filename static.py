import os
from shutil import copyfile

class Website():
    def __init__(self, directory):
        self.directory = directory
        self.pages = []
        self.html_names = []
        self.menu_sep = '&nbsp;&nbsp; // &nbsp;&nbsp;'

        if not os.path.exists(self.directory):
            os.makedirs(self.directory)
        
    def style(self, css_file):
        self.style_file = css_file
        if os.path.exists(self.directory + os.sep + self.style_file) is True:
            pass
        else:
            copyfile('default.css', self.directory + os.sep + self.style_file)
        return self.style_file        
    
    def menu_sep(self, sep):
        self.menu_sep = sep
        return self.menu_sep
	
    def title(self, title):
        title_string = '<!DOCTYPE html>\n\
<html>\n\
<head>\n\
    <meta charset="utf-8">\n\
    <meta name="viewport" content="width=device-width, initial-scale=1">\n\
    <title>{}</title>\n\
    <link rel="stylesheet" href="{}">\n\
</head>\n\
<body>\n'.format(title, self.style_file)
        self.title = title_string
        return self.title
        
    def header(self, head, aside):
        header_string = '<header>\n\
    <h1>{}</h1>\n\
    <center>\n\
    <aside>{}</aside>\n\
    </center>\n\
</header>\n'.format(head, aside)
        self.header = header_string
        return self.header
    
    def menu(self, menu_items):
        menu_string = '<menu>'
        for i in menu_items:
            if i != menu_items[-1]:
                menu_string += '\n\
    <a href="{}">{}</a>{}'.format(i[0], i[1], self.menu_sep)
            else:
               menu_string += '\n\
    <a href="{}">{}</a>'.format(i[0], i[1])
        menu_string += '\n</menu>'
        self.menu = menu_string
        return self.menu
    
    def footer(self, foot):
        footer_string = '<footer>{}</footer>'.format(foot)
        self.footer = footer_string
        return self.footer
    
    def page(self, html_name, content):
        page_string = '{}'.format(content)
        self.pages.append(page_string)
        self.html_names.append(html_name)
        return True
    
    def publish(self):
        for i in range(len(self.html_names)):
            page = open(self.directory + os.sep + self.html_names[i], 'w+')
            page.write(self.title)
            page.write(self.header)
            page.write(self.menu)
            page.write(self.pages[i])
            page.write(self.footer)
            page.close()
        return True
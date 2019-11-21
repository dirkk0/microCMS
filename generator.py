# via http://stackoverflow.com/questions/9320370/markdown-to-html-using-a-specified-css
import markdown2
import os, sys

import time

# change this to the name of the folder with your markdown files and templates
SITE="example-site"

import os

def generate(file_in, file_out, folder_templates):
    output = open(os.path.join(folder_templates, "header.html")).read()

    mkin = open(file_in)
    # output += markdown2.markdown(mkin.read(), extras=["markdown-in-html","target-blank-links"])
    output += markdown2.markdown(mkin.read(), extras=["markdown-in-html"])
 
    output += open(os.path.join(folder_templates, "footer.html")).read()
    output += markdown2.markdown(mkin.read().replace("#TIMESTAMP", time.asctime()))
    output = output.replace("#TIMESTAMP", time.asctime())

    outfile = open(file_out, 'w')
    outfile.write(output)
    outfile.close()



from distutils.dir_util import copy_tree

# copy assets from both site and templates
if os.path.exists(os.path.join(SITE, "templates", "assets")):
    copy_tree(os.path.join(SITE, "templates", "assets"), os.path.join(SITE, "output", "assets"))
copy_tree(os.path.join(SITE, "input", "assets"), os.path.join(SITE, "output", "assets"))

for file in os.listdir(os.path.join(SITE, "input")):
    if file.endswith(".md"):
        file_in = os.path.join(SITE, "input", file)
        file_out = os.path.join(SITE, "output", file[:-3] + ".html")
        folder_templates = os.path.join(SITE, "templates")
        print(file_in, file_out, folder_templates)
        generate(file_in, file_out, folder_templates)

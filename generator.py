

# via http://stackoverflow.com/questions/9320370/markdown-to-html-using-a-specified-css
import markdown2
import os, sys

import time

output = open(sys.argv[3] + "/header.html").read()

mkin = open(sys.argv[1])
# output += markdown2.markdown(mkin.read(), extras=["markdown-in-html","target-blank-links"])
output += markdown2.markdown(mkin.read(), extras=["markdown-in-html"])

mkin = open(sys.argv[3] + "/footer.html")
output += markdown2.markdown(mkin.read().replace("#TIMESTAMP", time.asctime()))


outfile = open(sys.argv[2], 'w')
outfile.write(output)
outfile.close()


# via http://stackoverflow.com/questions/9320370/markdown-to-html-using-a-specified-css
import markdown2
import os, sys

import time

output = """<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <style type="text/css">
"""

cssin = open(sys.argv[2])
output += cssin.read()

output += """
    </style>
</head>

<body>
<div class="container" markdown="1"><div class="row" markdown="1"><div class="col-12" markdown="1">
"""
mkin = open(sys.argv[1])
output += markdown2.markdown(mkin.read(), extras=["markdown-in-html"])

mkin = open("input/footer.html")
output += markdown2.markdown(mkin.read().replace("#TIMESTAMP", time.asctime()))

output += """</div></div></div>
</body>

</html>
"""

outfile = open(sys.argv[3], 'w')
outfile.write(output)
outfile.close()
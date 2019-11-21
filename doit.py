
import generator


SITE="example-site"

import os
for file in os.listdir(os.path.join(SITE, "input")):
    if file.endswith(".md"):
        print(os.path.join(SITE, "input", file))


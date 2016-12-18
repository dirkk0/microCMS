# microCMS

I created several content management systems in the past, but this is the most minimal one and pain free that I could come up with.
I use it to create my [personal website](http://curious-electric.com).

I stumbled upon this [HN thread](https://news.ycombinator.com/item?id=13009080) and realized it might be useful for other people, too.

# Installation

You need Python 2.7x installed (but it should also work with 3.x). Just download or clone it, and change the files in 'example-site/input' accordingly.

Then run ```doit.sh```.

# Configuration

To create a site, you provide a couple of markdown files that will be converted to HTML files.

The doit.sh script creates HTML pages in the output folder from all files in the input folder. It expects the three folders 'input', 'output' and 'templates'.
To point to a specific site, change the first line in the doit.sh script.


For extra measure, the ```do_ftp.sh``` script (that you derive from the template) uploads the 'output' folder to your provider.

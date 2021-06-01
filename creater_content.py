import re
import codecs
import os


filename = r'_posts\2021-06-01-handbook-git.markdown'

heads = []
with codecs.open(filename, 'r', 'utf-8') as f:
    
    for line in f.readlines():
        if re.match("^#\ ", line):
            heads.append(line)  

FILTER = [
    "\n",
    "\r",
    "&lt;",
    "&gt;",
    "'",
    ">",
    "<",
    "**",
    "#"
]

def STRFILTER(text):
    for i in FILTER:
        text = text.replace(i, '')
    return text

with codecs.open(os.path.basename(filename) + ".contents", 'w', 'utf-8') as f:
    for i, head in enumerate(heads):
        head = STRFILTER(head)
        final = " ".join(re.findall("\S+", head))
        
        f.write("- '{}'\n".format(final))
        print("%3d %s" % (i, final))



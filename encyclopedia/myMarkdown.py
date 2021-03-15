import re
pp = re.compile('(^<li>.*</li>)', re.M | re.DOTALL)
def convert(txt):
    # collect matches in iterator
    iterators = iters(txt)
    for i in range(10):
        for it in iterators[i]:
            if i == 0:
                grp = " " + it.group() # this is only for <p></p> not to omit the first letter in a new line
            else:
                grp = it.group()
            txt = txt.replace(it.group(), compilers[i].sub(subs[i], grp))
    txt = pp.sub(r'<ul>\n\1\n</ul>', txt)
    return txt

def iters(txt):
    it = []    
    for i in range(10):
        it.append(compilers[i].finditer(txt))
    return it

# link
p = re.compile("""
    \[                    # match [ at the start
    ([^\[|\]]*)           # group to be included, and do not include [] in the middle
    \]                    # match ] at the end
    \(                    # match ( at the start
    ([^\(|\)]*)           # group to be included, and do not include () in the middle
    \)                    # match ) at the end
    """, re.VERBOSE | re.M)

# bold
p1 = re.compile("""
    \*\*                    # match ** at the start
    ([^**]*)                # group to be included, and do not include ** in the middle
    \*\*                    # match ** at the end
    """, re.VERBOSE | re.M)

# heading
p21 = re.compile('^#{1,1}\s+(.*)', re.M)
p22 = re.compile('^#{2,2}\s+(.*)', re.M)
p23 = re.compile('^#{3,3}\s+(.*)', re.M)
p24 = re.compile('^#{4,4}\s+(.*)', re.M)
p25 = re.compile('^#{5,5}\s+(.*)', re.M)
p26 = re.compile('^#{6,6}\s+(.*)', re.M)

# unordered list
p3 = re.compile('^\*\s+(.*)', re.M)

# paragraph
p4 = re.compile('^[^#|*|\[|\n]([^\s*].+)', re.M)

compilers = [p4, p, p1, p26, p25, p24, p23, p22, p21, p3]

# HTML tags to be substituted
subs = [r'<p>\1</p>', r'<a href="\2">\1</a>', r'<b>\1</b>', r'<h6>\1</h6>', 
        r'<h5>\1</h5>', r'<h4>\1</h4>', r'<h3>\1</h3>', r'<h2>\1</h2>', 
        r'<h1>\1</h1>', r'<li>\1</li>']
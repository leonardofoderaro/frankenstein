import re
from frankie import frankiefun

@frankiefun("simple") 
def transform(**kwargs):
    doc = kwargs['doc']
    find = kwargs['find']
    replace = kwargs['replace']
    result = re.sub(find, replace, doc, re.MULTILINE)
    return result



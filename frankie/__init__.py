import lxml
from lxml import html
from lxml import etree

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

transformations = {}

class FrankieFunction(object):
    def __init__(self, function, name):
        transformations[name] = function 
        self.name = name
        self.function = function

    def __call__(self, **kwargs):
        # Here the code returning the correct thing.
        return self.function(**kwargs)

def frankiefun(name):
    def _cache(function):
        return FrankieFunction(function, name)
    return _cache



def _htmlParse(html, parseAsHtml=True):
    if parseAsHtml:
        parser = etree.HTMLParser(encoding='utf-8')
        tree   = etree.parse(StringIO(html), parser)
    else:
        tree   = etree.parse(StringIO(html))
    return tree

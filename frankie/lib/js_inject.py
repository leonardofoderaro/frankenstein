import re
from lxml import etree
from frankie import frankiefun, _htmlParse

@frankiefun("InjectRemoteJS")
def _injectRemoteJS(doc, **kwargs):
    url = kwargs['url']
    parsedDoc = _htmlParse(doc)
    element = parsedDoc.find('//head')
    element.insert(0, etree.fromstring('<script src="' + url + '"></script>'))
    doc = etree.tostring(parsedDoc, pretty_print=True, method="html")
    return doc.decode("utf-8")


@frankiefun('ActivateVueJS')
def _activateVueJS(doc, **kwargs):
    vueSrc = "<script>var app = new Vue({el: '#" + kwargs['el'] + "'});</script>"
    doc = re.sub('</body>', vueSrc + "</body>", doc)

    return doc

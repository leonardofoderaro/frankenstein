import os
import pandas as pd
from lxml import html, etree
from frankie import frankiefun, _htmlParse, transformations

@frankiefun("XPathRemove")
def _XPathRemove(doc, **kwargs):
    xpath = kwargs['xpath']

    parsedDoc = _htmlParse(doc)

    element = parsedDoc.find(xpath)

    if element is None:
       return doc

    element.clear()

    doc = etree.tostring(parsedDoc, pretty_print=True, method="html")

    return doc.decode("utf-8")


@frankiefun("XPathReplace")
def _XPathReplace(doc, **kwargs):
    XPathFind = kwargs['find']
    replace  = kwargs['replace']

    parsedDoc = _htmlParse(doc)
    element = parsedDoc.find(XPathFind)
    if element is not None:
        element.clear()
        element.append(etree.fromstring(replace))
        doc = etree.tostring(parsedDoc, pretty_print=True, method="html")
        return doc.decode("utf-8")
    else:
        return doc


@frankiefun("XPathCopyFromRemote")
def _XPathCopyFromRemote(doc, **kwargs):
    origin = kwargs['origin']
    XPathSource = kwargs['XPathSource']
    XPathDest = kwargs['XPathDest']
    parsedDoc = _htmlParse(doc)
    sourceDoc = _htmlParse(requests.get(origin).text)
    element = sourceDoc.find(XPathSource)
    elementDest = parsedDoc.find(XPathDest)
    elementDest.clear()
    elementDest.append(element)
    doc = etree.tostring(parsedDoc, pretty_print=True, method="html")
    return doc.decode("utf-8")


@frankiefun("XPathCopyFromLocal")
def _XPathCopyFromLocal(doc, **kwargs):
    origin = kwargs['origin']
    XPathSource = kwargs['XPathSource']
    XPathDest = kwargs['XPathDest']

    if 'position' in kwargs:
        position = kwargs['position'] 
    else:
        position = "AddBefore"

    path = os.getcwd() + '/fragments/' + origin
    sourceDoc = _htmlParse(open(path).read(), parseAsHtml=False)
    parsedDoc = _htmlParse(doc)
    element = sourceDoc.xpath(XPathSource) #[0].getchildren()
    elementDest = parsedDoc.xpath(XPathDest)

    if elementDest is not None and elementDest != []:
       elementDest = elementDest[0]
    else:
       return doc

    if element != None and element != []:
        if position == 'AddBefore':
            i = 1
            for e in element:
                elementDest.getparent().insert(elementDest.getparent().index(elementDest), e)
                i = i + 1
        elif position == 'AddLast':
            for e in element:
                elementDest.append(e)

    doc = etree.tostring(parsedDoc, pretty_print=True, method="html")

    return doc.decode("utf-8")


@frankiefun("XPathSetText")
def _XPathSetText(doc, **kwargs):
    XPathFind = kwargs['XPathFind']
    text = kwargs['text']
    parsedDoc = _htmlParse(doc)
    element = parsedDoc.find(XPathFind)
    if element is not None:
        element.clear()

        fragments = html.fragments_fromstring(text)
        last = None

        for frag in fragments:
          if isinstance(frag, lxml.etree._Element):
            element.append(frag)
            last = frag
          else:
            if last:
              last.tail = frag
            else:
              element.text = frag


        doc = etree.tostring(parsedDoc, pretty_print=True, method="html")
        return doc.decode("utf-8")
    else:
        return doc


@frankiefun("AppendLast")
def _XPathAppendLast(doc, **kwargs):
    kwargs['position'] = 'AddLast'
    print(kwargs)
    return transformations['XPathCopyFromLocal'](doc, **kwargs)


@frankiefun("XPathToDataFrame")
def _XPathToDataFrame(doc, **kwargs):
    name = kwargs["name"]
    dataframeDescriptor  = kwargs["DataFrame"]

    sourceDoc = _htmlParse(doc)

    data = {}

    schema = dataframeDescriptor['schema']

    for field in schema.keys():
        data[field] = sourceDoc.xpath(schema[field])

    kwargs['ctx']['df'] = pd.DataFrame(data)

    return doc

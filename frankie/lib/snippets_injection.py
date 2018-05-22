import os
import re
import unidecode
from frankie import frankiefun

@frankiefun("StaticSnippetInject")
def staticInject(doc, **kwargs):
    name = unidecode.unidecode(patch['name'])
    name = re.sub(' ', '-', name)
    path = os.path.abspath('snippets') + '/' + name

    if not os.path.exists(path):
        os.makedirs(path)

        subdirs = ['html', 'css', 'js']

        for subdir in subdirs:
            if not os.path.exists(path + '/' + subdir):
                os.makedirs(path + '/' + subdir)

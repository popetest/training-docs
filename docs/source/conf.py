from recommonmark.parser import CommonMarkParser

source_parsers = {
    '.md': CommonMarkParser,
}

source_suffix = ['.rst', '.md']

extensions = ['sphinx.ext.graphviz']

import sys, os
sys.path.append(os.path.abspath('exts'))
extensions = ['foo']

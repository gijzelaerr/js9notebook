js9notebook
===========

Embed JS9 (the javascript version of DS9 (the astronomical image viewer))
inside Jupyter.

[![Build Status](https://travis-ci.org/gijzelaerr/js9notebook.svg)](https://travis-ci.org/gijzelaerr/js9notebook)

[![Gitter](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/gijzelaerr/js9notebook?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)

**note** For now this project doens't do much, I still need to figure out what is the best way to actually integrate JS9 into ipython. For the meanwhile you can already use JS9 in your notebook by copy pasting this code into a cell:

```
%%html
<div class="JS9Menubar"></div>
<div class="JS9"></div>
<link type="text/css" rel="stylesheet" href="http://js9.si.edu/js9/js9-allinone.css">
<script type="text/javascript" src="http://js9.si.edu/js9/js9-allinone.js"></script>
```


install
=======

From source:
```
$ python setup.py install
```

Or with pip:
```
$ pip install js9notebook
```

usage
=====
```
import js9notebook
js9notebook.initialize()
```

examples
========

https://github.com/gijzelaerr/js9notebook/tree/master/example

links
=====

 * https://github.com/ericmandel/js9
 * http://ds9.si.edu/site/Home.html
 * https://jupyter.org/


license
=======

MIT

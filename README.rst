tw2.jqplugins.elfinder
======================

:Author: Joseph Tate <jtate@dragonstrider.com>

.. comment: split here

.. _toscawidgets2 (tw2): http://toscawidgets.org/documentation/tw2.core/
.. _jQuery UI: http://jqueryui.com/
.. _jQuery: http://jquery.com/
.. _elFinder: http://elrte.org/elfinder/

tw2.jqplugins.elfinder is a `toscawidgets2 (tw2)`_ wrapper for `elFinder`_.

Live Demo
---------
.. comment: Peep the `live demonstration <http://tw2-demos.threebean.org/module?module=tw2.jqplugins.elfinder>`_.

Links
-----
Get the `source from github <http://github.org/toscawidgets/tw2.jqplugins.elfinder>`_.

`PyPI page <http://pypi.python.org/pypi/tw2.jqplugins.elfinder>`_
and `bugs <http://github.org/toscawidgets/tw2.jqplugins.elfinder/issues>`_

Description
-----------

`toscawidgets2 (tw2)`_ aims to be a practical and useful widgets framework
that helps people build interactive websites with compelling features, faster
and easier. Widgets are re-usable web components that can include a template,
server-side code and JavaScripts/CSS resources. The library aims to be:
flexible, reliable, documented, performant, and as simple as possible.

`jQuery`_ is a fast and concise JavaScript Library that simplifies HTML
document traversing, event handling, animating, and Ajax interactions
for rapid web development. jQuery is designed to change the way that
you write JavaScript.

`elFinder`_ is an open-source file manager for web, written in JavaScript using
jQuery UI.  It is inspired by Finder in Mac OS X.

The main goal of the file manager is to let you work with remote files with
the same convenience as on your own computer.

This module, tw2.jqplugins.elfinder, provides `toscawidgets2 (tw2)`_ access to the
`elFinder`_ widget.

Sampling tw2.jqplugins.elfinder in the WidgetBrowser
----------------------------------------------------

The best way to scope out ``tw2.jqplugins.elfinder`` is to load its widgets in the
``tw2.devtools`` WidgetBrowser.  To see the source code that configures them,
check out ``tw2.jqplugins.elfinder/tw2/jqplugins/elfinder/samples.py``

To give it a try you'll need git, python, and `virtualenvwrapper
<http://pypi.python.org/pypi/virtualenvwrapper>`_.  Run::

    $ git clone git://github.com/toscawidgets/tw2.jqplugins.elfinder.git
    $ cd tw2.jqplugins.elfinder
    $ mkvirtualenv tw2.jqplugins.elfinder
    (tw2.jqplugins.elfinder) $ pip install tw2.devtools
    (tw2.jqplugins.elfinder) $ python setup.py develop
    (tw2.jqplugins.elfinder) $ paster tw2.browser

...and browse to http://localhost:8000/ to check it out.

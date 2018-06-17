=======================
plonetheme.armadillotec
=======================


Introduction
============

*plonetheme.armadillotec* package uses the *theming & packaging* features
available in `plone.app.theming`_ to make a theme for the 
`Armadillo Integración Tecnológica C.A.`_ Website with Plone_.

.. image:: https://raw.github.com/macagua/plonetheme.armadillotec/master/plonetheme/armadillotec/static/preview.png


Requirements
============

- From the Plone 4.1.x To the Plone 4.3 latest versión (https://plone.org/download)
- The ``plone.app.theming`` package (*will be installed as a dependency of this package*)


Features
========

- It's an installable Plone_ Theme package.
- After installation from Add-ons controlpanel, this theme is enabled automatically.
- Also it's a simple Diazo_ package (Zip file).
- It's have support for clean uninstallation.


Installation
============


Zipfile
-------

If you are an **end user**, you might enjoy installation via zip file import.

1. Download the `zip file <https://github.com/macagua/plonetheme.armadillotec/raw/master/armadillotec.zip>`_.
2. Import the theme from the Diazo theme control panel.


Buildout
--------

If you are a **developer user**, you might enjoy installing it via buildout.

For install ``plonetheme.armadillotec`` package add it to your ``buildout`` section's 
*eggs* parameter e.g.: ::

   [buildout]
    ...
    eggs =
        ...
        plonetheme.armadillotec


and then running ``bin/buildout``.

Or, you can add it as a dependency on your own product ``setup.py`` file: ::

    install_requires=[
        ...
        'plonetheme.armadillotec',
    ],


Enabling the theme
^^^^^^^^^^^^^^^^^^

Browse to ``http://yoursite/Plone/@@theming-controlpanel`` click on ``Enable`` on 
``ArmadilloTec`` theme from the Diazo control panel. That's it!


Contribute
==========

- Issue Tracker: https://github.com/macagua/plonetheme.armadillotec/issues
- Source Code: https://github.com/macagua/plonetheme.armadillotec


License
=======

This package is licensed under the GPL Version 2.


Credits
-------

- Leonardo J. Caballero G. (leonardocaballero at gmail dot com).


.. _`Plone`: http://plone.org
.. _`plone.app.theming`: https://pypi.org/project/plone.app.theming/
.. _`Diazo`: http://diazo.org
.. _`Armadillo Integración Tecnológica C.A.`: http://armadillotec.com/

.. vim: set fileencoding=utf-8 :
.. @author: Manuel Guenther <Manuel.Guenther@idiap.ch>
.. @date:   Fri Oct 31 16:01:33 CET 2014

==============
 User's Guide
==============

This package contains the access API and descriptions for the BioSecure_ database.
The actual raw data for the database should be downloaded from the original URL.
This API is only compatible with the DS2 Still face image part of the BioSecure_ database.

This package only contains the Bob_ accessor methods to use the DB directly from python.


The Database Interface
----------------------

The :py:class:`bob.db.biosecure.Database`  complies with the standard biometric verification database as described in `bob.db.base <bob.db.base>`, implementing the interface :py:class:`bob.db.base.SQLiteDatabase`.

.. todo::
   Explain the particularities of the :py:class:`bob.db.biosecure.Database` database.


.. _biosecure: http://biosecure.it-sudparis.eu/AB
.. _bob: https://www.idiap.ch/software/bob

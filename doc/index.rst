.. vim: set fileencoding=utf-8 :
.. @author: Manuel Guenther <Manuel.Guenther@idiap.ch>
.. @date:   Tue Aug 26 09:42:18 CEST 2014

.. _bob.db.biosecure:

===========================================
 BioSecure Database Verification Protocols
===========================================

.. todolist::

Documentation
-------------

This package contains the face verification protocol for the DS2 Still face image part of the BioSecure database.
The images themselves are not provided in this package, they can be obtained via: http://biosecure.it-sudparis.eu/AB

Included in this package, there are eye annotations that were automatically detected using the `VeriLook SDK 4.0 from Neurotechnology <http://www.neurotechnology.com/verilook.html>`_.
When you use the annotations in a scientific publication, please cite::

  @INPROCEEDINGS {marta14FaceBF,
    author = {M. Gomez-Barrero and C. Rathgeb and J. Galbally and J. Fierrez and C. Busch},
    title = {Protected Facial Biometric Templates Based on Local Gabor Patterns and Adaptive Bloom Filters},
    booktitle = {Proc. IAPR/IEEE Int. Conf. on Pattern Recognition, ICPR},
    month = {August},
    pages = {4483-4488},
    year = {2014},
  }




.. toctree::
   :maxdepth: 2

   guide
   py_api

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


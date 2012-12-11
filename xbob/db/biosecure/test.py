#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Laurent El Shafey <laurent.el-shafey@idiap.ch>
#
# Copyright (C) 2011-2012 Idiap Research Institute, Martigny, Switzerland
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""A few checks at the Biosecure database.
"""

import os, sys
import unittest
import xbob.db.biosecure

class BiosecureDatabaseTest(unittest.TestCase):
  """Performs various tests on the Biosecure database."""

  def test01_clients(self):
    # test that the clients() function returns reasonable output
    db = xbob.db.biosecure.Database()

    self.assertEqual(len(db.clients()), 210)
    # TODO: more specific tests

  def test02_objects(self):
    # test that the objects() function returns reasonable output
    db = xbob.db.biosecure.Database()

    self.assertEqual(len(db.objects()), 2520)
    # TODO: more specific tests


  def test03_driver_api(self):

    from bob.db.script.dbmanage import main

    self.assertEqual(main('biosecure dumplist --self-test'.split()), 0)
    self.assertEqual(main('biosecure dumplist --protocol=ca0 --class=client --group=dev --purpose=enrol --client=141 --self-test'.split()), 0)
    self.assertEqual(main('biosecure checkfiles --self-test'.split()), 0)
    self.assertEqual(main('biosecure reverse ca0/u141_s02_face_ds2-ca-0i_02 --self-test'.split()), 0)
    self.assertEqual(main('biosecure path 748 --self-test'.split()), 0)


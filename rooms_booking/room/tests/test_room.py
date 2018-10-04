# This file is a part of the AnyBlok / book examples project
#
#    Copyright (C) 2018 Pierre Verkest <pverkest@anybox.fr>
#
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file,You can
# obtain one at http://mozilla.org/MPL/2.0/.

from anyblok.tests.testcase import BlokTestCase


class TestRoom(BlokTestCase):
    """ Test python api on AnyBlok models"""

    def test_create_room(self):
        room_count = self.registry.Room.query().count()
        room = self.registry.Room.insert(
            name="A1",
            capacity=25,
        )
        self.assertEqual(
            self.registry.Room.query().count(),
            room_count + 1
        )
        self.assertEqual(
            room.name,
            "A1"
        )
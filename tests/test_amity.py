from unittest import TestCase

import mock



class TestAmityClass(TestCase):
    def setUp(self):
        self.amity = Amity()

    def test_default_values(self):
        self.assertEqual(0,
                         len(self.amity.get_unallocated_people()),
                         msg="The unallocated fellows and staff should be 0 on creation of Amity Object")

        self.assertEqual(
            0,
            len(self.amity.get_rooms()['offices']['available']) + len(self.amity.get_rooms()['offices']['unavailable'])
            ,
            msg="The available and unavailable offices should be 0 on creating new amity object"
        )

        self.assertEqual(
            0,
            len(self.amity.get_rooms()['living_spaces']['available']) + len(
                self.amity.get_rooms()['living_spaces']['unavailable'])
            ,
            msg="The available and unavailable living rooms should be empty on creating new amity object"
        )

    @mock.patch.dict('amity.amity.Amity.offices', {'available': [OfficeSpace('Summer')], 'unavailable': []})
    @mock.patch.dict('amity.amity.Amity.living_spaces', {'available': [LivingSpace('Shell')], 'unavailable': []})
    def test_create_fellow(self):
        self.amity.create_fellow(first_name="John", other_name="Dow", accomodation='Y')
        self.amity.create_fellow(first_name="Brian", other_name="Kimani")

        self.assertEqual(2,
                         len(self.amity.get_rooms()['offices']['available'][0].get_allocations()),
                         msg="Two fellows should be assigned to the Summer Office Space")
        self.assertEqual(1,
                         len(self.amity.get_rooms()['living_spaces']['available'][0].get_allocations()),
                         msg="One Fellow should be assigned a Living Space at Shell")

    @mock.patch.dict('amity.amity.Amity.offices', {'available': [OfficeSpace('Summer'), OfficeSpace('Winter')]})
    @mock.patch.dict('amity.amity.Amity.living_spaces', {'available': [LivingSpace('Shell'), LivingSpace('Perl')]})
    def test_create_rooms(self):
        self.assertItemsEqual(["Summer", "Winter"],
                              [office.get_name() for office in self.amity.get_rooms()['offices']['available']],
                              msg="Offices in Amity should be Summer and Winter")
        self.assertItemsEqual(["Shell", "Perl"],
                              [living_space.get_name() for living_space in
                               self.amity.get_rooms()['living_spaces']['available']],
                              msg="Living Spaces in Amity should be Shell and Perl")

        self.assertEqual('Room Exists', self.amity.create_office("Summer"),
                         msg='Office name should be unique ')

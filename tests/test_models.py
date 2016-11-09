import unittest


class StaffClassTest(unittest.TestCase):
    def test_staff_name(self):
        staff_name = "John Doe"
        staff = Staff()

        staff.set_name(staff_name)

        self.assertEqual(staff_name, staff.get_name(),
                         msg="Staff name should be {0}".format(staff_name))

    def test_staff_office_allocation(self):
        staff_name = "John Doe"
        office_space = "Hogwarts"

        staff = Staff(name=staff_name, office_space=office_space)

        self.assertListEqual([staff_name, office_space],
                             [staff.get_name(), staff.get_allocated_office()],
                             msg="Staff {0} should be assigned office space at {1}".format(staff_name, office_space))

        self.assertTrue(staff.is_assigned(),
                        msg="is_assigned function should be True when staff is allocated space")


class FellowClassTest(unittest.TestCase):
    def test_fellow_name(self):
        fellow_name = "Brian Test"
        fellow = Fellow()

        fellow.set_name(fellow_name)

        self.assertEqual(fellow_name, fellow.get_name(),
                         msg="The Fellow name should be Brian Test")

    def test_allocated_office_and_living_space(self):
        office_space = "Hogwarts"
        living_space = "PHP"
        fellow = Fellow()

        fellow.set_allocated_office_space(office_space)
        fellow.set_allocated_living_space(living_space)

        self.assertListEqual([office_space, living_space],
                             [fellow.get_allocated_office_space(),
                              fellow.get_allocated_living_space()],
                             msg="Fellow should be assigned Hogwarts Office and PHP living space")


class LivingSpaceClassTest(unittest.TestCase):

    def test_raise_error_assign_staff_to_living_space(self):
        staff = Staff(name="John Staff", id="1")
        living_space = LivingSpace("Shell")

        self.assertRaises(ValueError,
                          living_space.set_allocate_person, staff,
                          msg="A Staff member cannot be allocated Living Space"
                          )


class AmityClassTest(unittest.TestCase):

    def setUp(self):

        self.amity = Amity()

        office_list= [Office("Camelot"), Office("Valhala")]
        living_space_list = [LivingSpace("Orange"), LivingSpace("Blue")]

        self.amity.offices = {}
        self.amity.living_spaces = {}
        for office in office_list:
            self.amity.offices[office.get_name()] = office

        for living_space in living_space_list:
            self.amity.living_spaces[living_space.get_name()] = living_space

    def test_raise_error_on_allocate_non_existing_room(self):
        self.assertRaises(ValueError, self.amity.allocate_room, ("SHELL", 1),
                          msg="a peron should not allocate space in non existing rooom")

    




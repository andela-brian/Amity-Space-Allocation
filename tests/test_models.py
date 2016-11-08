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

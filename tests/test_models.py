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


class RoomClassTest(unittest.TestCase):

    def test_create_new_room(self):
        pass

    def test_allocate_person_to_room(self):
        pass

    def test_get_allocated_users(self):
        pass

    def test_raise_value_error_on_allocate_nonexisitng_room(self):
        pass


class OfficeClassTest(unittest.TestCase):

    def test_office_allocate_max_four_persons(self):
        pass

    def test_raise_error_on_assigning_full_office(self):
        pass

    def test_allocate_staff_to_office(self):
        pass

    def test_allocate_fellow_to_office(self):
        pass


class LivingClassTest(unittest.TestCase):

    def test_raise_error_allocate_staff_to_living_space(self):
        pass

    def test_raise_error_on_allocate_more_than_six_fellows(self):
        pass


class AmityClassTest(unittest.TestCase):

    def test_relocate_person(self):
        pass

    def test_raise_error_on_allocate_non_existing_room(self):
        pass

    def test_get_room_allocations(self):
        pass

    def test_get_unallocated_persons(self):
        pass


import unittest


class PersonClassTest(unittest.TestCase):
    pass


class StaffClassTest(unittest.TestCase):
    pass


class FellowClassTest(unittest.TestCase):

    def setUp(self):
        self.fellow_default = Fellow("Brian Test")

    def test_fellow_is_subclass_of_person(self):
        self.assertIsInstance(Fellow(), Person,
                              msg="Fellow class should be subclass of Person")

    def test_fellow_get_name(self):
        self.assertEqual("Brian Test", self.fellow_default.get_name(),
                         msg="The Fellow name should be Brian Test")

    def test_default_is_fellow(self):
        self.assertEqual(True, self.fellow_default.is_fellow(),
                         msg="The is_fellow function should be true for Fellow class")

    def test_default_accomodation_is_false(self):
        self.assertEqual(False, self.fellow_default.needs_accomodation(),
                         msg="Fellow should not require accomodation when created ")

    def test_default_is_allocated_living_space(self):
        self.assertEqual(False, self.fellow_default.is_allocated_living_space(),
                         msg="Fellow should not be allocated Living Space when created")

    def test_default_is_allocated_office_space(self):
        self.assertEqual(False, self.fellow_default.is_allocated_living_space(),
                         msg="Fellow should not be allocated Office Space when created")

    def test_default_set_allocated_office_and_living_space(self):
        office_space = "Hogwarts"
        living_space = "PHP"
        self.fellow_default.set_allocated_office_space(office_space)
        self.fellow_default.set_allocated_living_space(living_space)

        self.assertListEqual([office_space, living_space],
                             [self.fellow_default.get_allocated_office_space(),
                              self.fellow_default.get_allocated_living_space()],
                             msg="Fellow should be assigned Hogwarts Office and PHP living space")

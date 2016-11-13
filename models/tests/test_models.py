from unittest import TestCase


class TestPersonClass(TestCase):

    def setUp(self):
        self.name = "John Doe"
        self.id = "FE01"

    def test_error_creating_person_object(self):
        self.assertRaises(ValueError, Person(id=self.id),
                          msg="A person object cannot be created without id")
        self.assertRaises(ValueError, Person(name=self.name),
                          msg="A person cannot be created with a name")


class TestFellowCLass(TestCase):
    def setUp(self):
        self.name = "John Doe"
        self.id = "FE01"
        self.fellow = Fellow(id=self.id, name=self.name)

    def test_fellow_is_subclass_of_person(self):
        self.assertIsInstance(self.fellow, Person,
                              msg="Fellow class should be a subclass of Person")

    def test_create_new_fellow_(self):

        self.assertListEqual([self.id, self.name],
                             [self.fellow.get_id, self.fellow.get_name],
                             msg="The fellow named {0} should have id {1}".format(self.name, self.id))
        self.assertEqual("FELLOW", fellow.get_role(),
                         msg="get_role functions should return 'FELLOW' for Fellow Class")


class TestStaffClass(TestCase):
    def setUp(self):
        self.name = "Jane Doe"
        self.id = "ST01"
        self.staff = Staff(id=self.id, name=self.name)

    def test_staff_is_subclass_of_person(self):
        self.assertIsInstance(self.staff, Person,
                              msg="Staff class should subclass of Person")

    def test_create_new_staff(self):
        self.assertListEqual([self.id, self.name],
                             [self, self.staff.get_id(), self.staff.get_name()],
                             msg="The Staff named {0} should have id {1}".format(self.name, self.id))
        self.assertRaises(ValueError, Staff, id=self.id, name=None,
                          msg="cannot create Staff with name as None type")


class TestLivingRoomClass(TestCase):

    def setUp(self):
        self.name = "SHELL"
        self.living_space = LivingSpace(name=self.name)

    def test_living_room_subclass_of_room(self):
        self.assertIsInstance(self.living_space, Room,
                              msg="LivingRoom class should be a subclass of Room")

    def test_living_room_capacity(self):
        self.assertEqual(4, self.living_space.get_capacity(),
                         msg="Living Space should have a total of 4 spaces")

    def test_allocating_living_space(self):
        self.assertTrue(self.living_space.is_available(),
                        msg="Living Space should be available before allocation of spaces")
        staff = Staff(id="STF01", name="John Doe")

        self.assertRaises(TypeError, self.living_space.allocate_space(staff),
                          msg="A staff member cannot be allocated Living Space")

        # create test data for fellows
        fellows = [Fellow(id=fellow_id, name="Fellow Name " + str(fellow_id)) for fellow_id in xrange(1, 6)]
        for fellow_id in xrange(4):
            self.living_space.allocate_space(fellows.pop())

        self.assertListEqual(fellows, self.living_space.get_allocations(),
                             msg="Living Space should contain four fellows after allocation")

        self.assertRaises(ValueError, self.living_space.allocate_space, fellows.pop(),
                          msg="Living space cannot be allocated to more than 4 fellows")


class TestOfficeClass(TestCase):
    def setUp(self):
        self.name = "SHELL"
        self.office_space = Office(name=self.name)

    def test_office_subclass_of_room(self):
        self.assertIsInstance(self.office_space, Room,
                              msg="LivingRoom class should be a subclass of Room")

    def test_office_room_capacity(self):
        self.assertEqual(6, self.office_space.get_capacity(),
                         msg="Office should have a total of 6 spaces ")

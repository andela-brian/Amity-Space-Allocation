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
                              msg="Fellow class should subclass of Person")

    def test_create_new_staff(self):
        self.assertListEqual([self.id, self.name],
                             [self,staff.get_id(), self.staff.get_name()],
                             msg="The Staff named {0} should have id {1}".format(self.name, self.id))


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


class TestOfficeClass(TestCase):
    def setUp(self):
        self.name = "SHELL"
        self.office_space = Office(name=self.name)

    def test_office_subclass_of_room(self):
        self.assertIsInstance(self.office_space, Room,
                              msg="LivingRoom class should be a subclass of Room")

    def test_office_romm_capacity(self):
        self.assertEqual(6, self.office_space.get_capacity(),
                         msg="Office should have a total of 6 spaces ")

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

    def test_fellow_is_subclass_of_person(self):
        fellow = Fellow(id=self.id, name=self.name)
        self.assertIsInstance(fellow, Person,
                              msg="Class Fellow should extend Person Class")

    def test_create_new_fellow_(self):
        fellow = Fellow(id=self.id, name=self.name)
        self.assertListEqual([self.id, self.name],
                             [fellow.get_id, fellow.get_name],
                             msg="The fellow named {0} should have id {1}".format(self.name, self.id))
        self.assertEqual("FELLOW", fellow.get_role(),
                         msg="get_role functions should return 'FELLOW' for Fellow Class")


class TestStaffClass(TestCase):
    def setUp(self):
        self.name = "Jane Doe"
        self.id = "ST01"

    def test_staff_is_subclass_of_person(self):
        staff = Staff(id=self.id, name=self.name)
        self.assertIsInstance(staff, Person,
                              msg="Class Fellow should extend Person Class")

    def test_create_new_staff(self):
        staff = Staff(id=self.id, name=self.name)
        self.assertListEqual([self.id, self.name],
                             [staff.get_id(), staff.get_name()],
                             msg="The Staff named {0} should have id {1}".format(self.name, self.id)))


class TestLivingRoomClass(TestCase):
    def test_living_room_subclass_of_room(self):
        pass

    def test_create_living_room_instance(self):
        pass

    def test_allocate_fellow_to_living_space(self):
        pass

    def test_allocate_staff_to_living_space(self):
        pass

    def test_error_allocate_more_than_four_persons(self):
        pass


class TestOfficeClass(TestCase):
    def test_office_subclass_room(self):
        pass

    def test_create_office_space(self):
        pass

    def test_allocate_staff_to_office(self):
        pass

    def test_allocate_fellow_to_office(self):
        pass

    def test_error_allocate_more_than_four_persons(self):
        pass

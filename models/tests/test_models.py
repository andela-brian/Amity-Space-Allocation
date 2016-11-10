
from unittest import TestCase


class TestFellowCLass(TestCase):

    def test_fellow_is_subclass_of_person(self):
        pass

    def test_create_person(self):
        pass


class TestStaffClass(TestCase):

    def test_staff_is_subclass_of_person(self):
        pass

    def test_create_staff(self):
        pass


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

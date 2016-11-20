class Person(object):

    name = None
    office = None

    def __init__(self, name=None):
        pass

    def get_name(self):
        pass

    def set_allocated_office(self, office=None):
        pass

    def get_allocated_office(self):
        pass

    def is_allocated_office(self):
        pass


class Staff(Person):
    def __init__(self, name=None):
        super(self.__class__, self).__init__(name)


class Fellow(Person):
    living_space = None

    def __init__(self, name=None):
        super(self.__class__, self).__init__(name)

    def get_allocated_living_space(self):
        pass

    def is_allocated_living_space(self):
        pass


class Room(object):
    persons_id = []
    capacity = None

    def __init__(self, name):
        self.name = name

    def is_available(self):
        pass

    def allocate_space(self, person_id=None):
        pass

    def get_allocated(self):
        pass

    def get_capacity(self):
        pass


class LivingSpace(Room):
    capacity = 4


class Office(Room):
    capacity = 6

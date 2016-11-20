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

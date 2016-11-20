class Amity(object):
    living_spaces = {
        'available': {},
        'unavailable': {},
    }

    offices = {
        'available': {},
        'unavailable': {},
    }

    fellows = {}
    staff = {}

    unallocated_persons_ids = []

    def create_office(self, office_name):
        pass

    def create_living_spaces(self, living_space_name):
        pass

    def create_fellow(self, name, accommodation='N'):
        pass

    def create_staff(self, name):
        pass

    def relocate_person(self, person_id, room_id):
        pass

    def get_rooms(self):
        pass

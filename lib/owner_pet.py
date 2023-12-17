

class Owner:

    def __init__(self, name):
        self.name = name
        self.pet_list =[]
    def pets(self):
        return self.pet_list

    def add_pet(self, pet):
        valid_pet = isinstance(pet, Pet)
        if valid_pet:
            self.pet_list.append(pet)
            pet.owner = self
            Pet.all.append(pet)
            return self.pet_list
        else:
            raise Exception ("Must be a pet.")


    def get_sorted_pets(self):
        return sorted(self.pet_list, key=lambda pet: pet.name)

'''
pet_list.map(pet => pet.name)
'''


class Pet:

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name,  pet_type, owner = None) -> None:
        if pet_type in Pet.PET_TYPES:
            self.name = name
            self.pet_type = pet_type
            self.owner = owner
            if owner is not None:
                owner.pet_list.append(self)
            Pet.all.append(self)
        else:
            raise Exception("Must be a valid pet type.")
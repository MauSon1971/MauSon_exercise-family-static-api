
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        # Inicializamos la lista con los tres miembros especificados en las instrucciones
        self._members = [
            {
                "id": self._generateId(),  # Usamos el método para generar un ID único
                "first_name": "John",
                "last_name": last_name,
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            },
            {
                "id": self._generateId(),
                "first_name": "Jane",
                "last_name": last_name,
                "age": 35,
                "lucky_numbers": [10, 14, 3]
            },
            {
                "id": self._generateId(),
                "first_name": "Jimmy",
                "last_name": last_name,
                "age": 5,
                "lucky_numbers": [1]
            }
        ]

    # Método para generar IDs únicos
    def _generateId(self):
        return randint(0, 99999999)
    

    def add_member(self, member):
        #Si no tiene ID genero uno aleatorio
        if 'id' not in member:
            member['id'] = self._generateId()
        # Agrego el apellido Jackson automáticamente
        member['last_name'] = self.last_name
        #Agrego al nuevo miembro a la lista members
        self._members.append(member)
        return member


    def delete_member(self, id):
        # Filtra la lista excluyendo al miembro con el id dado
        self._members = [member for member in self._members if member['id'] != id]
        return True

    

    def get_member(self, id):
        # Busca en la lista y devuelve el miembro correspondiente
        for member in self._members:
            if member['id'] == id:
                return member
        return None

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members

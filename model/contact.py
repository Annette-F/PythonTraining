from sys import maxsize


class Contact:
    def __init__(self, firstname=None, lastname=None, company=None, address=None, phonehome=None, email=None, id=None):
        self.firstname = firstname
        self.lastname = lastname
        self.company = company
        self.address = address
        self.phonehome = phonehome
        self.email = email
        self.id = id

    def __repr__(self):
        return f'{self.id}:{self.firstname}:{self.lastname}'

    def __eq__(self, other):
        return (self.id == other.id and self.firstname == other.firstname, self.lastname == other.lastname)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

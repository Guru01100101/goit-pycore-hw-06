from collections import UserDict
from typing import List
from normalize_phone import normalize_phone


class Field:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self):
        return f'{self.name}: {self.value}'


class Name(Field):
    def __init__(self, name):
        super().__init__('Name', name)


class Phone(Field):
    def __init__(self, phone):
        super().__init__('Phone', normalize_phone(phone))


class Record:
    def __init__(self, name, phones: List[Phone] = []):
        self.name = Name(name)
        self.phones = phones

    def add_phone(self, phone):
        self.phones.append(phone)

    def edit_phone(self, phone, new_phone):
        for p in self.phones:
            if p.value == phone:
                p.value = new_phone

    def search_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def __str__(self):
        return (f"Contact name: {self.name.value}, "
                f"phones: {'; '.join(p.value for p in self.phones)}")


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete_record(self, name):
        if name in self.data:
            del self.data[name]

    def __str__(self):
        return '\n'.join(str(record) for record in self.data.values())

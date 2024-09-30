from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Contact:
    name: str
    phone: str
    email: str
    tags: list[str] = field(default_factory=list)
    creation_date: datetime = field(init=False, default=datetime.now())

    def add_tag(self, tag: str):
        if tag not in self.tags:
            self.tags.append(tag)

    def __str__(self) -> str:
        tags = ""
        for tag in self.tags:
            tags += f"{tag}, "
        return f"Name: {self.name}\nPhone: {self.phone}\nEmail: {self.email}\nTags: {tags[:-2]}\nCreated on: {self.creation_date}"


@dataclass
class ContactBook:
    contacts: dict[str, Contact] = field(init=False, default_factory=dict)

    def add_contact(self, name: str, phone: str, email: str, tags: list[str]):
        self.contacts[phone] = Contact(name, phone, email, tags)

    def delete_contact(self, phone: str):
        if phone in self.contacts:
            del self.contacts[phone]

    def list_contacts(self) -> list[Contact]:
        return [contact for contact in self.contacts.values()]

    def contacts_by_tag(self, tag: str) -> list[Contact]:
        return [contact for contact in self.contacts.values() if tag in contact.tags]

    def search_by_criteria(self, name: str = "", phone: str = "", email: str = "") -> list[Contact]:
        return [contact for contact in self.contacts.values() if (name in contact.name or name == "") and (phone in contact.phone or phone == "") and (email in contact.email or email == "")]

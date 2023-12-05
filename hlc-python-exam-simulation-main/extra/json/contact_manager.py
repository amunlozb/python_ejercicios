import os
import json
from assignment.contact import Contact

class ContactManager:
    """Gestiona una lista de contactos y su almacenamiento en un archivo."""

    def __init__(self, filename):
        """
        Inicializa el gestor de contactos con un archivo especificado.

        Args:
            filename (str): Ruta del archivo donde se guardarán los contactos.
        """
        self.filename = filename
        self.contacts = []

    def add_contact(self, contact):
        """Agrega un nuevo contacto a la lista de contactos."""
        self.contacts.append(contact)

    def find_contact(self, name):
        """
        Busca un contacto por nombre.

        Args:
            name (str): Nombre del contacto a buscar.

        Returns:
            Contact: El contacto encontrado, o None si no se encuentra.
        """
        for contact in self.contacts:
            if contact.nombre == name:
                return contact
        return None

    def save_contacts(self):
        """Guarda los contactos en el archivo especificado en formato JSON."""
        with open(self.filename, 'w') as file:
            json_contacts = [contact.__dict__ for contact in self.contacts]
            json.dump(json_contacts, file, indent=2)

    def load_contacts(self):
        """Carga los contactos desde el archivo especificado en formato JSON."""
        self.contacts = []  # Limpiar la lista antes de cargar nuevos contactos
        with open(self.filename, 'r') as file:
            json_contacts = json.load(file)
            for json_contact in json_contacts:
                self.contacts.append(Contact(**json_contact))

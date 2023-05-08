import xml.etree.ElementTree as ET
import time


class XMLEntity:

    # Il costruttore parsa il file XML di metadata.
    def __init__(self, entity_id=None):
        self.tree = ET.parse("edugain-v2.xml")
        self.root = self.tree.getroot()
        if entity_id is not None:
            self.entity_id = entity_id
        self.entity_id = ""
        self.regauth = ""
        self.dsc = ""
        self.display_names = ""

    def get_all_entityids(self):
        entity_ids = []
        for child in self.root:
            for entity_id in child.attrib.values():
                entity_ids.append(entity_id)
        return entity_ids

    def get_entityid(self):
        return self.entity_id

    def get_all_regatuh(self):

        regs = self.tree.findall(".//{urn:oasis:names:tc:SAML:metadata:rpi}RegistrationInfo")
        regauth_list = [reg.get("registrationAuthority") for reg in regs]
        reg_set = set(regauth_list)
        return reg_set
    """
    def get_dsc(self):
        desc = self.tree.findall(".//{urn:oasis:names:tc:SAML:2.0:metadata:ui}Description")
        for d in desc:
            print(d.text)
    """

    def get_lang(self, org_name):
        names = self.tree.findall(".//{urn:oasis:names:tc:SAML:2.0:metadata}OrganizationName")
        for name in names:
            # Controlla se il nome dell'organizzazione è presente nel file
            if org_name == name.text:
                # Estrae la lingua
                _, lang = name.attrib.popitem()
        return lang

    def get_display_names(self):
        names = self.tree.findall(".//{urn:oasis:names:tc:SAML:2.0:metadata}OrganizationDisplayName")
        self.display_names = set([name.text for name in names])
        return self.display_names
ù


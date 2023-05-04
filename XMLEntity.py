import xml.etree.ElementTree as ET
import time


class XMLEntity:

    # Il costruttore parsa il file XML di metadata.
    def __init__(self):
        self.tree = ET.parse("edugain-v2.xml")
        self.root = self.tree.getroot()
        self.entity_ids = ""
        self.dsc = ""

    def get_all_entityids(self):
        entity_ids = []
        for child in self.root:
            for entity_id in child.attrib.values():
                entity_ids.append(entity_id)
        return entity_ids

    def get_dsc(self):
        desc = self.tree.findall(".//{urn:oasis:names:tc:SAML:2.0:metadata}SPSSODescriptor")
        if desc is not None:
            for d in desc:
                print(d.ET.SubElement())
            #for child in sp:
            #    print(child.text)

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
        display_names = set([name.text for name in names])
        return display_names



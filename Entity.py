import requests
import json


class Entity:

    # Il costruttore base crea un oggetto Entity a partire da un entity_id dato in input.
    def __init__(self, entityid):

        entity_details = requests.get("https://technical.edugain.org/api.php?action=show_entity_details&e_id={id}".format(id=entityid))
        dump = json.dumps(entity_details.json(), indent=4)
        entity_details_json = json.loads(dump)
        if "SPSSODescriptor" in entity_details_json['roles']:
            # Qui vengono inizializzati gli attributi con le informazioni dell'entità data in input
            self.entityid = entity_details_json['entityid']
            self.regauth = entity_details_json['regauth']
            self.logo = entity_details_json['roles']['SPSSODescriptor']['logo']
            self.dn = entity_details_json['roles']['SPSSODescriptor']['DN']
            if "SN" in entity_details_json['roles']['SPSSODescriptor']:
                self.sn = entity_details_json['roles']['SPSSODescriptor']['SN']
            self.pp = entity_details_json['roles']['SPSSODescriptor']['PP']
            self.dsc = entity_details_json['roles']['SPSSODescriptor']['DSC']
            self.lang = entity_details_json['roles']['SPSSODescriptor']['langs']
            self.req_init = ""
            if "requestinitiator" in entity_details_json['roles']['SPSSODescriptor']:
                self.req_init = entity_details_json['roles']['SPSSODescriptor']['requestinitiator']

            self.org = entity_details_json['org']
            # Crea una lista con i display name dell'entità, in base a quanti ne vengono forniti
            self.display_name = []
            for key in self.org.keys():
                self.display_name.append(self.org[key]['displayname'])

        else:
            print("Entity is not a Service Provider")


    # Secondo costruttore, genera un oggetto Entity se è fornito un row_id invece che un entity_id	
    @classmethod
    def from_rowid(cls, rowid):

        entity_details = requests.get("https://technical.edugain.org/api.php?action=show_entity_details&row_id={row}".format(row=rowid))
        dump = json.dumps(entity_details.json(), indent=4)
        entity_details_json = json.loads(dump)

        # Genera un nuovo oggetto Entity senza chiamare il costruttore __init__, poiché non stiamo dando in input un entity_id.
        obj = cls.__new__(cls)
        if "SPSSODescriptor" in entity_details_json['roles']:
            # Qui vengono assegnati gli attributi dell'oggetto, esattamente come nel costruttore.
            obj.entityid = entity_details_json['entityid']
            obj.regauth = entity_details_json['regauth']
            obj.logo = entity_details_json['roles']['SPSSODescriptor']['logo']
            obj.dn = entity_details_json['roles']['SPSSODescriptor']['DN']
            if "SN" in entity_details_json['roles']['SPSSODescriptor']:
                obj.sn = entity_details_json['roles']['SPSSODescriptor']['SN']
            obj.pp = entity_details_json['roles']['SPSSODescriptor']['PP']
            obj.dsc = entity_details_json['roles']['SPSSODescriptor']['DSC']
            obj.lang = entity_details_json['roles']['SPSSODescriptor']['langs']
            if "requestinitiator" in entity_details_json['roles']['SPSSODescriptor']:
                obj.req_init = entity_details_json['roles']['SPSSODescriptor']['requestinitiator']
            obj.org = entity_details_json['org']
            # Crea una lista con i display name dell'entità, in base a quanti ne vengono forniti
            obj.display_name = []
            for key in obj.org.keys():
                obj.display_name.append(obj.org[key]['displayname'])
        else:
            print("Entity is not a Service Provider")

        return obj

    def get_entityid(self):
        return self.entityid

    def get_regauth(self):
        return self.regauth

    def get_logourl(self):
        for key in self.logo.keys():
            return self.logo[key]['value']

    def get_dn(self):
        return self.dn

    def get_sn(self):
        return self.sn

    def get_pp(self):
        return self.pp

    def get_dsc(self):
        return self.dsc

    # Il metodo ritorna la descrizione dell'entità nella lingua che si specifica in input
    def get_dsc_in(self, lang):
        if lang in self.dsc.keys():
            return self.dsc[lang]
        else:
            return None

    def get_lang(self):
        return self.lang

    def get_reqinit(self):
        return self.req_init

    def get_org(self):
        return self.org

    def get_org_url(self):
        for key in self.org.keys():
            return self.org[key]['url']

    def get_displayname(self):
        return self.display_name

    # Semplice metodo che verifica se l'entità è erogata da un'organizzazione italiana
    def is_italian(self):
        if "it" in self.org.keys():
            return True
        else:
            return False



class XMLEntity:

    def __init__(self, entityid):

        entity_details = requests.get("https://technical.edugain.org/api.php?action=show_entity&e_id={id}".format(id=entityid))

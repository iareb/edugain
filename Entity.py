import requests
import json


class Entity:

    # Il costruttore base crea un oggetto Entity a partire da un entity_id dato in input.
    def __init__(self, entityid):

        if type(entityid) is not str:
            raise TypeError("entity_id is not str")
        else:
            entity_details = requests.get("https://technical.edugain.org/api.php?action=show_entity_details&e_id={id}".format(id=entityid))
            dump = json.dumps(entity_details.json(), indent=4)
            entity_details_json = json.loads(dump)

            '''
            roles è una lista delle categorie di servizi, IDP o SP o AA. La classe Entity è generale, quindi non fa differenza
            se l'entità generata è un IDP/SP/AA, le informazioni vengono estratte comunque.
            '''
            roles = ["IDPSSODescriptor", "SPSSODescriptor", "AttributeAuthorityDescriptor"]

            '''
            category è l'effettiva categoria dell'entità. La chiave è trasformata in lista e poi viene estratto il primo elemento.
            category diventa una stringa e può avere valore 'SPSSODescriptor' o 'IDPSSODescriptor'.
            '''
            category = list(entity_details_json['roles'].keys())[0]

            # Se il campo 'roles' del JSON è un IDPSSODescriptor o un SPSSODescriptor, estrae le informazioni.
            if any(x in category for x in roles):

                # Qui vengono inizializzati gli attributi con le informazioni dell'entità data in input
                self.category = category
                self.entityid = entity_details_json['entityid']
                self.regauth = entity_details_json['regauth']
                if "logo" in entity_details_json['roles'][category]:
                    self.logo = entity_details_json['roles'][category]['logo']
                if "DN" in entity_details_json['roles'][category]:
                    self.dn = entity_details_json['roles'][category]['DN']
                if "SN" in entity_details_json['roles'][category]:
                    self.sn = entity_details_json['roles'][category]['SN']
                if "PP" in entity_details_json['roles'][category]:
                    self.pp = entity_details_json['roles'][category]['PP']
                self.dsc = entity_details_json['roles'][category]['DSC']
                self.lang = entity_details_json['roles'][category]['langs']
                self.req_init = ""
                if "requestinitiator" in entity_details_json['roles'][category]:
                    self.req_init = entity_details_json['roles'][category]['requestinitiator']

                self.org = entity_details_json['org']
                # Crea una lista con i display name dell'entità, in base a quanti ne vengono forniti
                self.display_name = []
                for key in self.org.keys():
                    self.display_name.append(self.org[key]['displayname'])

            else:
                print("Entity search problem")


    # Secondo costruttore, genera un oggetto Entity se è fornito un row_id invece che un entity_id
    @classmethod
    def from_rowid(cls, rowid):

        if type(rowid) is not int:
            raise TypeError("row_id is not int")
        else:
            entity_details = requests.get("https://technical.edugain.org/api.php?action=show_entity_details&row_id={row}".format(row=rowid))
            dump = json.dumps(entity_details.json(), indent=4)
            entity_details_json = json.loads(dump)

            # Genera un nuovo oggetto Entity senza chiamare il costruttore __init__, poiché non stiamo dando in input un entity_id.
            obj = cls.__new__(cls)
            roles = ["IDPSSODescriptor", "SPSSODescriptor", "AttributeAuthorityDescriptor"]
            category = list(entity_details_json['roles'].keys())[0]

            if any(x in category for x in roles):

                # Qui vengono assegnati gli attributi dell'oggetto, esattamente come nel costruttore.
                obj.category = category
                obj.entityid = entity_details_json['entityid']
                obj.regauth = entity_details_json['regauth']
                if "logo" in entity_details_json['roles'][category]:
                    obj.logo = entity_details_json['roles'][category]['logo']
                if "DN" in entity_details_json['roles'][category]:
                    obj.dn = entity_details_json['roles'][category]['DN']
                if "SN" in entity_details_json['roles'][category]:
                    obj.sn = entity_details_json['roles'][category]['SN']
                if "PP" in entity_details_json['roles'][category]:
                    obj.pp = entity_details_json['roles'][category]['PP']
                if "DSC" in entity_details_json['roles'][category]:
                    obj.dsc = entity_details_json['roles'][category]['DSC']
                if "langs" in entity_details_json['roles'][category]:
                    obj.lang = entity_details_json['roles'][category]['langs']
                if "requestinitiator" in entity_details_json['roles'][category]:
                    obj.req_init = entity_details_json['roles'][category]['requestinitiator']
                obj.org = entity_details_json['org']
                # Crea una lista con i display name dell'entità, in base a quanti ne vengono forniti
                obj.display_name = []
                for key in obj.org.keys():
                    obj.display_name.append(obj.org[key]['displayname'])
            else:
                print("Entity is not a Service Provider")

        return obj

    # get_category() ritorna 'IDPSSODescriptor' se l'entità è IDP, 'SPSSODescriptor' se l'entità è SP.
    def get_category(self):
        return self.category

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


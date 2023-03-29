from Entity import Entity

# Esempio: genera un oggetto Entity da un entity_id in input
entity = Entity("https://annis.fdm.uni-hamburg.de/shibboleth")
print("Descrizione: ", entity.get_dsc())
print("Controlla se esiste una descrizione in italiano: ", entity.get_dsc_in('it'))
print("Organizzazione: ", entity.get_org())
print("URL dell'organizzazione: ", entity.get_org_url())


# Esempio: controlla se l'entità è erogata da un'rganizzazione italiana
italian = Entity("https://sp-bestr-prod.cineca.it/shibboleth")
print("L'entità è erogata da un'organizzazione italiana? ", italian.is_italian())


# Esempio: genera un oggetto Entity da un row_id in input
obj = Entity.from_rowid(22037)
print("Entity ID: ", obj.get_entityid())
print("URL del logo: ", obj.get_logourl())
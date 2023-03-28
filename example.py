from Entity import Entity

# Esempio: genera un oggetto Entity da un entity_id in input
entity = Entity("https://annis.fdm.uni-hamburg.de/shibboleth")
print("Description: ", entity.get_dsc())
print("Organization: ", entity.get_org())



# Esempio: genera un oggetto Entity da un row_id in input
obj = Entity.from_rowid(22037)
print("Entity ID: ", obj.get_entityid())
print("URL del logo: ", obj.get_logourl())

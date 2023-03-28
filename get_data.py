import requests
import json
from Entity import Entity

# Chiamata all'API che restituisce una lista di Entità Service Provider
entity_list = requests.get("https://technical.edugain.org/api.php?action=list_entities&type=sp&format=json")
# L'oggetto Response è convertito in JSON e poi in dizionario Python, per lavorarci in maniera più semplice
dump = json.dumps(entity_list.json(), indent=4)
entity_json = json.loads(dump)

# Vengono estratti tutti i row_id delle entità ottenute con la chiamata
row_id_list = []
for entity in entity_json:
    try:
        row_id_list.append(entity[0]['id'])
    except KeyError:
        print("C'è stato un errore: ", KeyError)


# Viene creato un oggetto Entity per ogni singolo row_id estratto prima. Così otteniamo le informazioni delle entità.
entity_id_list = []
for row_id in row_id_list:
    obj = Entity.from_rowid(row_id)
    entity_id_list.append(obj.entityid)

print(entity_id_list)

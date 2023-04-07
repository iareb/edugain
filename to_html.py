import pandas as pd
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
try:
    row_id_list = [entity[0]['id'] for entity in entity_json]
except KeyError:
    print("Errore: ", KeyError)


# Trasforma la lista di row_id da stringhe a numeri.
row_id_list = list(map(int, row_id_list))


pd.set_option('display.max_columns', None)

# Viene creato un oggetto Entity per ogni singolo row_id estratto prima. Così otteniamo le informazioni delle entità.
# L'oggetto è poi rappresentato in un DataFrame di pandas, e infine il DataFrame viene trasformato in tabella HTML.
table_file = open("table.html", "w")
for row_id in row_id_list:

    obj = Entity.from_rowid(row_id)

    data = obj.__dict__
    df = pd.DataFrame.from_dict(data, orient='index')
    df = df.transpose()
    table = df.to_html()
    table_file.write(table)

table_file.close()




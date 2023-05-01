import pymongo
import pprint

print("conectando ao MongoDB")

connection = pymongo.MongoClient("mongo-db")

db = connection.bank
collection = db.clients

new_clients = [{
            "agency": 1020,
            "name": "Jonnathan Kent",
            "cpf": "123.456.789.01",
            "address": "Rancho Kent, SN",
            "account": ["cc", "1101201"],
            "balance": 120000
            },
            {
            "agency": 10120,
            "name": "Clark Kent",
            "cpf": "123.456.789.02",
            "address": "Rancho Kent, SN",
            "account": ["cp", "2101201"],
            "balance": 54000
            },

            {
            "agency": 2000,
            "name": "Martha Kent",
            "cpf": "123.456.789.03",
            "address": "Rancho Kent, SN",
            "account": ["cc", "120001"],
            "balance": 45000
            }]


clients = db.clients
result = clients.insert_many(new_clients)
print(result.inserted_ids)


print("\n Obtendo as informações de Clark:")
pprint.pprint(db.clients.find_one({"name": "Clark Kent"}))


print("\n Listando clientes:")
for client in clients.find():
    pprint.pprint(client)

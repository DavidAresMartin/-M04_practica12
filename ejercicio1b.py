import json
def funcionB():
    datas = {
        "book": [
            {"title": "El Principito",
             "cover": "Antoine de Saint-Exupery",
             "year": "1988",
             "pages": "120 paginas"
             },

            {"title": "Crimen Y Castigo",
             "cover": "Fiodor Dostoievski",
             "year": "1998",
             "pages": "211 paginas"
             },

            {"title": "Cien anos de soledad ",
             "cover": "Gabriel Garcia Marquez ",
             "year": "2002",
             "pages": "164 paginas"
             },

            {"title": "Preludio a la fundacion",
             "cover": "Isaac Asimov",
             "year": "2001",
             "pages": "322 paginas"
             }
        ]
    }

    print(json.dumps(datas))

    with open('archivo1.json', 'w') as file:
        json.dump(datas, file)

    with open("archivo1.json", 'r') as file:
        print(json.dumps(datas, indent=2))



















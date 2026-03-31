def blast(query):
    db = {
    "seq001": "ATGCGGAATT",
    "seq002": "CGTACGTAGC",
    "seq003": "TTATGCATTA",
    "seq004": "GGAATCCGTA",
    "seq005": "CATGCCGTAGC",
    "seq006": "GGGCGTGCAT",
    "seq007": "AATGCTAGCTA",
    "seq008": "CGCGATGCGC",
    "seq009": "TATATATATA",
    "seq010": "ATGCGGATGCA"
    }
    list = []
    for i in query:
        if i in db:
            list.append(db[i].keys())
        else:
            print("invalid query")
    print(list)
query = input("enter sequence to blast: ")
blast(query)
def find_matches(query: str, db: dict) -> list:
    List = []
    for key, seq in db.items():
        if query in seq:
            List.append(key)
    return List

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

query = 'ATGC'
List = find_matches(query, db)
print(List)



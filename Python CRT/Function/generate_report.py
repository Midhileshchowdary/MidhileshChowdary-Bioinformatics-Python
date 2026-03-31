db = {
    "geneA": "ATGT",  # 75%
    "geneB": "ATGC",  # 100%
    "geneC": "TTAC",  # 25%
    "geneD": "ATGG",  # 75%
    "geneE": "ATCC",  # 75%
    "geneF": "AGGC",  # 50%
    "geneG": "GTGC",  # 75%
    "geneH": "TTGC",  # 75%
    "geneI": "GGGG",  # 0%
    "geneJ": "ATGA"   # 75%
}

def generate_report(dna,db):
    Count_G=0
    Count_C=0
    if dna in db:
        ID=db[dna]
    for i in dna:
        Count_G=dna.count(i)
        Count_C=dna.count(i)
    GC_count=(Count_G+Count_C)/len(dna)*100
    if(GC_count>=80):
        Status="Good Match"
    elif(GC_count>=50 and GC_count<80):
        Status="Moderate Match"
    else:
        Status
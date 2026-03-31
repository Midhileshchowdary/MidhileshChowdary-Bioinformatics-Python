def generate_report(dna,db):    
    count_g = 0
    count_c = 0
    if dna in db:
        id = db[dna]
    for i in dna:
        count_g = dna.count[i]
        count_c = dna.count[i]
    gc_count = (count_c+count_g)/len(dna)*100
    if(gc_count >= 80):
        status = "Good Match"
    elif(gc_count>=50 and gc_count<80):
        status = "Moderate"
    else:
        status = "poor match"

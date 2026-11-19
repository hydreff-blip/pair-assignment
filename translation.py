def translate(dna):
    length = len(dna)
    start_codon = dna.find("ATG")
    dna1 = []
    for i in range (start_codon, length-(length%3), 3):
        dna1.append(dna[i:i+3])

    import pandas as pd

    df = pd.read_csv("codons.csv")

    prot = []
    for i in dna1:
        if i == "TGA" or i == "TAA" or i == "TAG":
            break
        else:
            for j in range(0,63):
                if i == df["codon"].loc[df.index[j]]:
                    prot.append(df["AA"].loc[df.index[j]])

    prot1 = "-".join(prot)
    print(prot1)
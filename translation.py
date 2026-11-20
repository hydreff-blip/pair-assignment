def translate(seq):
    length = len(seq)
    start_codon = seq.find("ATG")
    seq1 = []
    for i in range (start_codon, length-(length%3), 3):
        seq1.append(seq[i:i+3])

    import pandas as pd

    df = pd.read_csv("codons.csv")

    prot = []
    for i in seq1:
        if i == "TGA" or i == "TAA" or i == "TAG":
            break
        else:
            for j in range(0,63):
                if i == df["codon"].loc[df.index[j]]:
                    prot.append(df["AA"].loc[df.index[j]])

    prot1 = "-".join(prot)
    return(prot1)
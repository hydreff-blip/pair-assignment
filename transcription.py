def transcription(dna):
    rna1 = dna.replace("A", "u").replace("T", "a").replace("G", "c").replace("C", "g")
    rna = rna1.upper()
    return rna
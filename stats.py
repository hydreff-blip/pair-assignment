def stats(seq):
    #length of the sequence
    length = len(seq)
    print(f"Sequence length is {length} b.p.")

    #gc content of the sequence
    GC = round((seq.count("G") + seq.count("C"))/length*100, 2)
    print(f"GC content is {GC}%")    

    #amount of unknown nucleotides
    N = seq.count("N")
    N_percent = round(N/length*100, 2)
    if N_percent > 30:
        print(f"Amount of undefined nucleotides: {N}, which equals to {N_percent}% - low quality.")
    else:
        print(f"Amount of undefined nucleotides: {N}, which equals to {N_percent}% - high quality, congratulations!")

    #finding the start codon
    ATG_position = seq.find("ATG")
    if "ATG" in seq:
        print(f"Start codon found - position {ATG_position}.")
    else:
        print("Start codon not found - translation impossible.")
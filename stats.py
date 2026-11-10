def stats(seq):
    #collecting statistics about the sequence
    length = len(seq)
    GC = round((seq.count("G") + seq.count("C"))/length*100, 2)
    N = seq.count("N")
    N_percent = round(N/length*100, 2)
    AUG_position = seq.find("AUG")
    
    print(f"Sequence length is {length} b.p.\nGC content is {GC}%")

    if N == 1:
        print(f"There is 1 undefined nucleotide in the sequence.")
    else:
        print(f"There are {N} undefined nucleotides in the sequence.")
    
    if N_percent > 30:
        print(f"The sequence contains {round(N/length*100,2)}% of unknown nucleotides - low quality.")
    
    if "AUG" in seq:
        print(f"Start codon found - position {AUG_position}.")
    else:
        print("Start codon not found.")
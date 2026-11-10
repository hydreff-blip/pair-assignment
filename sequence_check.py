def seq_check(dna):
    if ("N" or "n") in dna:
        print("The sequence can't be translated.")

    for i in dna:
        if i != ("A" or "T" or "G" or "C" or "N"):
            print("The sequence contains symbols besides nucleotides.")
            break
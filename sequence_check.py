def seq_check(dna):
    if ("N" or "n") in dna:
        print("The sequence can't be translated.")

    for i in dna:
        if i != "A" and i != "T" and i != "G" and i != "C" and i != "N":
            print("The sequence contains symbols besides nucleotides.")
            break
def seq_check(dna):
    if ("N" or "n") in dna:
        print("\n======= Sequence quality check =======")
        print("The sequence contains unknown nucleotides, so it can't be translated.")
        N_percent = dna.count("N")*100/len(dna)
        if N_percent >= 30:
            print(f"Sequence contains {N_percent}% of unknown nucleotides - low quality.")

    for i in dna:
        if i != "A" and i != "T" and i != "G" and i != "C" and i != "N":
            print("\n======= Sequence quality check =======")
            print("The sequence contains symbols besides nucleotides.")
            break

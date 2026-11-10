import transcription
import sequence_check

# opening a file
#file_name = input()
with open("data/ms2_phage.fasta") as file:
    lines = file.readlines()

    if lines[0].startswith(">"):
        print("Header: ", lines[0])
        lines.remove(lines[0])

    for line in lines:
        line = line.rstrip()

    dna = "".join(lines)
    print(dna)



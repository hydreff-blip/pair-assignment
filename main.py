from transcription import transcribe
from sequence_check import seq_check
from stats import stats

# opening a file
#file_name = input()
with open("data/ms2_phage.fasta") as file:

    lines = file.readlines()

    if lines[0].startswith(">"):
        print("Header: ", lines[0].rstrip())
        lines.remove(lines[0])

    lines_stripped = []
    for line in lines:
        line = line.rstrip()
        lines_stripped.append(line)

    dna = "".join(lines_stripped)

    seq_check(dna)
    stats(dna)
    print (f"mRNA: {transcribe(dna)}")



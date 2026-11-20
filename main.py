from transcription import transcribe
from sequence_check import seq_check
from stats import stats
from pcr import primer_design
from restriction import restrictases, sites, restriction_sites, looking_for_sites

# opening a file
#file_name = input("Enter path to a .fasta file: ")
with open("data/ms2_phage.fasta") as file:

    lines = file.readlines()

    if lines[0].startswith(">"):
        print("Header: ", lines[0].rstrip()[1::])
        lines.remove(lines[0])

    lines_stripped = []
    for line in lines:
        line = line.rstrip()
        lines_stripped.append(line)

    dna = "".join(lines_stripped)

    seq_check(dna)
    stats(dna)
    print (f"\n======= mRNA =======\n{transcribe(dna)}")
    primer_design(dna)
    restriction_sites(dna)
    looking_for_sites(dna)



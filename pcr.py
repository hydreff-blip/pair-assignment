def primer_design (seq):
    primers = {}
    primers['forward'] = seq[0:20]
    coding_rev = seq[-20::]
    coding_rev = coding_rev[::-1]
    reverse_lower = coding_rev.replace('A','t').replace('T','a').replace('G','c').replace('C','g')
    primers['reverse'] = reverse_lower.upper()
    print(f"Primers for sequence: {primers}")
    return primers

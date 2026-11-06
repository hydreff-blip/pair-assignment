def gc_content(seq):
    gc = (seq.count("G") + seq.count("C")) / len(seq)
    return round(gc, 5)
def gc_content(seq):
    gc = (seq.count("G") + seq.count("C")) / len(seq) * 100
    return round(gc, 2)

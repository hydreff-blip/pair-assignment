restrictases = {
            'AatII': 'GACGTC', 'AcII': 'AACGTT', 'AfeI': 'AGCGCT', 'AfIII': 'CTTAAG',
            'AgeI': 'ACCGGT', 'ApaI': 'GGGCCC', 'ApaLI': 'GTGCAC', 'AscI': 'GGCGCGCC',
            'AseI': 'ATTAAT', 'AsiSI': 'GCGATCGC', 'AvrII': 'CCTAGG', 'BamHI': 'GGATCC',
            'BbsI': 'GAAGAC', 'BbvCI': 'CCTCAGC', 'BbvI': 'GCAGC', 'BccI': 'CCATC',
            'BceAI': 'ACGGC', 'BciVI': 'GTATCC', 'BcII': 'TGATCA', 'BcoDI': 'GTCTC',
            'BfaI': 'CTAG', 'BfuAI': 'ACCTGC', 'BglII': 'AGATCT', 'BmgBI': 'CACGTC',
            'BmrI': 'ACTGGG', 'BmtI': 'GCTAGC', 'BpmI': 'CTGGAG', 'BpuEI': 'CTTGAG',
            'BseRI': 'GAGGAG', 'BseYI': 'CCCAGC', 'BsgI': 'GTGCAG', 'BsiWI': 'CGTACG',
            'BsmAI': 'GTCTC', 'BsmBI': 'CGTCTC', 'BsmFI': 'GGGAC', 'BsmI': 'GAATGC',
            'BspCNI': 'CTCAG', 'BspDI': 'ATCGAT', 'BspEI': 'TCCGGA', 'BspHI': 'TCATGA',
            'BspMI': 'ACCTGC', 'BspQI': 'GCTCTTC', 'BsrBI': 'CCGCTC', 'BsrDI': 'GCAATG',
            'BsrGI': 'TGTACA', 'BsrI': 'ACTGG', 'BssHII': 'GCGCGC', 'BssSI': 'CACGAG',
            'BstBI': 'TTCGAA', 'BtgZI': 'GCGATG', 'BtsCI': 'GGATG', 'ClaI': 'ATCGAT',
            'EarI': 'CTCTTC', 'EciI': 'GGCGGA', 'EcoRI': 'GAATTC', 'EcoRV': 'GATATC',
            'Esp3I': 'CGTCTC', 'FatI': 'CATG', 'FseI': 'GGCCGGCC', 'FspI': 'TGCGCA',
            'HgaI': 'GACGC', 'HhaI': 'GCGC', 'HindIII': 'AAGCTT', 'HpaI': 'GTTAAC',
            'HphI': 'GGTGA', 'KasI': 'GGCGCC', 'KpnI': 'GGTACC', 'MboII': 'GAAGA',
            'MfeI': 'CAATTG', 'MluI': 'ACGCGT', 'MscI': 'TGGCCA', 'NarI': 'GGCGCC',
            'NcoI': 'CCATGG', 'NdeI': 'CATATG', 'NgoMIV': 'GCCGGC', 'NheI': 'GCTAGC',
            'NotI': 'GCGGCCGC', 'NruI': 'TCGCGA', 'NsiI': 'ATGCAT', 'PacI': 'TTAATTAA',
            'PaqCI': 'CACCTGC', 'PciI': 'ACATGT', 'PleI': 'GAGTC', 'PluTI': 'GGCGCC',
            'PmeI': 'GTTTAAAC', 'PmlI': 'CACGTG', 'PstI': 'CTGCAG', 'PvuI': 'CGATCG',
            'PvuII': 'CAGCTG', 'RsaI': 'GTAC', 'SacI': 'GAGCTC', 'SacII': 'CCGCGG',
            'SalI': 'GTCGAC', 'SapI': 'GCTCTTC', 'ScaI': 'AGTACT', 'SfaNI': 'GCATC',
            'SfoI': 'GGCGCC', 'SmaI': 'CCCGGG', 'SnaBI': 'TACGTA', 'SpeI': 'ACTAGT',
            'SphI': 'GCATGC', 'SrfI': 'GCCCGGGC', 'StuI': 'AGGCCT', 'SwaI': 'ATTTAAAT',
            'XbaI': 'TCTAGA', 'XhoI': 'CTCGAG', 'XmaI': 'CCCGGG', 'ZraI': 'GACGTC'}
sites = []

def restriction_sites(seq):
    sites.clear()  # Clear the list before searching for new sites
    for enzyme, site in restrictases.items():
        if site in seq:
            sites.append(restrictases[enzyme])
    if len(sites) == 0:
        return "No restriction sites found."
    else:
        return sites

def looking_for_sites(seq):
    print('What site are you looking for? (type the name of the enzyme or "all" to see all the sites)')
    name = input()
    if name == "all":
        print(sites)
    elif name in restrictases:
        if restrictases[name] in sites:
            print(f"{name} site is present in the sequence.")
        else:
            print(f"No {name} site found in the sequence.")
    else:
        print("Enzyme not recognized. Please check the name and try again.")
    print("Do you want to look for another site? (Y/N)")
    answer = input()
    if answer == "Y" or answer == "y":
        looking_for_sites(seq)
    elif answer == "N" or answer == "n":
        print("Thank you for using the restriction site finder.")

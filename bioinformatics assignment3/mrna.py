
codon_table = {
    'F': 2, 'L': 6, 'S': 6, 'Y': 2, 'C': 2, 'W': 1, 'P': 4, 'H': 2, 'Q': 2,
    'R': 6, 'I': 3, 'M': 1, 'T': 4, 'N': 2, 'K': 2, 'V': 4, 'A': 4, 'D': 2,
    'E': 2, 'G': 4, 'STOP': 3
}

def count_rna_strings(protein):
    total = 1
    modulo = 1000000
    for amino_acid in protein:
        total = (total * codon_table[amino_acid]) % modulo
    total = (total * codon_table['STOP']) % modulo
    return total
protein = "MA"
print(count_rna_strings(protein))
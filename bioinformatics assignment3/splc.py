
def transcribe_dna_to_rna(dna):
    return dna.replace('T', 'U')
def translate_rna_to_protein(rna):
    
    codon_table = {
        'AUG': 'M', 'GUC': 'V', 'UCA': 'S', 'CAU': 'H', 'AGC': 'S', 'UGA': '',
        'AAC': 'N', 'AAG': 'K', 'GAU': 'D', 'GGC': 'G', 'GUA': 'V', 'GUG': 'V',
        'GAC': 'D', 'GAA': 'E', 'UUG': 'L', 'GCU': 'A', 'UAU': 'Y', 'CUG': 'L',
        'UCU': 'S', 'ACU': 'T', 'GCU': 'A', 'CCG': 'P', 'CGA': 'R', 'GAA': 'E',
        'GCA': 'A', 'GCG': 'A', 'UCA': 'S', 'CGA': 'R', 'GAU': 'D', 'UGG': 'W',
    }
    protein = []
    for i in range(0, len(rna), 3):
        codon = rna[i:i+3]
        if codon in codon_table:
            amino_acid = codon_table[codon]
            if amino_acid == '':
                break
            protein.append(amino_acid)
    return ''.join(protein)
def remove_introns(dna, introns):
    for intron in introns:
        dna = dna.replace(intron, '')
    return dna
def main():
    main_dna = "ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG"
    introns = ["ATCGGTCGAA", "ATCGGTCGAGCGTGT"]
    exons_dna = remove_introns(main_dna, introns)
    exons_rna = transcribe_dna_to_rna(exons_dna)
    protein = translate_rna_to_protein(exons_rna)
    print(protein)

if __name__ == "__main__":
    main()

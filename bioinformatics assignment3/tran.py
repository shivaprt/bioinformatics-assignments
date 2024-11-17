def parse_fasta(fasta_data):
    """Parses FASTA input into a list of DNA strings."""
    sequences = []
    current_sequence = []
    for line in fasta_data.splitlines():
        if line.startswith(">"):
            if current_sequence:
                sequences.append("".join(current_sequence))
                current_sequence = []
        else:
            current_sequence.append(line.strip())
    if current_sequence:
        sequences.append("".join(current_sequence))
    return sequences

def calculate_transition_transversion_ratio(s1, s2):
    """Calculates the transition/transversion ratio for two DNA strings."""
    transitions = 0
    transversions = 0
    transition_pairs = {("A", "G"), ("G", "A"), ("C", "T"), ("T", "C")}
    for base1, base2 in zip(s1, s2):
        if base1 != base2:
            if (base1, base2) in transition_pairs:
                transitions += 1
            else:
                transversions += 1
    if transversions == 0:
        return float("inf")
    return transitions / transversions
fasta_input = """>Rosalind_0209
GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGA
AGTACGGGCATCAACCCAGTT
>Rosalind_2200
TTATCTGACAAAGAAAGCCGTCAACGGCTGGATAATTTCGCGATCGTGCTGGTTACTGGC
GGTACGAGTGTTCCTTTGGGT"""
sequences = parse_fasta(fasta_input)
s1, s2 = sequences[0], sequences[1]
ratio = calculate_transition_transversion_ratio(s1, s2)
print(f"{ratio:.11f}")
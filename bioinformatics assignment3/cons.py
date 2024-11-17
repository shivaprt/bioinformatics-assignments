def parse_fasta(fasta_data):
    """Parse FASTA format input into a list of DNA strings."""
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
def calculate_profile_and_consensus(dna_strings):
    """Calculate the profile matrix and consensus string."""
    n = len(dna_strings[0])
    profile = {
        'A': [0] * n,
        'C': [0] * n,
        'G': [0] * n,
        'T': [0] * n,
    }
    for dna in dna_strings:
        for i, base in enumerate(dna):
            profile[base][i] += 1
    consensus = []
    for i in range(n):
        max_base = None
        max_count = -1
        for base in "ACGT":
            if profile[base][i] > max_count:
                max_count = profile[base][i]
                max_base = base
        consensus.append(max_base)
    return "".join(consensus), profile
fasta_input = """>Rosalind_1
ATCCAGCT
>Rosalind_2
GGGCAACT
>Rosalind_3
ATGGATCT
>Rosalind_4
AAGCAACC
>Rosalind_5
TTGGAACT
>Rosalind_6
ATGCCATT
>Rosalind_7
ATGGCACT"""
dna_strings = parse_fasta(fasta_input)
consensus, profile = calculate_profile_and_consensus(dna_strings)
print(consensus)
for base in "ACGT":
    print(f"{base}: {' '.join(map(str, profile[base]))}")

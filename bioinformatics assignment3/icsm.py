
def parse_fasta(fasta_data):
    """Parse FASTA format data into a list of DNA strings."""
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

def find_longest_common_substring(dna_strings):
    """Find the longest common substring among a list of DNA strings."""
    shortest = min(dna_strings, key=len)
    length = len(shortest)
    for l in range(length, 0, -1):
        for start in range(length - l + 1):
            candidate = shortest[start:start + l]
            if all(candidate in dna for dna in dna_strings):
                return candidate

    return ""
fasta_input = """>Rosalind_1
GATTACA
>Rosalind_2
TAGACCA
>Rosalind_3
ATACA"""
dna_strings = parse_fasta(fasta_input)
lcs = find_longest_common_substring(dna_strings)
print(lcs)


mass_table = {
    'A': 71.037, 'C': 103.009, 'D': 115.027, 'E': 129.043, 'F': 147.068,
    'G': 57.021, 'H': 137.058, 'I': 113.084, 'K': 128.094, 'L': 113.084,
    'M': 131.040, 'N': 114.043, 'P': 97.053, 'Q': 128.059, 'R': 156.101,
    'S': 87.032, 'T': 101.048, 'V': 99.068, 'W': 186.079, 'Y': 163.063
}

def calculate_protein_mass(protein):
    total_weight = 0.0 
    for aa in protein:
 
        if aa in mass_table:
            total_weight += mass_table[aa]
        else:
            print(f"Warning: Unknown amino acid '{aa}' found!")
    return round(total_weight, 3)


protein = "SKADYEK"
result = calculate_protein_mass(protein)
print(result) 
######################
#### EXERCISE 1.2 ####
######################


## Consider the nucleotide chain of the previous exercise. Indicate the frequency of occurrence (in %) of nucleotides A, C, G and T ##
print("\n### EXERCISE 1.2 ###\n")

## first put the chain ##
nuc_chain='CATAGCGACAAGCTCGTAGGACATGAGACCACTTGAGCTTCACGCGCCATCCCCAGTGTAAGTCCCCTTACCCCGC'

# Calculate the frecuency of a nucleotide in a chain
# frecuency of a % = ( number of a / number of all the letters ) * 100
def frequency_nucleotide(chain, nucleotide):
    return (chain.count(nucleotide)/len(chain))*100

# Save in a hash the frecuency of each nucleotide
# key: nucleotide
# value: frecuency
def frequency_nucleotide_dict(chain):
    frec_aa={}
    frequency_A = frequency_nucleotide(nuc_chain, 'A')
    frec_aa['A']=frequency_A
    frequency_T = frequency_nucleotide(nuc_chain, 'T')
    frec_aa['T']=frequency_T
    frequency_C = frequency_nucleotide(nuc_chain, 'C')
    frec_aa['C']=frequency_C
    frequency_G = frequency_nucleotide(nuc_chain, 'G')
    frec_aa['G']=frequency_G
    return(frec_aa)

# this function prints the frecuencies of each nucleotide 
# and add the frecuencies to prove that it's good calculated
def print_frequency_nucleotide_dict(chain, dict):
    print("Frecuency of nucleotide in the nucleotide chain:",chain,"\n")
    total=0
    for key,value in dict.items():
        print ("The frecuency of {0} is {1}%".format(key, round(value,2)))
        total=total+value
    print("All this aminoacids add up to",total,"%")

# calculate the frecuency of the nucleotides 
frecuency_aa = frequency_nucleotide_dict(nuc_chain)
print_frequency_nucleotide_dict(nuc_chain,frecuency_aa)



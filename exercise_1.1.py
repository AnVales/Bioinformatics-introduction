######################
#### EXERCISE 1.1 ####
######################


## first put the chain ##
nuc_chain='CATAGCGACAAGCTCGTAGGACATGAGACCACTTGAGCTTCACGCGCCATCCCCAGTGTAAGTCCCCTTACCCCGC'
print("\n### EXERCISE 1.1 ###\n")
print("The nucleotide chain is:",nuc_chain)

## Indicate the position (index) of substrings ##

# this function saves all the positions of the substring in the string
# find by default only saves the first
# it searchs for the first, the second...
# until there aren't more and .find()==-1
# if there isn't any substring in the string saves "No Find"
def position_substring(string,substring):
    a_list=[]
    flag=True
    start=0

    while True:
        a = string.find(substring,start)

        if a==-1:
            break
        else:
            start=a+1
            a_list.append(a)
        if len(a_list)<1:
            a_list.append("No Find")
    return (a_list)


# a function that prints the information about the positions of the substring in the string
def print_positions(substring,position_substring):

    # how many finds
    how_many=""
    if position_substring[0]=="No Find":
        how_many="any"
    else: 
        how_many=len(position_substring)

    # positions
    positions=""
    if len(position_substring)==1:
        positions = str(position_substring[0])
    elif len(position_substring)>1:
        positions = str(position_substring)[1:-1]

    # print results
    print("\nSubstring:",substring,
    "\n Appears the number of times:", how_many,
    "\n Appears in the positions: ", positions)

# search for the substrings and prints the results 

# substring 'TTGAGC'
substring_1='TTGAGC'
position_substring_1 = position_substring(nuc_chain,substring_1)
print_positions(substring_1,position_substring_1)

# substring 'ATG'
substring_2='ATG'
position_substring_2 = position_substring(nuc_chain,substring_2)
print_positions(substring_2,position_substring_2)

# substring 'TAA'
substring_3='TAA'
position_substring_3 = position_substring(nuc_chain,substring_3)
print_positions(substring_3,position_substring_3)


## Indicate the number of nucleotides that are between two substrings ##

# this function calculates the number of aminoacids between the two substrings
# the array that is given to this function must have the same number of elements
# this is important because it's needed two values between have the aminoacids
def nuc_between(position_substring_a, position_substring_b, substring_a, substring_b):
    nuc_between_two_list=[]
    if len(position_substring_a)==len(position_substring_b):
        for i in range(len(position_substring_a)):
            if position_substring_a[i]<position_substring_b[i]:
                nuc_between_two_list.append(position_substring_b[i]-position_substring_a[i]-len(substring_a))
            else:
                nuc_between_two_list.append(position_substring_a[i]-position_substring_b[i]-len(substring_b))
    else:
        print("There isn't the same number of items in both lists")
    return (nuc_between_two_list)

# this function prints the information of the number of aminoacids between the two substrings
def print_nuc_between(nuc_between_,position_substring_a,position_substring_b):
    for i in range(len(nuc_between_)):
        print("\nThere are",nuc_between_[i],"nucelotides between",position_substring_a, "and", position_substring_b)

# calculate the distance Between substring_2 'ATG' and substring_2 'TAA'
nuc_between_ATG_TAA = nuc_between(position_substring_2, position_substring_3, substring_2, substring_3)
print_nuc_between(nuc_between_ATG_TAA,substring_2,substring_3)
import re
#-----------------------------------------------------------------
# BIOL/CMPU-353
# Spring 2020
# DNA: Playing with Strings with RegEx
# Author: Matthew Imiolek
#-----------------------------------------------------------------
#
# Summary: This Python program isolates the upstream and genic
#          regions of a sequence. A report is printed, a sample
#          of which is saved in file: genic-report.txt. This version
#          uses RegEx.
#
#-----------------------------------------------------------------

print("\n+++++++++ Upstream and Genic Report ++++++++++++++++\n")

# upstream and start of a gene ... 
some_sequence = "cgccatataatgctcgtccgcgcccta"
 
print("Starting sequence is: " + some_sequence)

# convert all nucleotides to uppercase
some_sequence =  some_sequence.upper()
print("Converted to uppercase: " + some_sequence)

# get the length of sequence
seq_length = len(some_sequence) 
print("\nLength of starting sequence is: " + str(seq_length))
 
print("\n----------------------------------------------------\n")

# get the upstream and genic sequences and their lengths
breakByRegex = re.search( r'(.*)(ATG)(...)(...)(.*)', some_sequence)
upstream_len = len(breakByRegex.group(1))
genic_seq = breakByRegex.group(2) + breakByRegex.group(3) + \
breakByRegex.group(4) + breakByRegex.group(5)
genic_len = len(genic_seq)

# print the upstream sequence and gene sequence
print("Upstream sequence is: " + breakByRegex.group(1) + "\n")
print("Gene sequence is: ", genic_seq)

# print the first 3 codons
codon_1 = breakByRegex.group(2)
codon_2 = breakByRegex.group(3)
codon_3 =  breakByRegex.group(4)

print("Codon 1 = " + codon_1)
print("Codon 2 = " + codon_2)
print("Codon 3 = " + codon_3)

print("\n----------------------------------------------------\n")

# print the lengths of the upstream sequence and the gene
print("Upstream length is: " + str(upstream_len))
print("Gene length is: " + str(genic_len))

print("\n----------------------------------------------------\n")



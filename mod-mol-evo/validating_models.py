# ------------------------------------------------------------------------------
# Part II of Assignment 2
# Matthew Imiolek
# ------------------------------------------------------------------------------

import re
import random
import statistics

################################################################################
# Global Variables
################################################################################
fasta_file = "C:\\Users\\mcimi\\Desktop\\cmpu-353\\mod-mol-evo\\comparison.fasta.txt" # fasta file to generate data from
sequences = [""] * 6 # array holding each individual nucleotide sequence
seq_names = [""] * 6 # array holding each sequence name
stat_names = ["Mean", "Median", "Min", "Max", "Range", "Mode"]



################################################################################
# main function
# does all the stuff
################################################################################
def main():
    read_fasta_file(fasta_file)
    diff_nuc_counts = calc_div()
    calc_stats(diff_nuc_counts)
  
  

################################################################################
# calc_div
# calculate the diversity of nucleotides at a specific location across
# all of the species
################################################################################
def calc_div():
    num_diff = [0] * len(sequences[0]) # an array that holds the number of different nucleotides at different locations
    loc = 0                            # location in array
    
    # count the number of different nucleotides between sequences, ignores gaps
    for let1, let2, let3, let4, let5, let6 in zip(sequences[0], sequences[1], sequences[2], sequences[3], sequences[4], sequences[5]):
        if let1 != "-":
            num_diff[loc] += 1
        if let2 != "-" and let2.upper() != let1.upper():
            num_diff[loc] += 1
        if let3 != "-" and (let3.upper() != let1.upper() and let3.upper() != let2.upper()):
            num_diff[loc] += 1
        if let4 != "-" and (let4.upper() != let1.upper() and let4.upper() != let2.upper() and let4.upper() != let3.upper()):
            num_diff[loc] += 1
        if let5 != "-" and (let5.upper() != let1.upper() and let5.upper() != let2.upper() and let5.upper() != let3.upper() and let5.upper() != let4.upper()):
            num_diff[loc] += 1
        if let6 != "-" and (let6.upper() != let1.upper() and let6.upper() != let2.upper() and let6.upper() != let3.upper() and let6.upper() != let4.upper() and let6.upper() != let5.upper()):
            num_diff[loc] += 1
            
        loc += 1
    
    return num_diff
    


################################################################################
# calc_stats
# calculates the significant statistics for each position in a codon (mean, median, mode)
################################################################################
def calc_stats(counts):
	divided_counts = [[], [], []]  # holds the counts divided by position
	means = [0,0,0]             # holds the means
	medians = [0,0,0]           # holds the medians
	modes = [0,0,0]             # holds the modes
	
	# put the counts in their specific list by position in codon
	for x in range(0, len(counts)):
		if x % 3 == 0:
			divided_counts[0].append(counts[x])
		elif x % 3 == 1:
			divided_counts[1].append(counts[x])
		else:
			divided_counts[2].append(counts[x])

	# calculate and print stats
	for x in range(0,3):
		means[x] = statistics.mean(divided_counts[x]) 
		medians[x] = statistics.median(divided_counts[x])
		modes[x] = statistics.mode(divided_counts[x])
		
		print("Codon Position " + str(x + 1) + ":")
		print("\tMean:\t" + str(means[x]))
		print("\tMedian:\t" + str(medians[x]))
		print("\tMode:\t" + str(modes[x]))
		print()
	
	

################################################################################
# read_fasta_file
# read in and break up the FASTA file to each different sequence
################################################################################
def read_fasta_file(filename):
    count = -1 # the location in the array of sequence currently being added to
    
    in_file = open(filename, 'r')

    # add each line of the sequence to the correct part of the array
    for line in in_file:
        # check if the next sequence has been reached
        next_seq_check = re.search(r'^>([\w]+)', line)
        
        # add to list of names or to the sequence
        if next_seq_check:
            seq_names[count] = next_seq_check.group(1)
            count += 1
        else:
            sequences[count] = sequences[count] + line.rstrip('\n')

    in_file.close()

main()



# BELOW THIS IS OLD CODE I WANTED TO KEEP FROM BEFORE I UNDERSTOOD WHAT WE WERE
# DOING !!!!!!!!!!!!!!!!!!!!!

################################################################################
# calculate_pair
# OBSOLETE
# calculate the summary statistics for a pair of sequences, also calculate
# numbers useful for comparing all sequences
################################################################################
def calculate_pair(seq1, seq2, counts, stats):
    cur_location = 0   # the current location in the string being examined
    
    # count the number of mutations between the sequences, ignores spacing
    for let1, let2 in zip(seq1, seq2):
        cur_location += 1
        
        if let1 != let2 and (let1 != '-' or let2 != '-'):
            counts[cur_location % 3] += 1
    
    # calculate stats
    stats[0] = statistics.mean(counts)        # mean
    stats[1] = statistics.median(counts)      # median
    stats[2] = min(counts)                    # min
    stats[3] = max(counts)                    # max
    stats[4] = stats[3] - stats[2]            # range
    stats[5] = counts.index(stats[3])         # mode
    
    # print the counts for each position
    print("Pos. 1: " + str(counts[1]) + " mutations\t", end = '')
    print("Pos. 2: " + str(counts[2]) + " mutations\t", end = '')
    print("Pos. 3: " + str(counts[0]) + " mutations\t", end = '')
    print()
    
    # print the statistics
    for stat, name in zip(stats, stat_names):
        if name == "Mode":
            if stat == 0:
                print(name + ":\tposition 3")
            else:
                print(name + ":\tposition " + str(stat))
        else:
            print(name + ":\t" + str(stat) + " mutations")



################################################################################
# calculate_all
# OBSOLETE
# compare and calculate the summary statistics based off of the comparisons of
# each pair
################################################################################
def calculate_all():
    combo_num = 0           # integer counting number of combos done so far
    counts = [[0] * 3] * 15 # holds an array of counts for each combination, 
                            # where each array holds the number of changes for each positon in a codon (array at index 0 holds mutations in the third nucleotide)
    stats = [[0] * 6] * 15  # holds an array of stats for each combination,
                            # where each array holds all of summary statistics (mean, median, min, max, range, mode; standard deviation is not valuable)
    tot_counts = [0] * 3    # counts of all combos together
    tot_stats = [0] * 7
    
    
    # calculate each pair
    for x in range(1, 6):
        for y in range(0, x):
            print(seq_names[x] + " and " + seq_names[y] + ":")
            calculate_pair(sequences[x], sequences[y], counts[combo_num], stats[combo_num])
            combo_num += 1
            print("")
            
    # calculate overall stats
    for count in counts:                       
        for x in range(0,3):
            tot_counts[x] += count[x]
            
    tot_stats[0] = statistics.mean(tot_counts)        # mean
    tot_stats[1] = statistics.median(tot_counts)      # median
    tot_stats[2] = min(tot_counts)                    # min
    tot_stats[3] = max(tot_counts)                    # max
    tot_stats[4] = tot_stats[3] - tot_stats[2]        # range
    tot_stats[5] = tot_counts.index(tot_stats[3])     # mode

    # print header
    print("Combined stats:")
    
    # print the counts for each position
    print("Pos. 1: " + str(tot_counts[1]) + " mutations\t", end = '')
    print("Pos. 2: " + str(tot_counts[2]) + " mutations\t", end = '')
    print("Pos. 3: " + str(tot_counts[0]) + " mutations\t", end = '')
    print()
    
    # print the statistics
    for stat, name in zip(tot_stats, stat_names):
        if name == "Mode":
            if stat == 0:
                print(name + ":\tposition 3")
            else:
                print(name + ":\tposition " + str(stat))
        else:
            print(name + ":\t" + str(stat) + " mutations")


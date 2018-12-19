#!/usr/bin/env python3


def parse_fasta(fasta_file):
	fasta_dict = {}
	fasta = open(fasta_file, "r")
	for line in fasta:
		if line.startswith(">"):
			header = line.strip().split(" ")[0][1:]
			fasta_dict[header] = []
		else:
			fasta_dict[header].append(line.strip())
	fasta.close()	

	for header in fasta_dict:
		fasta_dict[header] = "".join(fasta_dict[header])

	return fasta_dict

def write_fasta(file_handle, fasta_dict):
	file = open(file_handle, "w")
	for chrom in fasta_dict:
		file.write(">{}\n{}\n".format(chrom, "".join(fasta_dict[chrom]))
	file.close()
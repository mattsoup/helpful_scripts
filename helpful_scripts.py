#!/usr/bin/env python3

import gzip

def parse_fasta(fasta_file):

	print("Parsing {}".format(fasta_file))
	fasta_dict = {}
	if fasta_file.endswith(".gz"):
		fasta = gzip.open(fasta_file, "rb")
		for line in fasta:
			line = str(line, "utf-8")
			if line.startswith(">"):
				header = line.strip().split(" ")[0][1:]
				print(header)
				fasta_dict[header] = []
			else:
				fasta_dict[header].append(line.strip())
		fasta.close()	
	else:
		fasta = open(fasta_file, "r")
		for line in fasta:
			if line.startswith(">"):
				header = line.strip().split(" ")[0][1:]
				print(header)
				fasta_dict[header] = []
			else:
				fasta_dict[header].append(line.strip())
		fasta.close()	

	for header in fasta_dict:
		fasta_dict[header] = "".join(fasta_dict[header])

	return fasta_dict

def write_fasta(file_handle, fasta_dict):
	print("Writing {}".format(file_handle))
	file = open(file_handle, "w")
	for chrom in fasta_dict:
		file.write(">{}\n{}\n".format(chrom, "".join(fasta_dict[chrom])))
	file.close()
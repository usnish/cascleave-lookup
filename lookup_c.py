## Usnish Majumdar, last updated 1/11/16
## SCRIPT #1
# This script will take a list of NCBI protein GI numbers, retrieve their amino acid sequences,
# and then run all of the sequences through the cascleave algorithm available here:
# http://sunflower.kuicr.kyoto-u.ac.jp/~sjn/Cascleave/webserver.html
## requirements: Biopython
## USAGE:
# $python lookup.py prot_gi.txt
# INPUTS:
# prot_gi.txt is a file that contains a list of NCBI protein GI numbers, on separate lines
# OUTPUTS:
# output.txt is a file containing all of the sequences and the time at which the
# query containing those sequences was sent to the webserver.
# output.fasta is a plain FASTA file containing the amino acid sequences that were
# downloaded from NCBI.

from Bio import Entrez
from Bio import SeqIO
import mechanize
import datetime
import time
import sys

Entrez.email = "******@*****.***"

## set up Browser for form entry
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(False)
br.addheaders = [('User-agent', 'Firefox')]
form_url = "http://sunflower.kuicr.kyoto-u.ac.jp/~sjn/Cascleave/webserver.html"
response = br.open(form_url)

identifiers = [] # a list of the fasta sequence identifiers
sequences = [] # a list of raw peptide sequences

f = open("prot_gi.txt")
prot_gis = f.read().splitlines()

f_out = open("output.txt",'w')
fasta_out = open("output.fasta", 'w')

handle = Entrez.efetch(db="protein", rettype="fasta", retmode="text", id=prot_gis)
for seq_record in SeqIO.parse(handle, "fasta"):
    identifier = ">" + seq_record.id + seq_record.description
    sequence = seq_record.seq

    identifiers.append(identifier)
    sequences.append(str(sequence))

    print "processing ", identifier
    print >>f_out, identifier
    print >>f_out, sequence
    print >>fasta_out, identifier
    print >>fasta_out, sequence

    br.select_form("form1")
    sequence_input = br.form.find_control("textarea")
    selector = br.form.find_control("schema")
    email = br.form.find_control("textfield")

    sequence_input.value = identifier + '\n' + sequence
    selector.value = ["2"]
    email.value = Entrez.email

    response = br.submit()
    print "submitted at ", datetime.datetime.now()
    print >>f_out, datetime.datetime.now()
    print >>f_out, response.read()
    br.back()

    time.sleep(60)

handle.close()

print "all done!"
print >>f_out, "all done!"

# send to form

f.close()
f_out.close()
fasta_out.close()
p_identifiers.close()
p_sequences.close()

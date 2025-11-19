# Annotation_scripts
Scripts for helping to process the bacterial genome annotation data
## get_cazymes.py
The script uses the output file "overview" from dbcan and an output file named by the user.
It just enlists the results of dbcan, keeping with a cazyme at least founded with two algorithms.

If more than one algorithm finds the cazyme, the output name of eCAMI is kept.
DIAMOND's name is kept if it is found the cazyme with DIAMOND and HMMER.
If the gene comprises more than one cazyme, all the cazymes are kept and listed.

Usage:

        get_cazymes.py <input.txt> <output.txt>

## convert_bagel_to_antismash_like.py
The script converts the gbk output of Bagel4 to the gbk output of Antismash.
This helps to process these gbks with BigScape.

Usage:

        convert_bagel_to_antismash_like.py <bagel.gbk> <antismash.gbk>

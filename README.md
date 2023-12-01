# Annotation_scripts
Scripts for helping the processing of annotations bacteria genome data
## get_cazymes.py
The script uses the output file "overview" from dbcan and an output file named by the user.
It just enlists the results of dbcan, keeping with a cazyme at least founded with two algorithms.

In case more than one algorithm finds the cazyme, the output name of eCAMI is kept.
If it found the cazyme with DIAMOND and HMMER, DIAMOND's name is kept.
If the gene is composed of more than one cazyme, all the cazymes are kept and enlisted.

Usage:

        get_cazymes.py <input.txt> <output.txt>

# cascleave-lookup
## Requirements:
* Python >3.0
* Python packages noted in `requirements.txt`
* (preferred) Gmail account

## How to use?
* Script #1: `lookup_c.py` -- this will take a list of GenInfo Identifiers (gi #s), retrieve their associated amino acid sequences from NCBI, and then run them through the [CasCleave algorithm hosted by Kyoto University](http://sunflower.kuicr.kyoto-u.ac.jp/~sjn/Cascleave/webserver.html). You will need to change `Entrez.email = "******@*****.***"` to your email. Make sure you have an NCBI account with this email, and expect to recieve cascleave results at this email address soon after the script completes its run.
* Script #2: `process_email_output_c.py` -- this will login to your Gmail (change `email_id = '****@*****.***'`), asking you for your password (not stored anywhere!!!), and spit out a list of protein names, predicted cut sites, and sequences of those sites. It will also compare those sites with sites found via our proteomics pipeline (`Unique_FDR_CC.csv`).

## Caveats
* This code utilizes web scraping and simple email libraries -- if either the [CasCleave algorithm website](http://sunflower.kuicr.kyoto-u.ac.jp/~sjn/Cascleave/webserver.html) or Gmail change their interfaces, this script will cease to function.

## Citation:
Victor KG, Heffron DS, Sokolowski JD, Majumdar U, Leblanc A, Mandell JW. 
Proteomic identification of synaptic caspase substrates. Synapse . 2018;72(1).

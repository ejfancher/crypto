cryptotool (find various frequency distributions and repeats of a text or check for differences between two similar rootca certs)

It was designed with Python 3.7

Libraries used:
    argparse: for parsing command line options
    numpy: for list creation, manipulation and analysis routines. For example the numpy argmax() method which returns
    the index of the largest element of a nplist object is used in my get_ngram_frequencies() method



Command line usage:

./ctool.py [-h] [-c] [-n N] [-p] [-d] file

positional arguments:
  file        path of file containing the text to be analyzed (relative to the
              directory ctool.py is in)

optional arguments:
  -h, --help  show this help message and exit
  -c          display frequency distrubution of characters in the file
  -n N        enter the length of ngram after this option to display the
              frequency distrubution of such ngrams in the text
  -p          display possible periods based on repeats found in the text
  -d          supplementary to -p, display detailed information on the repeats
              found
  --cmp-pems  output dump of 2 certs, an expir(ing/ed) rootca cert and it's 
              replacement. arguments are the 2 certs in such order


references:
Basic Cryptanalysis. DEPARTMENT OF THE ARMY, 1970, Part Four.
“Frequency Distribution.” Wikipedia, Wikimedia Foundation, 22 Aug. 2018, en.wikipedia.org/wiki/Frequency_distribution.

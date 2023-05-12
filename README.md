# hw3

The github link for this project is: https://github.com/bgoldsc1/hw3

In order for this file to work, it must have access to the following two Python modules. For the Bloom filter, I used this module: https://pypi.org/project/bloom-filter2/. Two, for the MPHF, I used this module: https://pypi.org/project/bbhash/

To run this code, it is enough to simply run it in an environment where it has access to these modules. I hard-coded the particular numbers that are important in the code. Thus, to change, for example, the target false positive rate of the Bloom filter or the number of bits saved in the fingerprint array, one would simply change the value of the variable b at the beginning of the code. Likewise, to change the number of keys generated, one would change the value of the num_keys variable, and, to change the fraction of true keys which are also query keys, one would change the value of the frac variable. 

The code will print the relevant information, such as query time, false positive occurrences, etc. to the console. 

# -*- coding: utf-8 -*-
"""
Spyder Editor

"""
    
from bloom_filter2 import BloomFilter
import string
import random
import datetime
import bbhash
import sys

tkeys = []
qkeys = []
fingerprint = []
b = 10
num_keys = 10000
# This means that 1 in 2 query keys will be true keys
frac = 2

for i in range(num_keys):
    res = random.randint(0,2**32)
    tkeys.append(res)
    fingerprint.append(0)
    if i % frac == 0:
        qkeys.append(res)
        for i in range(frac-1):
            res = random.randint(0, 2**32)
            qkeys.append(res)
          
bloom = BloomFilter(max_elements=10000, error_rate=1/2**b)

def build_bloom_filter(bloom_filter, keys):
    for key in keys:
        bloom_filter.add(key)
        
def query_bloom_filter(bloom_filter, query_keys, true_keys):
    start = datetime.datetime.now()
    false_positives = 0
    false_negatives = 0
    for key in query_keys:
        if key in bloom_filter and key not in true_keys:
            false_positives += 1
        elif key not in bloom_filter and key in true_keys:
            false_negatives += 1
    end = datetime.datetime.now()
    duration = end - start
    return (false_positives, false_negatives, duration.microseconds)    
    
build_bloom_filter(bloom, tkeys)
print("Bloom Filter")
print("(False positives, false negatives, duration in microseconds)")
print(query_bloom_filter(bloom, qkeys, tkeys))
print("Size in bytes")
print(bloom.num_bits_m/8)

mph = bbhash.PyMPHF(tkeys, len(tkeys), 1, 1)

start = datetime.datetime.now()
false_positives = 0
for key in qkeys:
    if key not in tkeys and mph.lookup(key) != None:
        false_positives += 1
end = datetime.datetime.now()
duration = end - start
print("MPHF")
print("(False positives, duration in microseconds)")
print ((false_positives, duration.microseconds))

mph.save("mph")

for key in tkeys:
    fingerprint[mph.lookup(key)] = bin(hash(key) % 2**b)
    
start = datetime.datetime.now()
false_positives = 0
for key in qkeys:
    if key not in tkeys and mph.lookup(key) != None:
        if fingerprint[mph.lookup(key)] == bin(hash(key) % 2**b):
            false_positives += 1
end = datetime.datetime.now()
duration = end - start
fingerprint_size = sys.getsizeof(fingerprint)
print("MPHF + Fingerprint Array")
print("(False positives, duration in microseconds, Fingerprint Array size in bytes)")
print ((false_positives, duration.microseconds, fingerprint_size))
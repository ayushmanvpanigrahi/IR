from collections import Counter

Text = """MapReduce is a processing technique and a program model for distributed
computing based on java. The MapReduce algorithm contains two important tasks, namely
Map and Reduce. Map takes a set of data and converts it into another set of data, where
individual elements are broken down into tuple (key/value pairs). Secondly, reduce tasks, which
takes the output from a map as an input and combines those data tuples into a smaller set of
tuples. As the sequences of the same MapReduce implies, the reduce task is always
performed after the map job.

Map stage - The map or mapper's job to process the input data Shuffle stage and the reduce the data
stage. The
Reducer's job is to process the data that comes from the mapper. After processing, it produces
a new set of output, which will be stored in the HDFS"""

for char in '-.,\n':
    Text = Text.replace(char, "")

Text = Text.lower()
word_list = Text.split()
Counter(word_list).most_common()
d = {}

for word in word_list:
    d[word] = d.get(word, 0) + 1

word_freq = []
for key, value in d.items():
    word_freq.append((value, key))

word_freq.sort(reverse=True)
print(word_freq)
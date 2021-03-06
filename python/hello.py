import csv
import json
import logging

import numpy as np

log = logging.getLogger(__name__)

DATEFMT = "[%Y-%m-%d %H:%M:%S]"
FORMAT = "%(asctime)s %(thread)d %(message)s"
logging.basicConfig(level=logging.INFO, format=FORMAT, datefmt=DATEFMT)

msg = "log: Hello World from python app! numpy.dot: %d" % np.dot(2, 3)
log.info(msg)
print(msg)

# read csv: /tcdata/num_list.csv
f = None
try:
    f = open("/tcdata/num_list.csv")
except FileNotFoundError as e:
    log.info(e)
    f = open("./num_list.csv")

num_list = []
f_csv = csv.reader(f)
for row in f_csv:
    for col in row:
        num_list.append(int(col))

f.close()

log.info(num_list)
num_sum = sum(num_list)

# remove duplicated
# num_list = list(set(num_list))

# sort array
num_list.sort(reverse=True)

result = {
    "Q1": "Hello world",
    "Q2": num_sum,
    "Q3": num_list[:10]
}
log.info(result)

# save file
with open("result.json", "w") as f:
    json.dump(result, f)

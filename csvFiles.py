from operator import delitem

from requests import head
import numpy as np
new_data = np.random.random((50,4))
np.savetxt("main.csv", new_data, fmt="%.2f", delimiter=",", header = "H1, H2, H3, H4")

# Reading the csv files
reading_csv = np.loadtxt("main.csv", delimiter=",") 
read_csv = reading_csv[:4, :]
print(read_csv)
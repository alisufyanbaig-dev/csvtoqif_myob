import pandas as pd

df = pd.read_csv(r"C:\Users\Admin\Desktop\Book1.csv")

with open('readme.txt', 'w', newline="") as f:
    f.write("!Type:Bank")
    f.write("\n")
    for index, row in df.iterrows():
        f.write("D" + row['D'])
        f.write("\n")
        f.write("T" + row['T'])
        f.write("\n")
        f.write("M" + row['M'])
        f.write("\n")
        f.write("^")
        f.write("\n")

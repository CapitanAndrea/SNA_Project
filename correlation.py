import pandas as pd

df = pd.read_csv("id-indegree.csv")
print df.corr()

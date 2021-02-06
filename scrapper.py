
import pandas as pd
import requests

res = requests.get(input("Enter Proxy site URL: "))
name = input("Enter output file name: ")
proxies = pd.read_html(res.text)
proxies = proxies[0][:-1]
with open("%s.txt"%name, "w") as f:
    for index,row in proxies.iterrows():
        f.write("%s:%s\n"%(row["IP Address"],int(row["Port"])))
        print("%s:%s"%(row["IP Address"],int(row["Port"])))




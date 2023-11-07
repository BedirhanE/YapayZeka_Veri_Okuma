import pandas as pd

#örnek csv dosyasını okuma işlemi
print(pd.read_csv("ornekcsv.csv",sep=";"))

#örnek txt doyasını okuma işlemi
print(pd.read_csv("duz_metin.txt",sep=";"))

print(pd.read_excel("ornekx.xlsx",))
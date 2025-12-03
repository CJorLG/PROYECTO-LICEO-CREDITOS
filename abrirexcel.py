import pandas as pd

df = pd.read_excel("C:\\Users\\edgar\\Documents\\prueba_excel.xlsx")

# Convertir absolutamente todo a TEXTO
df = df.astype(str)

# Ahora convertir todo a MAYÚSCULAS
df = df.apply(lambda col: col.str.upper())


print(df)


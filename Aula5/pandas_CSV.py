# criar dados para o dataframe
import pandas as pd
import matplotlib.pyplot as plt
dados = {
"Nome": ["Arthur", "Maria", "Mateus", "Carlos", "Bruna"],
"Idade": [28,22, 18, 35, 11], 
"Cidade": ["Cotia", "Caracas", "São Paulo", "Osasco", "Vargem"]
    
}

dados2 = {
    "Nome": [
        "Volkswagen Gol",
        "Volkswagen Parati",
        "Volkswagen Santana",
        "Fiat Uno Fire",
        "Fiat Palio",
        "Fiat Siena",
        "Fiat Fiorino",
        "Fiat Tempra",
        "Chevrolet Corsa",
        "Ford Ka"
    ],
    "Data de Lançamento": [
        "1991-03-15",  # Exemplo de data
        "1990-05-20",
        "1992-08-10",
        "1992-07-01",
        "1996-04-12",
        "1997-09-15",
        "1995-06-08",
        "1990-11-03",
        "1994-03-22",
        "1996-10-30"
    ],
    "Modelo": [
        "Hatchback",
        "Station Wagon",
        "Sedan",
        "Hatchback",
        "Hatchback",
        "Sedan",
        "Van",
        "Sedan",
        "Compacto",
        "Hatchback"
    ],
    "Fabricante": [
        "Volkswagen",
        "Volkswagen",
        "Volkswagen",
        "Fiat",
        "Fiat",
        "Fiat",
        "Fiat",
        "Fiat",
        "Chevrolet",
        "Ford"
    ]
}

df = pd.DataFrame(dados)
print(df)
print("\n")

df2 = pd.DataFrame(dados2)
print(df2)

df2.to_csv("pandas_carros.csv", index=False)

df2_csv = pd.read_csv("pandas_carros.csv")
print("\n")
print("\n")

df_filtrado = df2[df2["Fabricante"] == "Fiat"]
print(df_filtrado)

df_ordenado = df.sort_values(by="Idade", ascending=True)
print(df_ordenado)

print(df.describe())

media_cidade = df.groupby("Cidade")["Idade"].mean()
print("a media da cidade é:\n", media_cidade)
      
df.plot(kind="bar", x="Nome", y="Idade", color="blue")      
plt.title("Idade das pessoas")
plt.xlabel("Nome")
plt.ylabel("Idade")
plt.show()      

df.boxplot(column="Idade", by="Cidade", grid=False)
plt.title("Distribuição da Idadde por Cidade")
plt.xlabel("Cidade")
plt.ylabel("Idade")
plt.show()      
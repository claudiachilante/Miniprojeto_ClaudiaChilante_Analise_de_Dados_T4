import pandas as pd

# Carregar a base de dados

df = pd.read_csv("Base Varejo.csv", sep=";")

# Remover colunas completamente vazias

df = df.dropna(axis=1, how="all")

# Mostrar as primeiras linhas

print(df.head())
print(df.shape)
print(df.isna().sum())
print(df.columns)
print(df.dtypes)
print("Duplicatas:", df.duplicated().sum())
print(df[df.duplicated()].head())

# Remover registros duplicados

df = df.drop_duplicates()
print("Registros após remover duplicatas:", len(df))

# Converter a coluna DATA para o tipo datetime

df["DATA"] = pd.to_datetime(df["DATA"], format="%d/%m/%Y")
print(df.dtypes)
print(df["CL_FHL"].value_counts().sort_index())
print("\nEstatísticas - Número de filhos:")
print("Contagem:", df["CL_FHL"].count())
print("Média:", df["CL_FHL"].mean())
print("Mediana:", df["CL_FHL"].median())
print("Desvio padrão:", df["CL_FHL"].std())
print("Moda:", df["CL_FHL"].mode().tolist())
print("Mínimo:", df["CL_FHL"].min())
print("Máximo:", df["CL_FHL"].max())
print("Quartis:")
print(df["CL_FHL"].quantile([0.25, 0.50, 0.75]))
print("\nCompras por gênero:")
print(df.groupby("CL_GENERO").size())
print("\nCompras por categoria:")
print(df.groupby("PR_CAT").size().sort_values(ascending=False))
print("\nCategorias existentes:")
print(df["PR_CAT"].value_counts(dropna=False))

# Tratar categorias não identificadas

df["PR_CAT"] = df["PR_CAT"].replace("#N/D", "Sem Categoria")
print("\nCategorias após o tratamento:")
print(df["PR_CAT"].value_counts())
print("\nQuantidade de compras por CO_ID:")
print(df["CO_ID"].value_counts().head(10))
print("\nValidação do identificador de compra:")
print("CO_ID nulos:", df["CO_ID"].isnull().sum())
print("Quantidade de CO_ID distintos:", df["CO_ID"].nunique())
print("Menor CO_ID:", df["CO_ID"].min())
print("Maior CO_ID:", df["CO_ID"].max())
print("\nQuantidade de produtos por compra:")
print(df.groupby("CO_ID")["PR_ID"].count().describe())

# Conclusões 

print("\nCONCLUSÕES:")
print("1. Após a limpeza, a base possui 733.447 registros.")
print("2. Foram identificadas e removidas 96.553 duplicatas.")
print("3. A categoria ALIMENTOS apresentou a maior quantidade de registros.")
print("4. O gênero F apresentou mais registros de compras que o gênero M.")
print("5. A quantidade de filhos apresentou mediana igual a 0 e máximo de 4.")
print("6. Foram encontrados 3.228 registros com categoria #N/D, tratados como 'Sem Categoria'.")
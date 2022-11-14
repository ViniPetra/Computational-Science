import pandas as pd
from sklearn import linear_model
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

dataset = pd.read_csv("Ex5/diamonds.csv")

#Limpeza
cutReplaces = {
    "Ideal": 1,
    "Premium" : 2,
    "Very Good" : 3,
    "Good": 4,
    "Fair": 5
}
dataset['cut'].replace(cutReplaces, inplace=True)

colorReplaces = {
    "D": 1,
    "E": 2,
    "F": 3,
    "G": 4,
    "H": 5,
    "I": 6,
    "J": 7
}
dataset['color'].replace(colorReplaces, inplace=True)

clarityReplaces = {
    "IF": 1,
    "VVS1": 2,
    "VVS2": 3,
    "VS1": 4,
    "VS2": 5,
    "SI1": 6,
    "SI2": 7,
    "I1": 8
}
dataset['clarity'].replace(clarityReplaces, inplace=True)

#valores independentes
x = dataset[["carat", "cut", "color", "clarity"]]

#valor dependente
y = dataset[["price"]]

#Treinamento e testes
xTreino, xTeste, yTreino, yTeste = train_test_split(x, y, test_size=0.2)

regression = linear_model.LinearRegression()

regression.fit(xTreino, yTreino)

predDiamondPrice = regression.predict(xTeste)

#R² dos coeficientes
r2 = r2_score(yTeste, predDiamondPrice)

print(r2)

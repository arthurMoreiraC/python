import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# --- 1. Gerando dados simulados ---
# x varia de 0 a 10, com 100 pontos
x = np.linspace(0, 10, 100)
# relação quadrática com um pouco de ruído
y = 2 + 3*x - 0.5*x**2 + np.random.randn(100) * 2

# transforma x em formato de coluna (necessário para sklearn)
x = x.reshape(-1, 1)

# --- 2. Transformação polinomial ---
# grau do polinômio (2 = quadrático)
poly = PolynomialFeatures(degree=2)
x_poly = poly.fit_transform(x)

# --- 3. Regressão linear sobre os dados transformados ---
model = LinearRegression()
model.fit(x_poly, y)

# --- 4. Fazendo previsões ---
y_pred = model.predict(x_poly)

# --- 5. Visualizando ---
plt.scatter(x, y, color='blue', label='Dados reais')
plt.plot(x, y_pred, color='red', linewidth=2, label='Ajuste polinomial')
plt.title('Regressão Polinomial (grau 2)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

# --- 6. Mostrando a equação ajustada ---
coef = model.coef_
intercept = model.intercept_
print(f"Equação ajustada: y = {intercept:.2f} + ({coef[1]:.2f})x + ({coef[2]:.2f})x²")

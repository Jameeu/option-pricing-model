import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Black-Scholes function
def black_scholes(S, K, T, r, sigma):
    d1 = (np.log(S/K) + (r + sigma**2 / 2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    C = S*norm.cdf(d1) - K*np.exp(-r*T)*norm.cdf(d2)
    return C

# Parameters
S = 100  # stock price
K = 100  # strike price
T = 1    # time to maturity
r = 0.05 # interest rate

# Vary volatility
sigma_values = np.linspace(0.1, 0.5, 50)
prices = [black_scholes(S, K, T, r, sigma) for sigma in sigma_values]

# Plot
plt.plot(sigma_values, prices)
plt.xlabel("Volatility")
plt.ylabel("Option Price")
plt.title("Option Price vs Volatility")
plt.show()

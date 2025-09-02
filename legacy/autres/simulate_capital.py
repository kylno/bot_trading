import matplotlib.pyplot as plt

# Exemple de capital sur 10 jours
jours = list(range(1, 11))
capital = [1000, 1050, 1100, 1080, 1150, 1200, 1250, 1300, 1280, 1350]

plt.plot(jours, capital, marker='o')
plt.title("Évolution du capital")
plt.xlabel("Jour")
plt.ylabel("Capital (€)")
plt.grid(True)
plt.savefig("graphs/capital_curve.png")
plt.show()

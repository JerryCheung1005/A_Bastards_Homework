import matplotlib.pyplot as plt

month = list(range(1, 13))
money=[5.2, 2.7, 5.8, 5.7, 7.3, 9.2, 18.7, 15.6, 20.5, 18, 7.8, 6.9]

plt.plot(month, money, 'r-.')
plt.scatter(month, money, c='b', marker='v', s=28)
plt.xlabel('month', fontsize=14)
plt.ylabel('money', fontsize=14)
plt.title('The revenue Trend of BBQ shop in 2019', fontsize=18)
plt.tight_layout()
plt.show()


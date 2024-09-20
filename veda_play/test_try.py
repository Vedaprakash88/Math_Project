from matplotlib import pyplot as plt

x = ['Requirements', 'Design', 'V&V', 'Production', 'Customer Use']
r = list(range(0, 5))

y = [2**a for a in r]

plt.plot(x, y)
plt.tick_params(left=False, labelleft=False)
plt.ylabel('Cost (€) to Fix', loc='top')
plt.savefig("sys.JPEG", bbox_inches='tight', dpi=1200)
plt.show()
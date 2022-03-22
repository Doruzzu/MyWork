import numpy as np
import numpy_financial as npf
import pandas as pd
import matplotlib.pyplot as plt


yields = np.arange(0, 10, 0.1)

bonds = pd.DataFrame(yields, columns=['bond_yields'])

price = -npf.pv(rate=0.05, nper=20, pmt=5, fv=100)

price_up = -npf.pv(rate=0.05+0.01, nper=20, pmt=5, fv=100)
price_down = -npf.pv(rate=0.05-0.01, nper=20, pmt=5, fv=100)

duration = (price_down - price_up)/(2 * price * 0.01)

bonds['changed_yields'] = bonds['bond_yields'] - 5
bonds['price'] = -npf.pv(rate=bonds['bond_yields']/100, nper=20, pmt=5,  fv=100)

dollar_duration = duration * price * 0.01

bonds['price_change'] = -100 * dollar_duration * bonds['changed_yields']/100

bonds['price_approximation'] = price + bonds['price_change']

plt.plot(bonds['bond_yields'], bonds['price'])
plt.plot(bonds['bond_yields'], bonds["price_approximation"])
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

pd.options.display.max_rows = 100000

df = pd.read_csv(r"E:\UR\Math\203\Project\data\1.csv")

print(df.info()) 

df.plot(kind="hist",x="Annual Income",y="Price ($)",density=True)

df.boxplot(by="Body Style",column=['Annual Income'],grid=False)

m=df['Annual Income'].to_numpy()

n=pd.qcut(m,5)

df=df.groupby([n,'Body Style']).size()
df=df.unstack()
df.plot(kind='bar')

df = pd.read_csv(r"E:\UR\Math\203\Project\data\1.csv")

df=df.groupby(["Dealer_Region",'Body Style']).size()
df=df.unstack()
df.plot(kind='bar')
df.plot()

plt.show()
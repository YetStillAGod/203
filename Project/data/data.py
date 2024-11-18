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
c_1=round(df.corr(),2)

df = pd.read_csv(r"E:\UR\Math\203\Project\data\1.csv")

df=df.groupby(["Dealer_Region",'Body Style']).size()
df=df.unstack()
df.plot(kind='bar')
df.plot()
c_2=round(df.corr(),2)

print(c_1)
print(c_2)

df = pd.DataFrame({"Dealer Region":["Aurora","Austin","Greenville","Janesville","Middletown","Pasco","Scottsdale"],"Frequency":[3130,4135,3128,3821,3128,3131,3433]})
df.plot(x="Dealer Region",y="Frequency",kind="bar")

df = pd.DataFrame({"Car Model":["Passenger","Sedan","Hatchback","SUV","Hardtop"],"Frequency":[3945,4488,6128,6374,2970]})
df.plot(x="Car Model",y="Frequency",kind="bar")


plt.show()

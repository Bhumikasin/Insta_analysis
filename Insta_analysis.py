import pandas as pd
import numpy as  np
import matplotlib.pyplot as plt
df = pd.read_csv(r"C:\Users\Administrator\Downloads\Telegram Desktop\ig.csv")
time_diff=np.diff(df["Time"],n=1)
likes_diff=np.diff(df["Likes"],n=1)

q80=np.percentile(likes_diff,q=80)
q20=np.percentile(likes_diff,q=20)



plt.plot(df["Time"][1:],likes_diff,marker="o",color="black",mfc="blue")
plt.axhline(q80,color="green",ls="--")
plt.axhline(q20,color="red",ls="--")
#print(f"mean: {np.mean(time_diff)}")
#print(f"median: {np.median(time_diff)}")

#q=np.percentile(time_diff,q=90)
#print(q)
#plt.hist(time_diff,color="darkcyan")
#plt.axvline(q,color="darkgreen",ls="--")
#plt.text(11,33,"90th percentile")
plt.show()

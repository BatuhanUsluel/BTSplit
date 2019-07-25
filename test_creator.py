import pandas as pd
import numpy as np
df = pd.DataFrame(columns=['Index'])
df['Index'] = range(1, 10000)#1500000
df.to_csv("random.csv", sep=',', index=False, header=False)
import random
import pandas as pd
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()

uniq = data['whoAmI'].unique()
one_hot_data = pd.DataFrame()
for value in uniq:
    one_hot_data[value] = (data['whoAmI'] == value).astype(int)
one_hot_data.head()
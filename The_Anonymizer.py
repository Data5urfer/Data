import pandas as pd
import numpy as np

# Create a dummy data frame, just for testing:
A=pd.DataFrame({'Email':['email0@email.com','amail1@email.net','email2@email.something','amail1@email.net'],
                'OtherData':[0,'af4',96,'foo']})
pid=np.array([0 for i in range(len(A))])

# Shuffle the data frame
A=A.sample(frac=1)

# Assign a preliminary ID to every entry in the 'Email' serie:
for a in range(1,len(A['Email'])):
    if A['Email'][:a].isin([A['Email'][a]]).any():
        pid[a]=np.where(A['Email'][:3].isin([A['Email'][3]]))[0][0]
    else:
        pid[a]=a

# Apply anonymization rule of your choice (depends on datatype):
A['Email']=A['Email'].apply(lambda x: sum(map(ord,x)))
B=A['Email']

# Exclude possible repetitions:
for h in range(len(A['Email'])):
    A['Email'][h]=int(str(B[h])+str(pid[h]))

# Shuffle the data frame
A=A.sample(frac=1)

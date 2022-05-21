import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import preprocessing

data = pd.read_csv('training_cases.csv')

X = data.drop(columns=['mood'])
y_1 = data['mood']

lab1 = preprocessing.LabelEncoder()
y = lab1.fit_transform(y_1).T

model = DecisionTreeClassifier()

model.fit(X, y)
model.predict([["""You fill me up 'til you're empty
I took too much and you let me
We've been down all these roads before
And what we found don't live there anymore
It's dark
It's cold
If my hand is not the one you're meant to hold
Maybe you'd be happier with someone else
Maybe loving me's the reason you can't love yourself
Before I turn your heart into a ghost town
Show me everything we built so I can tear it all down
Down
Down, down, down
You know I'll stay don't you tempt me
But all this weight is getting heavy
Been holding up what wasn't meant to stand
I turned this love into a wasteland
It's dark
It's cold
If my hand is not the one you're meant to hold
Maybe you'd be happier with someone else
Maybe loving me's the reason you can't love yourself
Before I turn your heart into a ghost town
Show me everything we built so I can tear it all down
Down
Down, down, down
Tear it all down
Down
Down, down, down
The streets are empty
Where love once was but it's faded away
These broken memories
I'm left here alone and afraid to say
Maybe you'd be happier with someone else
Oh-oh-oh
Maybe you'd be happier with someone else
Maybe loving me's the reason you can't love yourself
Before I turn your heart into a ghost town
Show me everything we built so I can tear it all down
Down
Down, down, down
Tear it all down
Down
Down, down, down
I'll tear it all down
I'll tear it all down""", 'BENSON_BOONE']])

print(y)
print(X)

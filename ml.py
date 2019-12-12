'''import numpy as np
import pandas as pd
df=pd.read_csv("Diabetes_Dataset.csv")
X=df.drop("Outcome",axis=1)
y=df['Outcome']
from sklearn.linear_model import LogisticRegression
model=LogisticRegression()
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.30,random_state=42)
model.fit(X_train,y_train)
model.score(X_test,y_test)'''


def pr(preg,glu,blood,skin,ins,bmi,pdf,age):
    import numpy as np
    import pandas as pd
    df=pd.read_csv("Diabetes_Dataset.csv")
    X=df.drop("Outcome",axis=1)
    y=df['Outcome']
    from sklearn.linear_model import LogisticRegression
    model=LogisticRegression()
    from sklearn.model_selection import train_test_split
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.30,random_state=42)
    model.fit(X_train,y_train)
    model.score(X_test,y_test)

    a=0
    l=pd.DataFrame((np.array([preg,glu,blood,skin,ins,bmi,pdf,age])).reshape(1,-1))
    a=model.predict(l)
    a=int(a)
    return a

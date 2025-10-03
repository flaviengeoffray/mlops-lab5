def build_linear_model():
    import pandas as pd 
    from sklearn.linear_model import LinearRegression
    import joblib
    df = pd.read_csv('houses.csv')
    X = df[['size', 'nb_rooms', 'garden']]
    y = df['price']
    model = LinearRegression()
    model.fit(X, y)
    joblib.dump(model, "regression.joblib")

build_linear_model()

def build_tree_model():
    import pandas as pd 
    from sklearn.tree import DecisionTreeRegressor
    import joblib
    df = pd.read_csv('houses.csv')
    X = df[['size', 'nb_rooms', 'garden']]
    y = df['price']
    model = DecisionTreeRegressor(max_depth=3)
    model.fit(X, y)
    joblib.dump(model, "tree_model.joblib")

build_tree_model()

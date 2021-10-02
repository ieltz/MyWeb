import pandas as pd

ie = pd.read_csv('iris.csv')

ie.to_html('irishy.html')

import panda as pd

#creating series
s = pd.Series([1,2,3,4,5] , name="numbers")

print(s)

#creating DataFrame

df = pd.DataFrame({
    "A":[1,2,3],
    "B":["a","b","c"],
    "C":[4.5,5.5,6.5]
})

print(df)

#functions in panda:

#read_csv("file.csv")->reads a csv(comma seperated values) file into a DataFrame

#head(n) / tail(n) -> displays the first or last n rows

#sort_values("column") -> sorts data based on a column
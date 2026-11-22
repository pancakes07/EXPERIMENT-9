import pandas as pd

data = {
        
        "Name": ["Rahul", "Aman", "Priya", "Sneha"],
        
        "Marks": [75, 88, 92, 65],
        
        "Phoneno": [9876543210, 8765432109, 9988776655, 9123456780],
        
        "USN": ["01BCAR101", "01BCAR102", "01BCAR103", "01BCAR104"],
        
        "loc": ["KA", "MH", "TN", "AP"]
        
}

df = pd.DataFrame(data)
print(df)

print("Head \n", df.head())
print("Tail \n",df.tail())
print("Info \n",df.info())
print("Describe \n", df.describe())
print("Sorted",df.sort_values("Marks"))

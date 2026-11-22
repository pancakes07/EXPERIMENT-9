import numpy as np

arr = np.array([45, 120, 78, 250, 95, 183, 49, 166, 203, 113])

arr[[2,5,8]] = 99
sorted_arr = np.sort(arr)

print(sorted_arr)


print("Array:",arr)
print("Minimum :", min(arr))
print("Maximun:", max(arr))
print("Accessing Element :",arr[1:5])
print("Sum", sum(sorted_arr))


a = np.array(
    [
        ('RAHUL', 3, 25.0),
        ('AMAN', 5, 35.0),
        ('PRIYA', 4, 29.0)
    ],
    dtype=[
        ('name', np.str_, 10),
        ('age', np.int32),
        ('weight', np.float64)
    ]
)

inputs = []

for i in range(10):
    value = input("Enter a string value: ")
    inputs.append(value)

unique_inputs = set(inputs)

print("Unique values (no repeats):")
for item in unique_inputs:
    print(item)
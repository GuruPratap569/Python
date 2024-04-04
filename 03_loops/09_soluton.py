items = ['apple', 'banana', 'orange','apple', 'mango']

unique_item = set()  # set koi v duplicate value nii store krta hai.

for item in items:
    if item in unique_item:
        print("Duplicate item is :", item)
        break
    unique_item.add(item)
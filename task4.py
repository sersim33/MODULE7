def data_preparation(data):
    cleaned_data = []
    for sublist in data:
        if len(sublist) > 2:
            sublist.remove(max(sublist))
            sublist.remove(min(sublist))
        cleaned_data.extend(sublist)
    return sorted(cleaned_data, reverse=True)
    print(cleaned_data)

data_preparation([[1, 2, 3], [3, 4], [5, 6]])

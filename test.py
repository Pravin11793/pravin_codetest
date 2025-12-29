def sort_by_path(data, path):
    keys = path.split(".")
    array_key = keys[0]
    sort_key = keys[1]

    if array_key not in data or not isinstance(data[array_key], list):
        raise ValueError("Invalid path or data structure")

    data[array_key] = sorted(data[array_key], key=lambda x: x.get(sort_key, ""))
    return data

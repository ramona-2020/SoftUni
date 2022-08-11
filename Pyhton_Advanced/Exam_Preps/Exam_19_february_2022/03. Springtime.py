

def start_spring(**kwargs):
    result = []
    collection_types = {}
    for name, c_type in kwargs.items():
        if c_type not in collection_types:
            collection_types[c_type] = [name]
        else:
            collection_types[c_type].append(name)

    collection_types_sorted = dict(sorted(collection_types.items(), key=lambda kv: (-len(kv[1]), kv[0])))
    for key, values in collection_types_sorted.items():
        values_sorted = sorted(values)
        result.append(f"{key}:")
        for value in values_sorted:
            result.append(f"-{value}")

    return "\n".join(result)

# Test Code:
example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))
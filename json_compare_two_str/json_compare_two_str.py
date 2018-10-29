import json


def dict_compare(d1, d2):
    d1_keys = set(d1.keys())
    d2_keys = set(d2.keys())
    intersect_keys = d1_keys.intersection(d2_keys)
    added = d1_keys - d2_keys
    removed = d2_keys - d1_keys
    modified = set(o for o in intersect_keys if d1[o] != d2[o])
    same = set(o for o in intersect_keys if d1[o] == d2[o])
    return added, removed, modified, same


json_string_1 = input()
json_string_2 = input()

# распарсенная строка
parsed_string_1 = json.loads(json_string_1)
parsed_string_2 = json.loads(json_string_2)
print(parsed_string_1)
print(parsed_string_2)
added, removed, modified, same = dict_compare(parsed_string_1, parsed_string_2)
for i in added:
    print('\"', i, '\": ', parsed_string_2[i], sep='')
for i in removed:
    print('\"', i, '\": ', parsed_string_1[i], sep='')
for i in modified:
    print('\"', i, '\": ', parsed_string_1[i], sep='')
    print('\"', i, '\": ', parsed_string_2[i], sep='')

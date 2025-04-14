"""Example of how to use list comprehensions
https://towardsdatascience.com/python-for-data-engineers-f3d5db59b6dd/"""

import json

def etl(item):
    # we would do transformations here
    return json.dumps(item)

# Text file loaded as a blob
blob = """
        [
{"id":"1","first_name":"John"},
{"id":"2","first_name":"Mary"}
]
"""
json_data = json.loads(blob)

# get that data using a loop
data_str = []
for item in json_data:
    data_str.append(etl(item))
print('using a loop')
print(data_str)

# now get that same data using a list comprehension instead
# data_str = u"\n".join(etl(item) for item in json_data)
data_str = [etl(item) for item in json_data]
print('\nusing a list comprehension')
print(data_str)

# # This data file is ready for BigQuery as Newline delimited JSON
# data_file = io.BytesIO(data_str.encode())
# print(data_file)
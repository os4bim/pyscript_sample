import json

tup_gmao = ()
with open("df_class_category.csv", encoding='latin-1') as fh:
    for line in fh:
        tup_gmao += (tuple(line.split(",")),)

json_string = json.dumps(tup_gmao)
print(json_string)


with open('class_categ.json', 'w') as outfile:
    outfile.write(json_string)
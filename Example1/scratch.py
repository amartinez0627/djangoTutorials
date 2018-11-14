import json

version= "ERP102100"
version_number = version[-3:]
switched_variables ={}
with open("variables.json","r") as read_file:
    data = json.load(read_file)
for variable in data[version_number]:
    switched_variables[variable] =data[version_number][variable]
# outputFromat = data[version_number]['outputFromat']
# addOperation = data[version_number]['addOperation']
# wbsDropdown = data[version_number]['wbsDropdown']
# wbsSelect1 = data[version_number]['wbsSelect1']
read_file.close()
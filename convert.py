import pandas as pd
df = pd.read_csv (r'shopping_data.csv', header=None)

file = open("shopping_data.json" , "w+")
for row in range(0,len(df)):
	instance = df.loc[row].values
	instance = list(instance)
	json_instance ="{\"index\":{\"_index\": \"data\",\"_type\":\"item\",\"_id\":"+str(row+1)+"}}\n"
	file.write(json_instance)
	json_instance = "{\"fields\" : { \"item\" : ["
	for x in range(0,len(instance)) :
		if not str(instance[x]) == "nan":
			json_instance += "\""+str(instance[x])+"\","
	json_instance+=  "]} ,\"id\" : \""+str(row)+"\",\"type\" : \"add\"}\n"
	file.write(json_instance)



"""json_instance = "{\"fields\" : {"
	for x in range(0,len(instance)) :
		if not str(instance[x]) == "nan":
			json_instance += "\"item"+str(x)+"\" : \""+str(instance[x])+"\","
	json_instance+=  "} ,\"id\" : \""+str(row)+"\",\"type\" : \"add\"}\n"""
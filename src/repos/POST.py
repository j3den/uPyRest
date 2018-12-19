import daos.POSTDao as pd
import json

def persist(request):
	print("POST REPO")
	parts = request.split("\\r\\n")
	#Id the model via the URL
	model = parts[0].split("/")[1].replace(" HTTP","")
	body = ""
	parts = request.split("\\r\\n")
	for i in range(0,len(parts)):
		if(str(parts[i]) == ""): #Look for empty line...Following is body.
			print(str(parts[i+1][:-1]) + "\n")
			jsonAsDict = json.loads(str(parts[i+1][:-1]))
	print("POSTING a "+model)
	return pd.postToFile(model,jsonAsDict)
	


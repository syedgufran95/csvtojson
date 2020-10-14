

import csv
import json

	
import glob


def make_json(csvfilepath,jsonfilepath):
	data={}
	
	for f in glob.iglob(csvfilepath+"/*.csv"):
		with open(f,encoding='utf-8') as csvf:
			print(f)
			csvreader=csv.DictReader(csvf)
			for index,row in enumerate(csvreader):
				condition=row["condition"]
				condition_cui=row["condition_cui"]
				if(index==0):
					data[condition]={}
					data[condition]["cui"]=condition_cui
					data[condition]["have_had"]={}
					data[condition]["looking_for"]={}

				data[condition][row["label_bucket"]][row["label"]]={}
				data[condition][row["label_bucket"]][row["label"]]["cui"]=row["label_cui"]
				data[condition][row["label_bucket"]][row["label"]]["score"]=row["label_score"]
				data[condition][row["label_bucket"]][row["label"]]["label_semantic_types"]=row["label_semantic_types"]
				data[condition][row["label_bucket"]][row["label"]]["label_ncts_counts"]=row["label_ncts_count"]
				data[condition][row["label_bucket"]][row["label"]]["ncts"]=row["label_ncts"]
	with open(jsonfilepath,'w',encoding='utf-8') as f:
		f.write(json.dumps(data,sort_keys=True,indent=4))
	


			#print(data)

csvfilepath=r'routput'
jsonfilepath=r'hello99.json'
make_json(csvfilepath,jsonfilepath)
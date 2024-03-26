import os, json, glob
promt_path = ""
inputfolder_path = "/PythonOpenAIBot/English/"
outputfoler_path = ""

# get input file from folder
for filename in glob.glob(os.path.join(inputfolder_path, '*.json')):#two path join together
   with open(os.path.join(os.getcwd(), filename), 'r') as f: #'r' ->open in readonly mode
    #getcwd get current path
    input_json_data = json.load(f)

# get promt file
    
with open('') as f:
  promt_data = json.load(f)

  with open("tmp.json","w") as outfile:#output translated json with indent
    json.dump(data,outfile,indent=4)
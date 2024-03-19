import os, json, glob
promt_path = ""
inputfolder_path = ""
outputfoler_path = ""

# get input file from folder
for filename in glob.glob(os.path.join(inputfolder_path, '*.json')):#two path join together
   with open(os.path.join(os.getcwd(), filename), 'r') as f: #'r' ->open in readonly mode
    #getcwd get current path
    input_json_data = json.load(f)

# get promt file
    
with open('') as f:
  promt_data = json.load(f)
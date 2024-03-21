import spacy
import os 
import json
from google.cloud import vision
import io
import argparse

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="key.json"

parser = argparse.ArgumentParser()
parser.add_argument("--modelDir", help="Path to model files", default="models/ner_model_90")
parser.add_argument("--fileType", help="type of file, img or txt", default="img")
parser.add_argument("--file", help="path of img or text file", default="testimages/1.jpg")
args = parser.parse_args()

client = vision.ImageAnnotatorClient()

nlp = spacy.load(args.modelDir)

def getOutput(type, data):
  
  textToPredict = ""
  if (type == "img"):
    with io.open(data, 'rb') as image_file:
        content = image_file.read()
        image = vision.types.Image(content=content)
        text_response = client.text_detection(image=image)
        texts = [text.description for text in text_response.text_annotations]
        textToPredict = texts[0]
  else:
    f = open(data, "r")
    textToPredict = f.read()
  doc = nlp(textToPredict)
  max_amt = 0
  i = 1
  data = {}
  items_list = []
  for ent in doc.ents:
    if (ent.label_ == "Total bill amount"):
      try:
        amt = float(ent.text)
        if amt > max_amt:
          data["Total bill amount"] = amt
      except Exception as e:
        pass
    elif (ent.label_ == "Items"):
      try:
        items_list.append(ent.text)
      except Exception as e:
        print(e)
    else:
      if ent.label_ in data.keys():
        data[ent.label_+"-"+str(i)] = ent.text
        i +=1
      else:
        data[ent.label_] = ent.text
  data["Items"]=items_list
  data = dict(sorted(data.items()))
  output=(json.dumps(data, indent=2))
  with open('output.json', 'w') as writer:
    writer.write(output)

getOutput(args.fileType, args.file)
import random
import json
import torch
import os
import sys
from Brain import NeuralNet
from NeuralNetwork import bag_of_words, tokenize
from Task import NonInputExecution
from Task import InputExecution_ms_word
device=torch.device('cuda' if torch.cuda.is_available() else 'cpu')
# with open("intents.json","r") as json_data:
#     intents=json.load(json_data)
file =open(os.path.join(sys.path[0], "intents.json"), "r")
intents = json.load(file)

FILE="TrainData.pth"
data=torch.load(FILE)

input_size=data["input_size"]
hidden_size=data["hidden_size"]
output_size=data["output_size"]
all_words=data["all_words"]
tags=data["tags"]
model_state=data["model_state"]

model=NeuralNet(input_size,hidden_size,output_size).to(device)
model.load_state_dict(model_state)
model.eval()

#-------------------------
Name="My Voice Assistant"
from Listen import Listen
from Speak import speak
def Main():
    sentence1=Listen()
    if sentence1=="bye":
        exit()
    sentence=tokenize(sentence1)
    X=bag_of_words(sentence,all_words)
    X=X.reshape(1,X.shape[0])
    X=torch.from_numpy(X).to(device)

    output=model(X)
    _,predicted=torch.max(output,dim=1)
    tag=tags[predicted.item()]
    probs=torch.softmax(output,dim=1)
    prob=probs[0][predicted.item()]
    if prob.item()>0.75:
        for intent in intents["intents"]:
            if tag==intent["tag"]:
                reply=random.choice(intent["responses"]) 
                if "time" in reply:
                    NonInputExecution(reply)
                elif "date" in reply:
                    NonInputExecution(reply)
                elif "word" in reply:
                    InputExecution_ms_word(reply,sentence1)
                elif "start writing" in reply:
                    InputExecution_ms_word(reply,sentence1)
                elif "save document" in reply:
                    InputExecution_ms_word(reply,sentence1)
                elif "close document" in reply:
                    InputExecution_ms_word(reply,sentence1)
                elif "align left" in reply:
                    InputExecution_ms_word(reply,sentence1)
                elif "align centre" in reply:
                    InputExecution_ms_word(reply,sentence1)
                elif "align right" in reply:
                    InputExecution_ms_word(reply,sentence1)
                elif "justify" in reply:
                    InputExecution_ms_word(reply,sentence1)
                elif "scroll down" in reply:
                    InputExecution_ms_word(reply,sentence1)
                elif "select the previous word" in reply:
                    InputExecution_ms_word(reply,sentence1)
                elif "select the next paragraph" in reply:
                    InputExecution_ms_word(reply,sentence1)
                elif "select all text" in reply:
                    InputExecution_ms_word(reply,sentence1)
                elif "deselect everything" in reply:
                    InputExecution_ms_word(reply,sentence1)  
                elif "find" in reply:
                    InputExecution_ms_word(reply,sentence1)
                elif "replace" in reply:
                    InputExecution_ms_word(reply,sentence1) 
                elif "start spell check" in reply:
                    InputExecution_ms_word(reply,sentence1)
                elif "ignore this word" in reply:
                    InputExecution_ms_word(reply,sentence1)
                elif "change misspelled to corrected" in reply:
                    InputExecution_ms_word(reply,sentence1)

                # Lists and Bullets
                elif "start numbered list" in reply:
                    InputExecution_ms_word(reply,sentence1)
                elif "start bulleted list" in reply:
                    InputExecution_ms_word(reply,sentence1)


            #font formatting
                elif "increase font size" in reply:
                    InputExecution_ms_word(reply,sentence1) 
                elif "bold text" in reply:
                    InputExecution_ms_word(reply,sentence1)
                elif "italicize this" in reply:
                    InputExecution_ms_word(reply,sentence1)
                elif "underline the selected text" in reply:
                    InputExecution_ms_word(reply,sentence1)
                elif "change font to arial" in reply:
                    InputExecution_ms_word(reply,sentence1)
                elif "change font to times new roman" in reply:
                    InputExecution_ms_word(reply,sentence1)
                elif "change font size to 12" in reply:
                    InputExecution_ms_word(reply,sentence1)
                elif "change font size to 16" in reply:
                    InputExecution_ms_word(reply,sentence1)
            

            #text formatting
                elif "cut this" in reply:
                    InputExecution_ms_word(reply,sentence1)
                elif "copy the selection" in reply:
                    InputExecution_ms_word(reply,sentence1)
                elif "paste" in reply:
                    InputExecution_ms_word(reply,sentence1)
                elif "undo the last action" in reply:
                    InputExecution_ms_word(reply,sentence1)
                elif "redo" in reply:
                    InputExecution_ms_word(reply,sentence1)
                elif "go to the beginning of the line" in reply:
                    InputExecution_ms_word(reply,sentence1)
                elif "go to the end of the document" in reply:
                    InputExecution_ms_word(reply,sentence1) 



            #table insertion
                elif "insert a table" in reply:
                    InputExecution_ms_word(reply,sentence1)
                elif "insert a table with rows and columns" in reply:
                    InputExecution_ms_word(reply,sentence1)              

            #formatting of table
                elif "format the table" in reply:
                    InputExecution_ms_word(reply,sentence1)
                elif "format the image" in reply:
                    InputExecution_ms_word(reply,sentence1)
                elif "change background color to yellow" in reply:
                    InputExecution_ms_word(reply,sentence1)
                elif "highlight selected text" in reply:
                    InputExecution_ms_word(reply,sentence1)
                elif "add borders to selection" in reply:
                    InputExecution_ms_word(reply,sentence1)
                elif "set table borders" in reply:
                    InputExecution_ms_word(reply,sentence1)
                elif "apply table style" in reply:
                    InputExecution_ms_word(reply,sentence1)
                elif "change cell background color" in reply:
                    InputExecution_ms_word(reply,sentence1)
                elif "change text color" in reply:
                    InputExecution_ms_word(reply,sentence1)
                elif "adjust column width" in reply:
                    InputExecution_ms_word(reply,sentence1)
                elif "adjust row height" in reply:
                    InputExecution_ms_word(reply,sentence1)
                elif "merge cells" in reply:
                    InputExecution_ms_word(reply,sentence1)
                elif "split cells" in reply:
                    InputExecution_ms_word(reply,sentence1)


                #insertion of image      
                elif "insert an image from file" in reply:
                    InputExecution_ms_word(reply,sentence1)
                #formatting of image        
                elif "format the image" in reply:
                    InputExecution_ms_word(reply,sentence1)
                elif "set image border" in reply:
                    InputExecution_ms_word(reply,sentence1)
                elif "change image size" in reply:
                    InputExecution_ms_word(reply,sentence1)
                elif "crop the image" in reply:
                    InputExecution_ms_word(reply,sentence1)
                elif "apply image effects" in reply:
                    InputExecution_ms_word(reply,sentence1)
                elif "rotate the image" in reply:
                    InputExecution_ms_word(reply,sentence1)
                elif "change image brightness" in reply:
                    InputExecution_ms_word(reply,sentence1)
                elif "adjust image contrast" in reply:
                    InputExecution_ms_word(reply,sentence1)
                elif "compress the image" in reply:
                    InputExecution_ms_word(reply,sentence1)
                elif "reset image formatting" in reply:
                    InputExecution_ms_word(reply,sentence1)              


            #insertion of list,hyperlink and shapes
                elif "create a bulleted list" in reply:
                    InputExecution_ms_word(reply,sentence1)
                elif "add a comment here" in reply:
                    InputExecution_ms_word(reply,sentence1)
                elif "insert a hyperlink" in reply:
                    InputExecution_ms_word(reply,sentence1)   
                elif "insert a rectangle shape" in reply:
                    InputExecution_ms_word(reply,sentence1)
                elif "insert an oval shape" in reply:
                    InputExecution_ms_word(reply,sentence1)
                elif "insert a triangle shape" in reply:
                    InputExecution_ms_word(reply,sentence1)
                elif "insert a star shape" in reply:
                    InputExecution_ms_word(reply,sentence1)
                elif "insert a line shape" in reply:
                    InputExecution_ms_word(reply,sentence1)
                elif "insert a callout shape" in reply:
                    InputExecution_ms_word(reply,sentence1)
                elif "change background color to yellow" in reply:
                    InputExecution_ms_word(reply,sentence1)
                elif "highlight selected text" in reply:
                    InputExecution_ms_word(reply,sentence1)
                elif "add borders to selection" in reply:
                    InputExecution_ms_word(reply,sentence1)
                #view reply,sentence1s    
                elif "switch to print layout view" in reply:
                    InputExecution_ms_word(reply,sentence1)
                elif "switch to read mode" in reply:
                    InputExecution_ms_word(reply,sentence1)
                elif "switch to web layout view" in reply:
                    InputExecution_ms_word(reply,sentence1)
                elif "switch to outline view" in reply:
                    InputExecution_ms_word(reply,sentence1)
                elif "switch to draft view" in reply:
                    InputExecution_ms_word(reply,sentence1)
                elif "go to the design tab" in reply:
                    InputExecution_ms_word(reply,sentence1)

                # Design Tab Options
                elif "change page color" in reply:
                    InputExecution_ms_word(reply,sentence1)

                elif "apply page borders" in reply:
                    InputExecution_ms_word(reply,sentence1)

                elif "add watermark" in reply:
                    InputExecution_ms_word(reply,sentence1)

                elif "change theme" in reply:
                    InputExecution_ms_word(reply,sentence1)

                elif "go to the insert tab" in reply:
                    InputExecution_ms_word(reply,sentence1)

                # Insert Header
                elif "insert header" in reply:
                    InputExecution_ms_word(reply,sentence1)

                # Insert Footer
                elif "insert footer" in reply:
                    InputExecution_ms_word(reply,sentence1)   

                
                # Format Header
                elif "format header" in reply:
                    InputExecution_ms_word(reply,sentence1)

                # Format Footer
                elif "format footer" in reply:
                    InputExecution_ms_word(reply,sentence1)       
                elif "close word" in reply:
                    InputExecution_ms_word(reply,sentence1)
                elif "save document" in reply:
                    InputExecution_ms_word(reply,sentence1)
                elif "close document" in reply:
                    InputExecution_ms_word(reply,sentence1)
                elif "open document" in reply:
                    InputExecution_ms_word(reply,sentence1)
                elif "new document" in reply:
                    InputExecution_ms_word(reply,sentence1)
                else:
                    speak(reply)

while True:
    Main()
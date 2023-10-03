import datetime
from Speak import speak
import pyttsx3
import os
import speech_recognition as sr
import pyautogui
import time
def Time():
    time=datetime.datetime.now().strftime("%H pass %M minutes %S seconds")
    speak(f"the time is {time}")
def Date():
    date=datetime.datetime.now().strftime("%d of %B %Y")
    speak(f"the date is {date}")

def ms_word(command):
    recognizer = sr.Recognizer()
    engine = pyttsx3.init()
    recognizer.energy_threshold = 4000
    if "start word" in command:
         pyautogui.press('win')
         time.sleep(1)
         search_query = "Word"
         pyautogui.write(search_query, interval=0.1)
         time.sleep(2)
         pyautogui.press('enter')
         time.sleep(5) 
    elif "start writing" in command:
        engine.say("Initializing typing")
        engine.runAndWait()
        with sr.Microphone() as source: 
         while True:
            audio = recognizer.listen(source)
            try:      
                text = recognizer.recognize_google(audio).lower()

                if "stop writing" in text:
                    engine.say("Stopping writing")
                    engine.runAndWait()
                    break
                pyautogui.typewrite(text)

            except sr.UnknownValueError:
                pass
    elif "save document" in command:
        pyautogui.hotkey("ctrl", "s")
    elif "close document" in command:
        pyautogui.hotkey("ctrl", "w")
    # Paragraph Formatting Commands
    elif "align left" in command:
        pyautogui.hotkey("ctrl", "l")  # Left-align text
    elif "align centre" in command:
        pyautogui.hotkey("ctrl", "e")  # Center-align text
    elif "align right" in command:
        pyautogui.hotkey("ctrl", "r")  # Right-align text
    elif "justify" in command:
        pyautogui.hotkey("ctrl", "j")  # Justify text
    elif "scroll down" in command:
        pyautogui.scroll(-3)  # Adjust the value as needed
    elif "select the previous word" in command:
        pyautogui.hotkey("ctrl", "left")
        pyautogui.hotkey("ctrl", "shift", "right")
    elif "select the next paragraph" in command:
        pyautogui.hotkey("ctrl", "down")
        pyautogui.hotkey("ctrl", "shift", "up")
    elif "select all text" in command:
        pyautogui.hotkey("ctrl", "a")
    elif "deselect everything" in command:
        pyautogui.click()   
    elif "find" in command:
        pyautogui.hotkey("ctrl", "f")  # Open the find dialog
    elif "replace" in command:
        pyautogui.hotkey("ctrl", "h")  # Open the replace dialog   
    elif "start spell check" in command:
        pyautogui.hotkey("f7")  # Start spell check (F7 key)  
    elif "ignore this word" in command:
        pyautogui.hotkey("ctrl", "d")  # Ignore the word
    elif "change misspelled to corrected" in command:
        pyautogui.hotkey("alt", "c")  # Activate "Change" button
        pyautogui.typewrite("corrected")  # Replace with "corrected"
        pyautogui.press("enter")  # Confirm change    


    # Lists and Bullets
    elif "start numbered list" in command:
        pyautogui.hotkey("alt", "h", "n")  # Start numbered list
    elif "start bulleted list" in command:
        pyautogui.hotkey("alt", "h", "u")  # Start bulleted list


#font formatting
    elif "increase font size" in command:
        pyautogui.hotkey("ctrl", ">")  # Increases the font size    
    elif "bold text" in command:
        pyautogui.hotkey("ctrl", "b")
    elif "italicize this" in command:
        pyautogui.hotkey("ctrl", "i")
    elif "underline the selected text" in command:
        pyautogui.hotkey("ctrl", "u")
    elif "change font to arial" in command:
        pyautogui.hotkey("ctrl", "d")  # Open the font dialog
        pyautogui.typewrite("Arial")
        pyautogui.press("enter")
    elif "change font to times new roman" in command:
        pyautogui.hotkey("ctrl", "d")  # Open the font dialog
        pyautogui.typewrite("Times New Roman")
        pyautogui.press("enter")
    elif "change font size to 12" in command:
        pyautogui.hotkey("ctrl", "shift", "p")  # Open the font size dialog
        pyautogui.typewrite("12")
        pyautogui.press("enter")
    elif "change font size to 16" in command:
        pyautogui.hotkey("ctrl", "shift", "p")  # Open the font size dialog
        pyautogui.typewrite("16")
        pyautogui.press("enter")    
   

   #text formatting
    elif "cut this" in command:
        pyautogui.hotkey("ctrl", "x")
    elif "copy the selection" in command:
        pyautogui.hotkey("ctrl", "c")
    elif "paste" in command:
        pyautogui.hotkey("ctrl", "v")
    elif "undo the last action" in command:
        pyautogui.hotkey("ctrl", "z")
    elif "redo" in command:
        pyautogui.hotkey("ctrl", "y")
    elif "go to the beginning of the line" in command:
        pyautogui.hotkey("ctrl", "home")
    elif "go to the end of the document" in command:
        pyautogui.hotkey("ctrl", "end")  



   #table insertion
    elif "insert a table" in command:
        pyautogui.hotkey("alt", "n", "t")  # Insert a table (Alt, N, T)
    elif "insert a table with rows and columns" in command:
        # Ask for the number of rows and columns
        pyautogui.hotkey("alt", "n", "t")  # Insert a table (Alt, N, T)
        # You may customize this part to ask for rows and columns via voice command
        rows = input("How many rows: ")
        columns = input("How many columns: ")
        pyautogui.typewrite(f"{rows}{' ' * 3}{columns}") 

#formatting of table
    elif "format the table" in command:
        pyautogui.hotkey("alt", "h", "ft")  # Format the table
    elif "format the image" in command:
        pyautogui.hotkey("alt", "h", "p")  # Format the image
    elif "change background color to yellow" in command:
        pyautogui.hotkey("alt", "h", "l", "k", "4")  # Change background color to yellow
    elif "highlight selected text" in command:
        pyautogui.hotkey("alt", "h", "l", "k", "5")  # Highlight selected text (adjust as needed)
    elif "add borders to selection" in command:
        pyautogui.hotkey("alt", "h", "b", "s")  # Add borders to the selection (adjust as needed)
    elif "set table borders" in command:
        pyautogui.hotkey("alt", "h", "b")  # Set table borders
    elif "apply table style" in command:
        pyautogui.hotkey("alt", "h", "t")  # Apply table style
    elif "change cell background color" in command:
        pyautogui.hotkey("alt", "h", "sh", "b")  # Change cell background color
    elif "change text color" in command:
        pyautogui.hotkey("alt", "h", "sh", "f")  # Change text color
    elif "adjust column width" in command:
        pyautogui.hotkey("alt", "h", "sh", "w")  # Adjust column width
    elif "adjust row height" in command:
        pyautogui.hotkey("alt", "h", "sh", "h")  # Adjust row height
    elif "merge cells" in command:
        pyautogui.hotkey("alt", "h", "sh", "m")  # Merge cells
    elif "split cells" in command:
        pyautogui.hotkey("alt", "h", "sh", "s")  # Split cells


    #insertion of image      
    elif "insert an image from file" in command:
        # Ask for the image file path via voice command
        pyautogui.hotkey("alt", "n", "p")  # Insert a picture (Alt, N, P)
        pyautogui.typewrite("Please enter the image file path:")
        audio = recognizer.listen(source)
        try:
            image_path = recognizer.recognize_google(audio).lower()
            if os.path.exists(image_path):
                pyautogui.typewrite(image_path)
                pyautogui.press("enter")
            else:
                print("The specified file path does not exist.")
        except sr.UnknownValueError:
            print("Could not understand the word")


    #formatting of image        
    elif "format the image" in command:
        pyautogui.hotkey("alt", "h", "p")  # Format the image
    elif "set image border" in command:
        pyautogui.hotkey("alt", "h", "s")  # Set image border
    elif "change image size" in command:
        pyautogui.hotkey("alt", "h", "si")  # Change image size
    elif "crop the image" in command:
        pyautogui.hotkey("alt", "h", "c")  # Crop the image
    elif "apply image effects" in command:
        pyautogui.hotkey("alt", "h", "fx")  # Apply image effects
    elif "rotate the image" in command:
        pyautogui.hotkey("alt", "h", "o")  # Rotate the image
    elif "change image brightness" in command:
        pyautogui.hotkey("alt", "h", "b")  # Change image brightness
    elif "adjust image contrast" in command:
        pyautogui.hotkey("alt", "h", "co")  # Adjust image contrast
    elif "compress the image" in command:
        pyautogui.hotkey("alt", "h", "p")  # Compress the image
    elif "reset image formatting" in command:
        pyautogui.hotkey("alt", "h", "e")  # Reset image formatting              


#insertion of list,hyperlink and shapes
    elif "create a bulleted list" in command:
        pyautogui.hotkey("ctrl", "shift", "l")  # Create a bulleted list
    elif "add a comment here" in command:
        pyautogui.hotkey("alt", "r", "c")  # Add a comment
    elif "insert a hyperlink" in command:
        pyautogui.hotkey("ctrl", "k")  #   
    elif "insert a rectangle shape" in command:
        pyautogui.hotkey("alt", "n", "sh", "r")  # Insert a rectangle shape
    elif "insert an oval shape" in command:
        pyautogui.hotkey("alt", "n", "sh", "o")  # Insert an oval shape
    elif "insert a triangle shape" in command:
        pyautogui.hotkey("alt", "n", "sh", "t")  # Insert a triangle shape
    elif "insert a star shape" in command:
        pyautogui.hotkey("alt", "n", "sh", "s")  # Insert a star shape
    elif "insert a line shape" in command:
        pyautogui.hotkey("alt", "n", "sh", "l")  # Insert a line shape
    elif "insert a callout shape" in command:
        pyautogui.hotkey("alt", "n", "sh", "c")  # Insert a callout shape
    elif "change background color to yellow" in command:
        pyautogui.hotkey("alt", "h", "l", "k", "4")  # Change background color to yellow
    elif "highlight selected text" in command:
        pyautogui.hotkey("alt", "h", "l", "k", "5")  # Highlight selected text (adjust as needed)
    elif "add borders to selection" in command:
        pyautogui.hotkey("alt", "h", "b", "s")  # Add borders to the selection (adjust as needed)    


    #view commands    
    elif "switch to print layout view" in command:
        pyautogui.hotkey("alt", "w", "p")  # Switch to Print Layout view
    elif "switch to read mode" in command:
        pyautogui.hotkey("alt", "w", "r")  # Switch to Read Mode
    elif "switch to web layout view" in command:
        pyautogui.hotkey("alt", "w", "l")  # Switch to Web Layout view
    elif "switch to outline view" in command:
        pyautogui.hotkey("alt", "w", "n")  # Switch to Outline view
    elif "switch to draft view" in command:
        pyautogui.hotkey("alt", "w", "d")  # Switch to Draft view
    elif "go to the design tab" in command:
        pyautogui.hotkey("alt", "g", "c")  # Navigate to the Design Tab

    # Design Tab Options
    elif "change page color" in command:
        pyautogui.hotkey("alt", "j")  # Open Page Color menu
        pyautogui.hotkey("alt", "j", "p")  # Select Page Color option

    elif "apply page borders" in command:
        pyautogui.hotkey("alt", "j")  # Open Page Color menu
        pyautogui.hotkey("alt", "j", "b")  # Select Page Borders option

    elif "add watermark" in command:
        pyautogui.hotkey("alt", "j")  # Open Page Color menu
        pyautogui.hotkey("alt", "j", "w")  # Select Watermark option

    elif "change theme" in command:
        pyautogui.hotkey("alt", "j")  # Open Page Color menu
        pyautogui.hotkey("alt", "j", "t")  # Select Themes option 

    elif "go to the insert tab" in command:
        pyautogui.hotkey("alt", "n")  # Navigate to the Insert Tab

    # Insert Header
    elif "insert header" in command:
        pyautogui.hotkey("alt", "n", "h")  # Insert a header

    # Insert Footer
    elif "insert footer" in command:
        pyautogui.hotkey("alt", "n", "f")  # Insert a footer   

    
    # Format Header
    elif "format header" in command:
        pyautogui.hotkey("alt", "p")  # Navigate to the Header & Footer Tools
        pyautogui.hotkey("alt", "h", "o")  # Format header

    # Format Footer
    elif "format footer" in command:
        pyautogui.hotkey("alt", "p")  # Navigate to the Header & Footer Tools
        pyautogui.hotkey("alt", "f", "o")  # Format footer       
    elif "close word" in command:
        pyautogui.hotkey("alt", "f4")  # Close Word                 
#for opening,closing and making of new document
    elif "save document" in command:
        pyautogui.hotkey("ctrl", "s")
    elif "close document" in command:
        pyautogui.hotkey("ctrl", "w")
    elif "open document" in command:
        pyautogui.hotkey("ctrl", "o")        
    elif "new document" in command:
        pyautogui.hotkey("ctrl", "n")
         # Wait for the "New Document" dialog to appear (you can adjust the duration)
        pyautogui.sleep(2)

        # Select "Blank document" by simulating keyboard navigation (you may need to adjust the keys)
        pyautogui.press('right')  # Navigate down to "Blank document"
        pyautogui.press('enter')  # Select "Blank document"


def NonInputExecution(query):
    query=str(query)
    if "time" in query:
        Time()

    elif "date" in query:
        Date()


def InputExecution_ms_word(tag,command):
    command = str(command)
    if "word" in tag:
        ms_word(command)
    elif "start writing" in tag:
        ms_word(command)
    elif "save document" in tag:
        ms_word(command)
    elif "close document" in tag:
        ms_word(command)
        
    # Paragraph Formatting Commands
    elif "align left" in tag:
        ms_word(command)
    elif "align centre" in tag:
        ms_word(command)
    elif "align right" in tag:
        ms_word(command)
    elif "justify" in tag:
        ms_word(command)
    elif "scroll down" in tag:
        ms_word(command)
    elif "select the previous word" in tag:
        ms_word(command)
    elif "select the next paragraph" in tag:
       ms_word(command)
    elif "select all text" in tag:
        ms_word(command)
    elif "deselect everything" in tag:
        ms_word(command)  
    elif "find" in tag:
        ms_word(command)
    elif "replace" in tag:
        ms_word(command) 
    elif "start spell check" in tag:
        ms_word(command)
    elif "ignore this word" in tag:
        ms_word(command)
    elif "change misspelled to corrected" in tag:
        ms_word(command)

    # Lists and Bullets
    elif "start numbered list" in tag:
        ms_word(command)
    elif "start bulleted list" in tag:
        ms_word(command)


#font formatting
    elif "increase font size" in tag:
        ms_word(command) 
    elif "bold text" in tag:
        ms_word(command)
    elif "italicize this" in tag:
        ms_word(command)
    elif "underline the selected text" in tag:
        ms_word(command)
    elif "change font to arial" in tag:
        ms_word(command)
    elif "change font to times new roman" in tag:
        ms_word(command)
    elif "change font size to 12" in tag:
        ms_word(command)
    elif "change font size to 16" in tag:
       ms_word(command)
   

   #text formatting
    elif "cut this" in tag:
        ms_word(command)
    elif "copy the selection" in tag:
        ms_word(command)
    elif "paste" in command:
        ms_word(command)
    elif "undo the last action" in tag:
        ms_word(command)
    elif "redo" in command:
        ms_word(command)
    elif "go to the beginning of the line" in tag:
        ms_word(command)
    elif "go to the end of the document" in tag:
        ms_word(command) 



   #table insertion
    elif "insert a table" in tag:
        ms_word(command)
    elif "insert a table with rows and columns" in tag:
        ms_word(command)                       # yaha tak atharva

#formatting of table
    elif "format the table" in tag:
        ms_word(command)
    elif "format the image" in tag:
        ms_word(command)
    elif "change background color to yellow" in tag:
        ms_word(command)
    elif "highlight selected text" in tag:
        ms_word(command)
    elif "add borders to selection" in tag:
        ms_word(command)
    elif "set table borders" in tag:
        ms_word(command)
    elif "apply table style" in tag:
        ms_word(command)
    elif "change cell background color" in tag:
        ms_word(command)
    elif "change text color" in tag:
        ms_word(command)
    elif "adjust column width" in tag:
        ms_word(command)
    elif "adjust row height" in tag:
        ms_word(command)
    elif "merge cells" in tag:
        ms_word(command)
    elif "split cells" in tag:
        ms_word(command)


    #insertion of image      
    elif "insert an image from file" in tag:
        ms_word(command)
    #formatting of image        
    elif "format the image" in tag:
        ms_word(command)
    elif "set image border" in tag:
        ms_word(command)
    elif "change image size" in tag:
        ms_word(command)
    elif "crop the image" in tag:
        ms_word(command)
    elif "apply image effects" in tag:
        ms_word(command)
    elif "rotate the image" in tag:
        ms_word(command)
    elif "change image brightness" in tag:
        ms_word(command)
    elif "adjust image contrast" in tag:
        ms_word(command)
    elif "compress the image" in tag:
        ms_word(command)
    elif "reset image formatting" in tag:
        ms_word(command)              


#insertion of list,hyperlink and shapes
    elif "create a bulleted list" in tag:
        ms_word(command)
    elif "add a comment here" in tag:
        ms_word(command)
    elif "insert a hyperlink" in tag:
        ms_word(command)   
    elif "insert a rectangle shape" in tag:
        ms_word(command)
    elif "insert an oval shape" in tag:
        ms_word(command)
    elif "insert a triangle shape" in tag:
        ms_word(command)
    elif "insert a star shape" in tag:
        ms_word(command)
    elif "insert a line shape" in tag:
        ms_word(command)
    elif "insert a callout shape" in tag:
        ms_word(command)
    elif "change background color to yellow" in tag:
        ms_word(command)
    elif "highlight selected text" in tag:
       ms_word(command)
    elif "add borders to selection" in tag:
        ms_word(command)
    #view commands    
    elif "switch to print layout view" in tag:
        ms_word(command)
    elif "switch to read mode" in tag:
        ms_word(command)
    elif "switch to web layout view" in tag:
        ms_word(command)
    elif "switch to outline view" in tag:
        ms_word(command)
    elif "switch to draft view" in tag:
        ms_word(command)
    elif "go to the design tab" in tag:
        ms_word(command)

    # Design Tab Options
    elif "change page color" in tag:
        ms_word(command)

    elif "apply page borders" in tag:
        ms_word(command)

    elif "add watermark" in tag:
        ms_word(command)

    elif "change theme" in tag:
        ms_word(command)

    elif "go to the insert tab" in tag:
        ms_word(command)

    # Insert Header
    elif "insert header" in tag:
        ms_word(command)

    # Insert Footer
    elif "insert footer" in tag:
        ms_word(command)   

    
    # Format Header
    elif "format header" in tag:
        ms_word(command)

    # Format Footer
    elif "format footer" in tag:
        ms_word(command)       
    elif "close word" in tag:
        ms_word(command)
    elif "save document" in tag:
        ms_word(command)
    elif "close document" in tag:
        ms_word(command)
    elif "open document" in tag:
        ms_word(command)
    elif "new document" in tag:
        ms_word(command)
    
import speech_recognition as sr
import pyautogui
import time
import pyttsx3
import os
from Speak import speak
# Initialize the speech recognizer
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Adjust microphone sensitivity
recognizer.energy_threshold = 4000  # Adjust the value as needed

# # Function to execute voice commands
# def execute_voice_command(command):
#     # Your code to process the command goes here

#     # Example: You can make the system say that the command is complete
#     response = "Command complete: " + command
#     engine.say(response)
#     engine.runAndWait()

# Function to execute voice commands

def execute_voice_command(command):
    if "open word" in command:
        # Simulate pressing the Windows key
         pyautogui.press('win')

# Wait briefly to open the Start menu (you can adjust the duration as needed)
         time.sleep(1)

        # Replace 'path_to_word.exe' with the actual path to Microsoft Word on your system
         search_query = "Word"
        # You can adjust the interval
         pyautogui.write(search_query, interval=0.1)

        # Wait briefly for the search results to appear (you can adjust the duration)
         time.sleep(2)

     # Simulate pressing Enter to open the first result (Microsoft Word)
         pyautogui.press('enter')

       # Wait briefly for Microsoft Word to open (you can adjust the duration)
         time.sleep(5)  # Adjust as needed
        
    elif "start typing" in command:
        # Notify the user that typing is initializing
        engine.say("Initializing typing")
        engine.runAndWait()

        while True:
            audio = recognizer.listen(source)
            try:      
                text = recognizer.recognize_google(audio).lower()

                if "stop writing" in text:
                    engine.say("Stopping writing")
                    engine.runAndWait()
                    break

                # Type the recognized text using pyautogui only if it's not "stop writing"
                pyautogui.typewrite(text)

            except sr.UnknownValueError:
                pass
        # Check if the user says "stop writing"
            
        # Simulate typing with a pause for user input
   
    elif "stop" in command:
        # Notify the user and exit the loop
        engine.say("Stopping voice recognition")
        engine.runAndWait()
        exit()


    # Paragraph Formatting Commands
    elif "align left" in command:
        pyautogui.hotkey("ctrl", "l")  # Left-align text
    elif "align center" in command:
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

    response = "Command complete: " + command
    engine.say(response)
    engine.runAndWait()

# # Main loop to listen for voice commands
# with sr.Microphone() as source:
#     print("Listening for voice commands...")
#     while True:
#         audio = recognizer.listen(source)
#         try:
#             command = recognizer.recognize_google(audio).lower()
#             print("You said:", command)
#             execute_voice_command(command)
#         except sr.UnknownValueError:
#             pass
#         except sr.RequestError:
#             print("Could not request results; check your network connection")
import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    while True:
        print("listening....")
        r.pause_threshold = 1
        audio = r.listen(source,0,5) #here we can set time for the assistant to hear our input. like here it is 5sec.
        try:
                print("recognizing....")
                query = r.recognize_google(audio, language='en-in').lower()
                execute_voice_command(query)
                print(f"you said: {query}\n")
                # speak(query)
        except Exception as e:
            print("please say again...")


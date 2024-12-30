import os
import speech_recognition as sr
import webbrowser
import datetime
import google.generativeai as genai
chat = ''
def chatjarvis(query):
    global chat
    print(chat)
    chat = f"Sai: {query}\n JARVIS: "
    genai.configure(api_key="AIzaSyCwjx6aJ9z1SZ3hj72mZl6PDVAXSfd2V3E")
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(chat)
    chat += response.text
    return response.text
def welcome(msg):
    os.system(f"say {msg}")

def gen_ai(query):
    genai.configure(api_key="AIzaSyCwjx6aJ9z1SZ3hj72mZl6PDVAXSfd2V3E")
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(query)
    
    if not os.path.exists("JARVIS"):
        os.mkdir("JARVIS")
    with open(f"JARVIS/{''.join(query.split('AI')).strip()}","w") as filer:
        filer.write(response.text)

def input_stream():
    srrec = sr.Recognizer()
    with sr.Microphone() as source:
        srrec.pause_threshold = 1
        voice = srrec.listen(source)
        try:
            query = srrec.recognize_google(voice, language="en-in")  
            return query
        except Exception as e:  
            #welcome("An Error has occured Sir sorry for inconvenience")
            print(f"Error: {e}")  # Log the error for debugging
            return ("An Error has occurred, Sir. Sorry for the inconvenience.")

if __name__ == '__main__':
    welcome("Hi Sir I am Jarvis")
    while True:
        print("Listening Sir ..")
        query = input_stream ()
        #welcome(query)
#todo:sites aur add karna bahut functionality keliye
        sites = {
        "you tube": "https://www.youtube.com",
        "google": "https://www.google.com",
        "wikipedia": "https://www.wikipedia.com",
        "whatsapp": "https://www.whatsapp.com",
        "facebook": "https://www.facebook.com",
        "fb": "https://www.facebook.com"}
        #print(query)
        for site_name in sites:
            if f"Open {site_name}".lower() in query.lower():
                    welcome(f"Opening {site_name} sir")
                    webbrowser.open(sites[site_name])

#todo: try time based on loaction of user input
            elif "What is Time".lower() in query.lower():
                welcome(f"Sir the time is {datetime.datetime.now().strftime('%H:%M:%S')}")
                #print(f"Date: {datetime.datetime.now().strftime('%d-%m-%Y')}")
                #print(f"Time: {datetime.datetime.now().strftime('%H:%M:%S')}")
            # if f"open ScreenShots".lower() in query.lower():
            #     path = r"Home/Pictures/Screenshots"
            #     os.access(path)
            #     os.system(f"opening  {path}")
            
#todo: add a specific song like pspk's spcl
            elif "use ai".lower() in query.lower():
                gen_ai(query)
                welcome(f"Work completed sir please check results sir")
            else:
                chatjarvis(query)
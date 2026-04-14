import nltk
import random
import string
import tkinter as tk
from tkinter import scrolledtext
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize



stemmer = PorterStemmer()

# Data
data = {
    "greeting": ["hello", "hi", "hey"],
    "admission": ["admission process", "how to apply"],
    "fees": ["fee structure", "college fee"],
    "courses": ["courses offered", "available courses", "what courses", "streams available"],
    "timings": ["college timing", "when does college start", "what are timings", "college hours"],
    "hostel": ["hostel facility", "is hostel available"],
    "placement": ["placement", "job opportunities"],
    "library": ["library timing", "is library open", "library hours"],
    "canteen": ["canteen food", "is canteen available", "canteen timing"],
    "faculty": ["teachers", "faculty details", "about professors"],
    "location": ["college location", "where is college", "address"],
    "transport": ["bus facility", "transport available", "college bus"],
    "scholarship": ["scholarship", "financial aid", "fee concession"],
    "exam": ["exam schedule", "when are exams", "exam dates"],
    "holiday": ["holidays", "vacation", "holiday list"],
    "wifi": ["wifi facility", "internet access", "is wifi available"],
    "internship": ["internship", "training program", "industrial training"],
    "events": ["college events", "fest", "cultural programs"],
    "sports": ["sports facility", "games", "playground"],
    "contact": ["contact number", "phone number", "email", "contact information" ],
    "department": ["department details", "departments in college", "available departments", "streams offered"],
    "bye": ["bye", "goodbye"]
}

responses = {
    "greeting": ["Hello! Welcome to our college chatbot."],
    "admission": ["You can apply online through the college website."],
    "fees": ["The fee is ₹1,50,000 per year for B.Tech course. Please check for the other courses from the college website."],
    "courses": ["The college offers programs in Civil, Mechanical, Computer Science, Electronics, and Management. Please specify if you want details about a particular course."],
    "timings": ["College runs from 8 AM to 3 PM."],
    "hostel": ["Yes, hostel facilities are available."],
    "placement": ["We provide good placement opportunities."],
    "library": ["Library is open from 9 AM to 5 PM."],
    "canteen": ["Canteen is available with hygienic food from 9 AM to 4 PM."],
    "faculty": ["We have experienced and qualified faculty members."],
    "location": ["The college is located in Kolkata, West Bengal."],
    "transport": ["Yes, college bus facilities are available for students."],
    "scholarship": ["Scholarships are available based on merit and category."],
    "exam": ["Exams are conducted at the end of each semester."],
    "holiday": ["You can check the academic calendar for holidays."],
    "wifi": ["Yes, WiFi is available across the campus."],
    "internship": ["Internship opportunities are provided in final years."],
    "events": ["We organize cultural fests, tech fests, and seminars."],
    "sports": ["Sports facilities include cricket, football, and indoor games."],
    "contact": ["You can contact us at info@college.com or call 1234567890."],
    "department": ["Our college offers departments like Computer Science, AI & Data Science, Electronics, Mechanical, Civil, and Management."],
    "bye": ["Goodbye!"]
}

def preprocess(text):
    words = word_tokenize(text.lower())
    words = [stemmer.stem(w) for w in words if w not in string.punctuation]
    return words

def chatbot_response(user_input):
    user_words = preprocess(user_input)

    for intent in data:
        for pattern in data[intent]:
            pattern_words = preprocess(pattern)

            if len(set(pattern_words).intersection(user_words)) >= len(pattern_words):
                return random.choice(responses[intent])

    return "Sorry, I didn't understand. Please ask about admission, fees, courses, hostel, etc."

def type_text(text):
    chat.insert(tk.END, "Bot: ", "bot")
    chat.update()

    for char in text:
        chat.insert(tk.END, char, "bot")
        chat.update()
        chat.after(10)  # speed (increase for slower typing)

    chat.insert(tk.END, "\n")

def send():
    user_input = entry.get()
    if user_input.strip() == "":
        return

    chat.insert(tk.END, "You: " + user_input + "\n", "user")

    response = chatbot_response(user_input)

    chat.insert(tk.END, "Bot is typing...\n", "bot")
    chat.update()

    window.after(500, lambda: type_text(response))

    entry.delete(0, tk.END)
    chat.yview(tk.END)

# GUI Window
window = tk.Tk()
window.title("🎓 College FAQ Chatbot")
window.geometry("500x550")
window.configure(bg="#f0f4f7")

# Chat Area
chat = scrolledtext.ScrolledText(window, wrap=tk.WORD, font=("Arial", 12))
chat.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Styling tags
chat.tag_config("user", foreground="blue")
chat.tag_config("bot", foreground="green")

# Welcome message
chat.insert(tk.END, "Bot: Welcome to the College FAQ Chatbot! How can I assist you today?\n", "bot")
# Input Frame
frame = tk.Frame(window, bg="#f0f4f7")
frame.pack(pady=5)

entry = tk.Entry(frame, font=("Arial", 14), width=25)
entry.pack(side=tk.LEFT, padx=5)

send_button = tk.Button(
    frame,
    text="Send",
    font=("Arial", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    padx=10,
    command=send
)
send_button.pack(side=tk.LEFT)

window.mainloop()
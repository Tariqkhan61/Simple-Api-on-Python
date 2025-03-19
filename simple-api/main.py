# Import the class of Fast Api
from fastapi import FastAPI
# Now import random module
import random

app = FastAPI()
# we build two simple get endpoints

#The term "side hustles"is general concept referring to secondary jobs or projects people 
# do for extra income or personal fulfillment. However.
side_hustles = [
    "Freelancing - start offering your skills online !",
    "Dropshipping - Sell without handling inventory !",
    "Sell Digital Products: Design and sell eBooks, templates, or digital art on platforms like Etsy.",
    "Graphic Design Services: Help small businesses with logos, branding, or promotional materials.",
    "Social Media Management: Assist businesses in building their online presence and engaging with their audience.",
    "Affiliate Marketing: Promote products or services and earn a commission for every sale made through your unique link.",
    "Fitness Coaching: If you're into fitness, guide others in their health journey through personal training or creating workout plans.",
    "Photography Business: Offer portrait, event, or product photography for individuals and companies.",
    "Handmade Crafts or Art: Turn your creativity into profit by selling items like paintings, jewelry, or custom apparel.",
    "Online Tutoring: Teach students in subjects you excel at or mentor professionals in a field you’re experienced in.",
]

money_quotes = [
    "Money is a terrible master but an excellent servant. - P.T. Barnum",
    "It’s not how much money you make, but how much money you keep. - Robert Kiyosaki",
    "Don’t tell me what you value, show me your budget, and I’ll tell you what you value. - Joe Biden",
    "Formal education will make you a living; self-education will make you a fortune. - Jim Rohn",
    "The stock market is filled with individuals who know the price of everything but the value of nothing. - Philip Fisher",
    "Rich people have small TVs and big libraries, and poor people have small libraries and big TVs. - Zig Ziglar",
    "The goal isn't more money. The goal is living life on your terms. - Chris Brogan",
    "Save money and money will save you. - Unknown",
    "Never spend your money before you have earned it. - Thomas Jefferson",
    "Too many people spend money they haven’t earned, to buy things they don’t want, to impress people they don’t like. - Will Rogers"
]

# now make a Decorator which is Route handler
@app.get("/side_hustles")
def get_side_hustles():
     # Doc string
     """returns a random side hustle idea"""
     return {"side_hustle": random.choice(side_hustles)}

@app.get("/money_quotes")
def get_money_quotes():
     """Returns a random money quote"""
     return {"money_quotes": random.choice(money_quotes)}

# fastapi dev main.py
# Direct Testing of APIS
# copy the command "http://127.0.0.1:8000 " and paste in a new terminal.
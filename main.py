from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

captions = {
    "catchy": [
        "🔥 Don't miss our amazing {topic} offers!",
        "✨ Big savings are here with our {topic}!",
        "🛍️ Shop now and enjoy the best {topic} deals!"
    ],

    "funny": [
        "😂 Your wallet may cry, but the {topic} deals are worth it!",
        "🔥 {topic} deals hotter than summer!",
        "🛒 Warning: You may buy everything in this {topic} sale!"
    ],

    "professional": [
        "Explore premium {topic} offers available now.",
        "Experience the best quality with our {topic} collection.",
        "Upgrade your shopping experience with our {topic} deals."
    ],

    "emotional": [
        "❤️ Celebrate happiness with our special {topic} offers.",
        "✨ Make beautiful memories with our {topic} collection.",
        "🎉 Share joy and savings with our {topic} event."
    ]
}

hashtags = [
    "#Sale",
    "#Shopping",
    "#Offers",
    "#Trending",
    "#Discount"
]

image_ideas = [
    "Colorful shopping bags with discount banners",
    "Festive decorations with products on display",
    "Modern promotional poster with bright offers",
    "Customers enjoying shopping with sale boards"
]

variants = [
    "Shop today before the offers end!",
    "Big discounts waiting for you!",
    "Grab your favorites now!"
]

@app.get("/")
def home():
    return {"message": "API Running Successfully"}

@app.get("/generate")
def generate(prompt: str, tone: str = "catchy"):

    caption = random.choice(
        captions.get(tone, captions["catchy"])
    ).format(topic=prompt)

    output = f"""
Caption:
{caption}

Hashtags:
{' '.join(hashtags)}

Image Idea:
{random.choice(image_ideas)}

Variants:
1. {random.choice(variants)}
2. {random.choice(variants)}
"""

    return {
        "output": output
    }
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI()

# Allow frontend access (CORS settings)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dummy sample data
sample_keywords = {
    "YouTube": {
        "Animal": ["funny cat", "wildlife facts", "cute puppy", "animal rescue", "zoo tour"],
        "Fashion": ["summer trends", "outfit ideas", "vintage fashion", "sneaker reviews"],
    },
    "Pinterest": {
        "Animal": ["cat memes", "bird nest decor", "puppy ideas"],
        "Fashion": ["boho style", "wedding outfits", "nail trends"],
    },
}

@app.get("/")
def read_root():
    return {"message": "Trend Finder API is running"}

@app.get("/keywords")
def get_keywords(platform: str = "YouTube", niche: str = "Animal"):
    data = sample_keywords.get(platform, {}).get(niche, [])
    if not data:
        return {"error": "No keywords found"}
    return {"keywords": random.sample(data, min(10, len(data)))}

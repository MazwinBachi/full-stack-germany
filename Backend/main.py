from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import requests
from datetime import datetime

app = FastAPI()

# CORS configuration
origins = [
    "http://localhost:5173",  # Vite dev server
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/top-10-stories")
def get_top_stories():
    try:
        top_stories_url = "https://hacker-news.firebaseio.com/v0/newstories.json"
        response = requests.get(top_stories_url)
        response.raise_for_status()
        story_ids = response.json()[:10]
        stories = []

        for story_id in story_ids:
            story_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
            story_response = requests.get(story_url)
            story_data = story_response.json()

            story = {
                "title": story_data.get("title"),
                "author": story_data.get("by"),
                "url": story_data.get("url"),
                "score": story_data.get("score"),
                "time": datetime.utcfromtimestamp(story_data.get("time")).strftime('%Y-%m-%d %H:%M:%S')
            }
            stories.append(story)

        return stories
    except requests.RequestException as e:
        raise HTTPException(status_code=503, detail="HackerNews API is unavailable")

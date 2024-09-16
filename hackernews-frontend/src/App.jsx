import React, { useState, useEffect } from 'react';
import './App.css'; // Make sure this import is present

const App = () => {
  const [stories, setStories] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch('http://localhost:8000/top-10-stories')
      .then(response => response.json())
      .then(data => {
        setStories(data);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching stories:', error);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return (
      <div className="loading-container">
        <p>Loading...</p>
      </div>
    );
  }

  return (
    <div className="container">
      <h1>Top 10 New HackerNews Stories</h1>
      <ul className="story-list">
        {stories.map((story, index) => (
          <li key={index} className="story-item">
            <a href={story.url} target="_blank" rel="noopener noreferrer">
              {story.title}
            </a>
            <div className="story-details">
              <p>Author: {story.author}</p>
              <p>Score: {story.score}</p>
            </div>
            <p className="story-time">Posted on: {story.time}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default App;

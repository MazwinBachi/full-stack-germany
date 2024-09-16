# HackerNews Top 10 Stories App

## Overview

This application retrieves and displays the top 10 new stories from the HackerNews API. It consists of a FastAPI backend that fetches the data and a React frontend that displays the stories.

## Getting Started

### Prerequisites

- Python 3.8+
- Node.js 14+

### Backend Setup

1. **Navigate to the backend directory:**
    ```bash
    cd path/to/backend
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the FastAPI server:**
    ```bash
    uvicorn main:app --reload --port 8000
    ```

### Frontend Setup

1. **Navigate to the frontend directory:**
    ```bash
    cd path/to/frontend
    ```

2. **Install dependencies:**
    ```bash
    npm install
    ```

3. **Run the React development server:**
    ```bash
    npm run dev
    ```

## Usage

1. **Start the backend server** by following the steps in the Backend Setup section.
2. **Start the frontend server** by following the steps in the Frontend Setup section.
3. **Open your browser** and go to `http://localhost:5173` to view the application.

## Error Handling

- If the backend server is not running, the frontend will display an error message.
- If there is an issue fetching data from the HackerNews API, an appropriate error message will be shown.


## Acknowledgments

- FastAPI for the backend framework
- React for the frontend framework
- HackerNews API for providing the news data

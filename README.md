# Mood Visualizer

A simple Streamlit app that reads diary-style text files, runs sentiment analysis with NLTK's VADER model, and plots positivity and negativity over time.

## Features

- Reads `.txt` diary entries from a local `diary/` folder
- Extracts positivity and negativity scores with NLTK
- Displays trend lines with Plotly inside a Streamlit app
- Uses filenames as dates for time-based visualization

## Project structure

```text
moodvisualizer/
├── backend.py
├── main.py
├── requirements.txt
├── .gitignore
└── diary/
    ├── 2023-10-21.txt
    └── ...
```

## Setup

1. Create and activate a virtual environment
2. Install the dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
streamlit run main.py
```

## Data format

Put diary entries inside the `diary/` folder as `.txt` files.
A good naming pattern is:

```text
YYYY-MM-DD.txt
```

Example:

```text
diary/2026-04-05.txt
```

## Tech stack

- Python
- Streamlit
- Plotly
- NLTK (VADER sentiment analysis)

## Notes

- If the VADER lexicon is missing, NLTK downloads it automatically on first run.
- The sample diary files are just example inputs for visualization.
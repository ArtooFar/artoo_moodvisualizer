# Mood Visualizer

Mood Visualizer is a Streamlit application that analyzes diary entries using natural language processing and visualizes sentiment trends over time.

The project was developed as a practical exploration of sentiment analysis in personal text data, combining VADER-based polarity scoring with interactive Plotly visualizations. Its main purpose is to study how NLP techniques can be applied to temporal text analysis in a simple and accessible interface.

This project demonstrates practical experience with:
- NLP preprocessing workflows
- sentiment analysis
- text-based feature extraction
- temporal data visualization
- interactive application development

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

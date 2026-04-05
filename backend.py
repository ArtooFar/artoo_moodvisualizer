from pathlib import Path
from nltk.sentiment import SentimentIntensityAnalyzer


def get_files_and_content(root_dir="diary"):
    """Return a sorted list of (date, text_content) tuples from diary .txt files."""
    root_path = Path(root_dir)
    files_and_content = []

    for file_path in sorted(root_path.glob("*.txt")):
        with file_path.open("r", encoding="utf-8") as file:
            files_and_content.append((file_path.stem, file.read()))

    return files_and_content



def get_positivity_and_date_list(sorted_files_and_content):
    analyzer = SentimentIntensityAnalyzer()
    positivity_list = []
    date_list = []

    for date, content in sorted_files_and_content:
        date_list.append(date)
        positivity_list.append(analyzer.polarity_scores(content)["pos"])

    return date_list, positivity_list



def get_negativity_and_date_list(sorted_files_and_content):
    analyzer = SentimentIntensityAnalyzer()
    negativity_list = []
    date_list = []

    for date, content in sorted_files_and_content:
        date_list.append(date)
        negativity_list.append(analyzer.polarity_scores(content)["neg"])

    return date_list, negativity_list

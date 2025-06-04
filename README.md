# FounderFootprint

FounderFootprint is an AI-powered Streamlit application that builds a concise, structured digital footprint of a startup founder or CEO using publicly available web content. The app scrapes relevant news articles, runs sentiment analysis using OpenAI's GPT API, and presents a short bio-style profile with headlines such as background, achievements, controversies, notable quotes, and public sentiment.

---

## Use Case

Whether you're an investor, journalist, or just curious about a tech leader, FounderFootprint helps you quickly understand their current public image, recent news, and major milestones—powered by automation and GPT analysis.

---

## Features

- Scrapes recent news articles from the web using search queries
- Extracts clean article text using `newspaper3k`
- Uses OpenAI GPT to generate:
  - Background
  - Recent News
  - Public Sentiment
  - Notable Quotes
  - Achievements
  - Controversies
- Simple Streamlit UI for entering founder name and viewing summaries

---

## Tech Stack

- Python 3.10+
- `newspaper3k` for article scraping
- OpenAI GPT for summarization and sentiment
- Streamlit for interactive web UI
- BeautifulSoup & requests for fallback scraping

---

## Project Structure

```
founderfootprint/
├── app.py               # Streamlit frontend
├── scrape_utils.py      # Web scraping utilities
├── summarise.py         # GPT-based summarization logic
├── requirements.txt     # Python dependencies
├── .env                 # API key (not pushed to Git)
├── README.md            # You're here
```

---

## Setup Instructions

1. Clone the repo

```bash
git clone https://github.com/amnaabbasi03/founderfootprint.git
cd founderfootprint
```

2. Create a virtual environment and install dependencies

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Add your OpenAI API key

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

4. Run the app

```bash
streamlit run app.py
```

---

## Example Output

**Search:** Elon Musk

- Background: CEO of SpaceX and Tesla, known for innovative leadership in EVs and space.
- Recent News: New satellite launch from SpaceX and updates on Tesla’s AI.
- Public Sentiment: Mixed — admired for innovation, criticized for controversial tweets.
- Notable Quotes: “When something is important enough, you do it even if the odds are not in your favor.”
- Achievements: First commercial space company to dock with the ISS.
- Controversies: SEC investigations, public Twitter disputes.

---

## To-Do Next

- Add caching for repeated searches
- Support for multiple data sources (e.g., social media)
- Export as PDF/Markdown
- Dockerize for deployment

---

## Author

Made with GPT-4 and Streamlit by [Amna Abbasi](https://github.com/amnaabbasi03)
import torch  

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, 
                             QLabel, QLineEdit, QPushButton, QTextEdit)
from src.scraper import scrape_article
from src.predictor import ArticlePredictor

class CredibilityApp(QWidget):
    def __init__(self):
        super().__init__()
        self.predictor = ArticlePredictor()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Multi-Model Article Credibility & Clickbait Analyzer')
        self.setGeometry(100, 100, 600, 500)

        layout = QVBoxLayout()

        self.label = QLabel('Enter Article URL or Paste Raw Text:', self)
        layout.addWidget(self.label)

        self.url_input = QLineEdit(self)
        self.url_input.setPlaceholderText('https://example.com/news-article')
        layout.addWidget(self.url_input)

        self.analyze_btn = QPushButton('Analyze Article', self)
        self.analyze_btn.clicked.connect(self.run_analysis)
        layout.addWidget(self.analyze_btn)

        self.result_display = QTextEdit(self)
        self.result_display.setReadOnly(True)
        layout.addWidget(self.result_display)

        self.setLayout(layout)

    def run_analysis(self):
        user_input = self.url_input.text().strip()
        if not user_input:
            self.result_display.setText("Please enter a URL or paste text to analyze.")
            return

        if user_input.startswith("http://") or user_input.startswith("https://"):
            self.result_display.setText("Fetching article contents...")
            text_to_analyze, error = scrape_article(user_input)
            if error:
                self.result_display.setText(f"Error scraping URL: {error}")
                return
        else:
            text_to_analyze = user_input

        results = self.predictor.predict(text_to_analyze)

        display_text = "--- ANALYSIS RESULTS ---\n\n"
        for model_name, data in results.items():
            fake_percentage = data['prob_fake'] * 100
            display_text += f"• {model_name}:\n"
            display_text += f"  Prediction: {data['label']}\n"
            display_text += f"  Clickbait / Fake Probability: {fake_percentage:.2f}%\n\n"

        self.result_display.setText(display_text)
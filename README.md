# PDF to Speech Reader

A simple Python script that reads aloud the text from any PDF file using offline text-to-speech.

No internet required — everything runs locally on your machine.

## What it does

- Opens a PDF file (using `os` for path handling)
- Reads the PDF content page by page with `PyPDF2`
- Extracts clean text from each page
- Uses `pyttsx3` to convert the extracted text to natural-sounding speech
- Speaks the content aloud through your computer's speakers

Great for:
- Listening to articles, books, or study notes hands-free
- Accessibility (screen reader alternative)
- Quick audio previews of documents

## Features

- Fully offline TTS (no cloud API needed)
- Reads entire PDF or specific pages (easy to customize)
- Adjustable speech rate, volume, and voice (via pyttsx3)
- Simple command-line usage

## Requirements

```bash
pip install pyttsx3 PyPDF2

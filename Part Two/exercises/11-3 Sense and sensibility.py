import os
import re

import PyPDF2

path = os.path.dirname(os.path.abspath(__file__))
pdf_filename = os.path.join(path, "Sense-and-Sensibility-by-Jane-Austen.pdf")

frequency_table = {}

with open(pdf_filename, "rb") as pdf_file:
  pdf_reader = PyPDF2.PdfReader(pdf_file)

  for page in pdf_reader.pages:
    page_text = page.extract_text() or ""

    for line in page_text.split("\n"):
      words = line.split()

      for word in words:
        cleaned_word = word.strip().lower()

        frequency_table[cleaned_word] = frequency_table.get(cleaned_word, 0) + 1

print(frequency_table)

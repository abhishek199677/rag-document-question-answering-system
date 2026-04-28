import pdfplumber
import logging

class PDFProcessor:
    @staticmethod
    def extract_text(pdf_path):
        """Extracts text from a PDF file."""
        full_text = ""
        try:
            with pdfplumber.open(pdf_path) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        full_text += page_text + "\n"
            return full_text
        except Exception as e:
            logging.error(f"Failed to extract text from {pdf_path}: {e}")
            return ""

    @staticmethod
    def split_text(text, chunk_size=1000, overlap=200):
        """Splits text into manageable chunks."""
        chunks = []
        if not text:
            return chunks
            
        start = 0
        text_len = len(text)
        while start < text_len:
            end = min(start + chunk_size, text_len)
            chunks.append(text[start:end])
            if end == text_len:
                break
            start = end - overlap
        return chunks

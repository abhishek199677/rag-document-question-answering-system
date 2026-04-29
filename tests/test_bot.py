import pytest
from src.bot import RAGBot

def test_bot_initialization():
    bot = RAGBot()
    assert bot.memory == []
    assert bot.vector_store is None

def test_processor_exists():
    bot = RAGBot()
    assert bot.processor is not None

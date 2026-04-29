import pytest
from unittest.mock import MagicMock, patch
from src.bot import RAGBot

@pytest.fixture
def mock_bot():
    with patch('src.api_client.OpenAI'):
        with patch.dict('os.environ', {'OPENAI_API_KEY': 'test-key'}):
            return RAGBot()

def test_bot_initialization(mock_bot):
    assert mock_bot.memory == []
    assert mock_bot.vector_store is None

def test_processor_exists(mock_bot):
    assert mock_bot.processor is not None

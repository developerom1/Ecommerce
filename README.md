# Ecommerce Voicebot Agent

A Python-based humanlike voicebot agent for ecommerce, using speech recognition, conversational AI, and sample product logic.

## Features
- Voice-based interaction (speech-to-text, text-to-speech)
- Humanlike conversation powered by GPT
- Product search functionality
- Modular structure (easy to expand)
- Order placement and tracking capabilities

## Project Structure
```
ecommerce_voicebot/
  ├── README.md
  ├── requirements.txt
  ├── main.py
  └── utils/
        ├── speech.py
        ├── nlp.py
        └── ecommerce.py
```

## Quick Start
1. Install requirements: `pip install -r requirements.txt`
2. Set your OpenAI API key in `main.py`
3. Run: `python main.py`
4. Speak your queries into the microphone!

## Modules
- `utils/speech.py`: Voice input/output helpers
- `utils/nlp.py`: Conversational logic
- `utils/ecommerce.py`: Sample product search API

## Requirements
- Python 3.8+
- OpenAI API key
- Microphone for voice input

## Example Conversations
- "Find wireless headphones"
- "Search for smartwatch"
- "What products do you have?"
- "Show me bluetooth mouse"

## Future Enhancements
- Payment gateway integration
- Order tracking system
- User authentication
- Shopping cart management
- Multi-language support
- Sentiment analysis

## License
MIT License

## Author
developerom1

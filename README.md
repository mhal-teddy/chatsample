# chatsample
This project is the chat sample using Streamlit.

## Install
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Set your OpenAI API key
```python
# .streamlit/secrets.toml
OPENAI_API_KEY = "YOUR_API_KEY"
```

## Run streamlit
```bash
streamlit run app.py
```
Then, open http://localhost:8501/
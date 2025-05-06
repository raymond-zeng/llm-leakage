from deep_translator import GoogleTranslator
import pandas as pd
import huggingface_hub as hf
from tqdm import tqdm

# Load your DataFrame
splits = {'train': 'main/train-00000-of-00001.parquet', 'test': 'main/test-00000-of-00001.parquet'}
df = pd.read_parquet("hf://datasets/openai/gsm8k/" + splits["test"])

# Translate the 'question' column to French
def safe_translate(text):
    try:
        return GoogleTranslator(source='en', target='fr').translate(text)
    except Exception as e:
        print(f"Error translating: {text}. Error: {e}")
        return None  # or return text if you want to keep the original

tqdm.pandas(desc="Translating questions to French")
df['french_question'] = df['question'].progress_apply(safe_translate)

# Save the updated DataFrame
df.to_csv('gsm8k-french-test.csv', index=False)

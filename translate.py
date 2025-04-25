from deep_translator import GoogleTranslator
import pandas as pd

# Load your DataFrame
df = pd.read_csv('gsm8k-french2-untranslated-test.csv')

# Translate the 'question' column to French
def safe_translate(text):
    try:
        return GoogleTranslator(source='en', target='fr').translate(text)
    except Exception as e:
        print(f"Error translating: {text}. Error: {e}")
        return None  # or return text if you want to keep the original

df['french_question'] = df['question'].apply(safe_translate)

# Save the updated DataFrame
df.to_csv('gsm8k-french2-translated-test.csv', index=False)

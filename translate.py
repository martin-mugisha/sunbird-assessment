import requests

url = 'https://sunbird-ai-api-5bq6okiwgq-ew.a.run.app'
headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJJbnRlcm5zaGlwcyIsImV4cCI6NDg0MTQ4NzEyMn0.-j3rdudJ9pXEm3-456LLiDPun5SwIm5sw-RoNvgDwfk",
    "Content-Type": "application/json"
}

source_language = input("Enter Source Language (English, Luganda, Runyankole, Ateso, Lugbara, or Acholi): ")

# Check if the source language is English
if source_language.lower() == "english":
    target_language = input("Enter the target language (Luganda, Runyankole, Ateso, Lugbara, or Acholi): ")
else:
    target_language = "English"

text = input("Enter the text to translate (in the source language chosen): ")

payload = {
    "source_language": source_language,
    "target_language": target_language,
    "text": text
}

response = requests.post(f"{url}/tasks/translate", headers=headers, json=payload)

if response.status_code == 200:
    translated_text = response.json().get("text")
    print("Translated text:", translated_text)
else:
    print("Error:", response.status_code, response.text)

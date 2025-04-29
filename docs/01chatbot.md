
# 🤖 Exemple bàsic d'ús de BlenderBot amb Hugging Face Transformers

Aquest exemple mostra com utilitzar el model [`facebook/blenderbot-400M-distill`](https://huggingface.co/facebook/blenderbot-400M-distill) per generar respostes a preguntes o missatges de l'usuari, utilitzant el `pipeline` de Hugging Face.

## 📦 Requisits

Assegura't de tenir instal·lades les dependències següents:

```bash
pip install transformers torch
```

## 📜 Codi complet

```python
from transformers import pipeline

# Inicialitzem el pipeline amb BlenderBot
# https://huggingface.co/facebook/blenderbot-400M-distill
chatbot = pipeline(task="text2text-generation", model="facebook/blenderbot-400M-distill")

# Missatge de l'usuari
user_message = """
What are some fun activities I can do in the winter?
"""

# Enviem el missatge al model i generem resposta
output = chatbot(user_message)

# Mostrem la resposta generada
print("Bot:", output[0]["generated_text"])
```

## 🔍 Explicació del funcionament

### 1. `chatbot = pipeline(...)`

Aquesta línia crea un objecte de tipus `Text2TextGenerationPipeline`, especialitzat en tasques de generació de text a partir de text (`text2text-generation`).

El model que s'utilitza és `facebook/blenderbot-400M-distill`, un model preentrenat per mantenir converses.

### 2. Què és `chatbot`

`chatbot` és un objecte que es pot cridar com una funció perquè implementa el mètode especial `__call__()`.

Gràcies a això, pots fer:

```python
output = chatbot(user_message)
```

### 3. Què fa `chatbot(user_message)`?

- Tokenitza el text d'entrada.
- El passa pel model preentrenat.
- Des-tokenitza la sortida i la retorna en una llista de diccionaris, on cada diccionari conté la clau `"generated_text"` amb la resposta generada.

**Exemple de sortida:**

```python
[{'generated_text': 'You can go skiing, ice skating, or drink hot chocolate by the fire.'}]
```

### 4. `print("Bot:", output[0]["generated_text"])`

Accedeix a la primera (i única) resposta generada i imprimeix el contingut textual.

## ✅ Resultat esperat

```
Bot: You can go skiing, ice skating, or drink hot chocolate by the fire.
```

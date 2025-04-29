from transformers import pipeline

# Inicialitzem el pipeline amb BlenderBot
# https://huggingface.co/facebook/blenderbot-400M-distill
chatbot = pipeline(task="text2text-generation", model="facebook/blenderbot-400M-distill")

# Missatge de l'usuari
missatge = input("Tu: ")

# Enviem el missatge al model i generem resposta
output = chatbot(missatge)

# Mostrem la resposta generada
print("Bot:", output[0]["generated_text"])


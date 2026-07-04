from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Asume el rol de experto en Inteligencia Artificial, explica en pocas palabras como trabaja la IA"
)

print(interaction.output_text)
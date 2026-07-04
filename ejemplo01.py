from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Asume el rol de experto en desarrollo de software y responde a la siguiente pregunta: ¿Cuáles son las mejores prácticas para escribir código limpio y mantenible en Python?"
)
print(interaction.output_text)
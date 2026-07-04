from google import genai

client = genai.Client()

# Modificación 3
while True:
    # Modificación 1
    pregunta = ""
    print("Bienvenido a la consulta de IA. Por favor, ingrese su pregunta:")
    pregunta = input()

    interaction = client.interactions.create(
        model="gemini-3.5-flash",
        input=pregunta # Modificación 2  
    )

    print(interaction.output_text)
    # Modificación 4
    respuesta = input("¿Desea hacer otra pregunta? (s/n): ?")
    if respuesta.lower() != "s":
        print("Gracias por usar la consulta de IA. ¡Hasta luego!")
        break
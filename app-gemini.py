import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
clave_api = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=clave_api)

def ejecutar_consulta():
    print("Realizando consulata con el motor de Gemini... 🕵🏻")
    try:
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents="¿Quién es el presidente de Francia?"
        )
        print("\n--- Respuesta Recibida ---")
        print(response.text)
        print("--------------------------")
    except Exception as e:
        print(f"❌ Ocurrió un error en la conexión: {e}")
 
if __name__ == "__main__":
    ejecutar_consulta()

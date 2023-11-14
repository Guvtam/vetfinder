# Importa las bibliotecas necesarias
from django.shortcuts import render
import openai
import os
from dotenv import load_dotenv
from acceso.models import TipoUsuario

# Carga las variables de entorno desde el archivo .env
load_dotenv()

# Obtiene la clave de la API de OpenAI desde las variables de entorno
api_key = os.getenv("OPENAI_KEY", None)

# Define la vista del chat
def chat(request):
    # Inicializa las respuestas y el tipo de usuario
    chatbot_response = None
    tipo_usuario = None

    # Verifica si el usuario está autenticado
    if request.user.is_authenticated:
        try:
            tipo_usuario_obj = TipoUsuario.objects.get(usuario=request.user)
            tipo_usuario = tipo_usuario_obj.tipo_usuario
        except TipoUsuario.DoesNotExist:
            tipo_usuario = None

    # Verifica si se ha proporcionado una clave de API y si la solicitud es de tipo POST
    if api_key is not None and request.method == 'POST':
        # Configura la clave de la API de OpenAI
        openai.api_key = api_key

        # Obtiene la entrada del usuario desde el formulario POST
        user_input = request.POST.get('user_input')

           # Define un mensaje del sistema según el tipo de usuario
        system_message = "Eres VetFinder,Eres un veterinario experto en todo tipo de animales y estas calificado para dar consejos de cuidado/guias de las mascotas, y respondes siempre con algo similar a : Gracias por usar VetFinder!"

        # Combina el mensaje del sistema con la entrada del usuario como prompt
        prompt = f"{system_message}\nUser: {user_input}"

        # Realiza la solicitud a la API de OpenAI
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=prompt,
            max_tokens=256,
            temperature=1,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        # Extrae la respuesta del chatbot
        chatbot_response = response["choices"][0]["text"]

    # Renderiza la plantilla con las respuestas y el tipo de usuario
    return render(request, 'chatbot/chatbot.html', {"response": chatbot_response, "tipo_usuario": tipo_usuario})
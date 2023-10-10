from django.shortcuts import render
import openai, os 
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("OPENAI_KEY", None)

# Create your views here.
def chat(request):
    chatbot_response=None
    if api_key is not None and request.method == 'POST':
        openai.api_key=api_key
        user_input=request.POST.get('user_input')
        prompt=user_input
        
        response=openai.Completion.create(
            engine= 'text-davinci-003',
            prompt= prompt,
            max_tokens= 256,
            temperature=1,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
  
  

        print(response)
        chatbot_response=response["choices"][0]["text"]
    return render(request,'chatbot/chatbot.html',{"response": chatbot_response})
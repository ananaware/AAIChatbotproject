from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

@csrf_exempt
def chat_view(request):
    if request.method == 'POST':
        user_message = request.POST.get('message')
        # Dummy reply logic for now:
        bot_reply = f"You said: {user_message}"
        return JsonResponse({'response': bot_reply})
    return render(request, 'chatapp/chat.html')


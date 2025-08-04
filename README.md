Anushka Nanaware  

The goal of this assignment was to design and build a simple web-based chatbot interface using Django. The chatbot needed to take user input from a web page, process it in the backend, and return a response dynamically using JavaScript and Django’s POST handling. I aimed to get hands-on experience with Django project structure, routing logic, handling POST requests, and using CSRF tokens securely. By completing this task, I wanted to build a fully functional chatbot skeleton that could later be extended with real logic or integrated with AI frameworks.  

I began by setting up my Django project using PyCharm. Inside the PyCharm interface, I opened the terminal and created a Django project named chatbot_project by typing the command django-admin startproject chatbot_project. This generated the essential files such as settings.py, urls.py, wsgi.py, etc., under the chatbot_project folder. 

Next, I created a Django app within the project directory named chatapp by running the command python manage.py startapp chatapp. This command generated a new folder named chatapp containing files like views.py, urls.py, models.py, and templates/. 

Then, I registered the new app in the project by opening the settings.py file (located inside the inner chatbot_project directory, the one with asgi.py, settings.py, etc.) and adding 'chatapp', under the INSTALLED_APPS list.  

To ensure Django could locate my HTML templates, I configured the TEMPLATES setting in the same settings.py file. I added 'DIRS': [os.path.join(BASE_DIR / 'chatapp' / 'templates')] (note: I had to add import os at the top of the file because it was missing and caused a red error underline). This tells Django to look inside the chatapp/templates directory for template files like chat.html. 

 

Then I created the folder structure inside the chatapp app: templates/chatapp/, and inside it I added a file called chat.html. This file held the chatbot UI and JavaScript logic. The full HTML code looked like this: 

<!DOCTYPE html> 
<html> 
<head> 
    <title>Chatbot</title> 
    <script> 
        async function sendMessage() { 
            const message = document.getElementById("userInput").value; 
            const response = await fetch("", { 
                method: "POST", 
                headers: { 
                    "Content-Type": "application/x-www-form-urlencoded", 
                    "X-CSRFToken": getCookie('csrftoken') 
                }, 
                body: "message=" + encodeURIComponent(message) 
            }); 
            const data = await response.json(); 
            document.getElementById("chatbox").innerHTML += `<p><strong>You:</strong> ${message}</p>`; 
            document.getElementById("chatbox").innerHTML += `<p><strong>Bot:</strong> ${data.response}</p>`; 
            document.getElementById("userInput").value = ""; 
        } 
 
        function getCookie(name) { 
            const value = "; " + document.cookie; 
            const parts = value.split("; " + name + "="); 
            if (parts.length === 2) return parts.pop().split(";").shift(); 
        } 
    </script> 
</head> 
<body> 
    <h2>Chat with Bot</h2> 
    <div id="chatbox" style="border:1px solid #ccc; padding:10px; width:300px; height:200px; overflow:auto;"></div> 
    <br> 
    <input type="text" id="userInput" placeholder="Type a message"> 
    <button onclick="sendMessage()">Send</button> 
</body> 
</html> 

 
 

Next, I implemented the backend logic for the chatbot in chatapp/views.py. I added the following code to handle both GET and POST requests. For POST, it reads the user's message and returns a dummy response: 

from django.shortcuts import render 
from django.views.decorators.csrf import csrf_exempt 
from django.http import JsonResponse 
 
@csrf_exempt 
def chat_view(request): 
    if request.method == 'POST': 
        user_message = request.POST.get('message') 
        bot_reply = f"You said: {user_message}" 
        return JsonResponse({'response': bot_reply}) 
    return render(request, 'chatapp/chat.html') 

 

Then I created a urls.py file inside the chatapp folder with this content to define a route for the chatbot view: 

from django.urls import path 
from . import views 
 
urlpatterns = [ 
    path('', views.chat_view, name='chat'), 
] 

 

I also updated the main urls.py inside the chatbot_project folder to include the chatapp's URLs. I wrote the following: 

from django.contrib import admin 
from django.urls import path, include 
 
urlpatterns = [ 
    path('admin/', admin.site.urls), 
    path('', include('chatapp.urls')), 
] 

 

After completing the code, I ran the server using the command python manage.py runserver. The terminal showed the development server running at http://127.0.0.1:8000/, and when I opened that URL in a browser, the chatbot interface appeared as expected. I typed “hello” in the input box, clicked “Send”, and the chatbot responded with “You said: hello”, confirming that the front-end and back-end were connected successfully and the entire flow was working. 

 


 

 

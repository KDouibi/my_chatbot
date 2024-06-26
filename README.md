The purpose of this tutorial is to learn how to build a basic chatbot with Django. Then, in a second phase to improve it to include an LLM.
Easy start to test this code:
- clone the repo and run the application in the terminal: python manage.py runserver
- click into the adress generated and go to blog page, the chatbot app will appear and you can ask some first questions.

For better understanding an learning purposes, I recommend you to follow the below steps and do the exercice yourself.
INSTALLING REQUIREMENTS/

First you need to :
- install Python in your machine.
- in CMD: pip install Django
- create new folder for your project and then cd to this folder and then tap: Django-admin startproject my_project
- open the project in an IDE( pycharm or visual studio of your choice)
- manage.py is the main function, and urls functions contain all urls that you want to add to your chatbot.
- every project in Django can have several apps for different purposes.

To create Django first app in your project:
- in the terminal of your IDE tap: python manage.py startapp blog  (if python 3 is installed use python3)
- Models.py is very important and it allows you to create for eg. new users to the app etc.

To run your app in the browser: 
- in the terminal, python manage.py runserver, it will give you an url where your app is launched, you copy the url and in a browser paste it. or just click on the link you get.
- you will see the following view:
  ![image](https://github.com/KDouibi/my_chatbot/assets/38917244/6ecbe4eb-059d-4e1d-bbee-d7a94626e2e1)
 
To create a new url: 
- open blog app and find urls.py if not existing: create it (refer to blog/urls.py.
- don't forget to add the url that we create in our app blog to the main urls.py of our main project (refer to my_chatbot.py)
- now, return to urls.py in blog:
  - In views.py of blog,  we need to create the function (index ()) that will be executed once the above url is opened.
- save all and then open terminal, run the server and add /blog to the url ![image](https://github.com/KDouibi/my_chatbot/assets/38917244/8bd0d407-83c5-4687-a833-30abd320c2d3)
  - you will see the message we have added to index function
- PS: if we want to add an url to blog as well (eg. Specific in this example) , we need to specify the main url of that app in blog app and add it to the urls.py of the whole project and add the specific function to the urls (see example "specific" in blog/urls and in views the definition of that function "specific".
  
HTML
  Add URL that return html code:
  - we need to create a new folder named templates where we can add our file ( refer to templates/blog/index.html), you can for now test with the following basic code.
      <img width="417" alt="image" src="https://github.com/KDouibi/my_chatbot/assets/38917244/fb72c9e0-9c63-48c7-87ef-3c241f30130f">

  - don't forget to add the function to the view.py, that will help to run the html page that we have created above. Also, it is important to add the following lines in settings.py of the main project (not the app blog) (see image below)
      <img width="417" alt="image" src="https://github.com/KDouibi/my_chatbot/assets/38917244/a9033211-4c09-45e2-9a5c-98d05eecb11c">
      
      <img width="418" alt="image" src="https://github.com/KDouibi/my_chatbot/assets/38917244/87e92b3b-2f71-4d98-bd0d-cc320ec31c39">
CSS
  Add CSS to have better view of our page:
    - we add a folder under blog called static and inside another folder named blog for the app that we are creating.
      ![image](https://github.com/KDouibi/my_chatbot/assets/38917244/e0c4db40-3c3e-4d0b-a306-9c4da8ea6f9b)
    - then, create a file called "style.css" to link our "index.html" with "style.css", add the following piece of code in "index.html" in the head section (refer to style.css)
  Note that sometimes, you need to restard the server to apply the modifications you added to your html page.
    - 
CREATING THE INTERFACE FOR THE INTERACTIONS WITH THE CHATBOT:
-  check "index.html", read the comments in the code to get better understanding of each functionality.
-  css.style file need to be improved as well, check the basic version tested in this tutorial.
-   now, to get text from our user in our app we need to use JQuery [2] which is "a fast, small, and feature-rich JavaScript library. It makes things like HTML document traversal and manipulation, event handling, animation, and Ajax much simpler with an easy-to-use API that works across a multitude of browsers. With a combination of versatility and extensibility, jQuery has changed the way that millions of people write JavaScript".

- install JQuery to add to our application AJAX request: Go to “jquery.com” / “download” then go to “Using jQuery with a CDN”
- to use the jQuery CDN, just reference the file in the script tag directly from the jQuery CDN domain. You can get the complete script tag, including Subresource Integrity attribute, by visiting https://releases.jquery.com and clicking on the version of the file that you want to use. Copy and paste that tag into your HTML file. Then, download the last version (uncompressed) and then copy the code of integration. 
- ![image](https://github.com/KDouibi/my_chatbot/assets/38917244/0f6d5c91-60b5-47dd-81e1-d8969f9d4a12)
- return to your project: index.html in the head section and paste the code you copied previously. Then, in the body of your html code add:
  <img width="455" alt="image" src="https://github.com/KDouibi/my_chatbot/assets/38917244/88c25c46-3afe-4e5d-ae41-7deb61a89301">
The result will be: 
  ![image](https://github.com/KDouibi/my_chatbot/assets/38917244/504c60ab-f698-49d6-a51f-26dccd960fbb)

PS: feel free to customize the style.css as you wish.
SEND QUESTIONS TO CHATBOT:

Now we want to keep the all the history and send the messages to the backend without changing the frontend: 
•	check more details in "index.html" / "getuserresponse" where we send the text to Python for treatment.

ANSWERING THE QUESTIONS 
The tools used for this step are:

•	Chatbots can provide real-time customer support and are therefore a valuable asset in many industries. When you understand the basics of the ChatterBot library, you can build and train a self-learning chatbot with just a few lines of Python code. The ChatterBot library combines language corpora, text processing, machine learning algorithms, and data storage and retrieval to allow you to build flexible chatbots. You can build an industry-specific chatbot by training it with relevant data. Additionally, the chatbot will remember user responses and continue building its internal graph structure to improve the responses that it can give.

•	YAML is a data serialization format designed for human readability and interaction with scripting languages. PyYAML is a YAML parser and emitter for Python. PyYAML features a complete YAML 1.1 parser, Unicode support, pickle support, capable extension API, and sensible error messages. PyYAML supports standard YAML tags and provides Python-specific tags that allow to represent an arbitrary Python object. PyYAML is applicable for a broad range of tasks from complex configuration files to object serialization and persistence.

•	spaCy is an open-source software library for advanced natural language processing, written in the programming languages Python and Cython.[3][4] The library is published under the MIT license and its main developers are Matthew Honnibal and Ines Montani, the founders of the software company Explosion.

- Check views.py for more details about the use of those librairies for this application, comments have been added to the code for better understanding.
- to train the model on a dataset, you can use a conversations available in the toolbox (we can use customized data).
    "Add from chatterbot.trainers import ChatterBotCorpusTrainer"
- If we use the corpus we don’t need the default response because the corpus has already a default answers
- We can see that now out corpus is trained about several topics:
  ![image](https://github.com/KDouibi/my_chatbot/assets/38917244/cb93ef48-b35f-4316-a31d-de4742142659)
- note that we can use another language by changing the language of the corpus
 

References:
- https://www.youtube.com/watch?v=5AmwVXIL-zU&list=PLg4ez-XXTcoMrk0qK1dDNbKywUhh3DdVr&index=2
- https://jquery.com/
- https://realpython.com/build-a-chatbot-python-chatterbot/
- https://chatterbot.readthedocs.io/en/stable/index.html
- wikipidia/spacy

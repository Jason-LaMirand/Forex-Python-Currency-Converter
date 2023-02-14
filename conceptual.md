### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
  JavaScript can run in the browser while Python is a backend server-side language.


- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
  1. You can use the get() method. 
  2. You can use setdefault() method.

- What is a unit test?
  A test that checks usually one function of code. 


- What is an integration test?
  A test to check if all the compents in an application can work together.

- What is the role of web application framework, like Flask?
  We use it as a framework to build web applications in Python. It will make it easier to make a web application.

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
  You use a URL query when you have mupltiple choices or data to sort through on a given URL page. A route is more when changing to a different html page.

- How do you collect data from a URL placeholder parameter using Flask?
  You use the request command to get information.

- How do you collect data from the query string using Flask?
  Using request.args.get().

- How do you collect data from the body of the request using Flask?
  Using request.args.get()???

- What is a cookie and what kinds of things are they commonly used for?
  A cookie is a value stored in the browser connected to a specific user. Stores small bits of the users information.

- What is the session object in Flask?
  It is stored data saved on the server. This data is saved for the user so if they login or logout they will retain the data.

- What does Flask's `jsonify()` do?
  It will return JSON data. It will convert the data into a JSON string.
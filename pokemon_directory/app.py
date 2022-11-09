# REDO THIS WITH PROPER HELPER


from flask import Flask
from helper import pets

app = Flask(__name__)

@app.route("/")
def index():
  return """
  <h1>My Pokedex</h1>
    <p>Browse through the links to discover my favorite Pokemon!</p>
    <ul>
      <li><a href='/pokemon/grass'>Grass</a></li>
      <li><a href='/pokemon/fire'>Fire</a></li>
      <li><a href='/pokemon/water'>Water</a></li>
    </ul>
  """

# Enumerate returns an object that contains a counter as a key for each value
# within the object, making items within the collection easier to access.
@app.route("/pokemon/<pet_type>")
def pokemon(pet_type):
  html = f"<h1>List of {pet_type} types:</h1>"
  html += "<ul>"

  for idx, pet in enumerate(pets[pet_type]):
    html += f"<li><a href='/pokemon/{pet_type}/{idx}'>" + pet["name"] + "</a></li>"
  html += "</ul>"
  return html

@app.route("/pokemon/<pet_type>/<int:pet_id>")
def pet(pet_type, pet_id):
  pet = pets[pet_type][pet_id]
  return f"""
  <h1>{pet['name']} #{pet['number']}</h1>
  <p>Type: {pet['type']}</p>
  <img src='{pet['photo']}'/>

  <ul>
    <li>Abilities: {pet['abilities']}</li>
    <li>Weaknesses: {pet['weaknesses']}</li>
  </ul>

  <p><a href='/'>Return Home</a></p>
  """
  







# from flask import Flask
# from helper import pets

# app = Flask(__name__)

# @app.route("/")
# def index():
#   return """
#   <h1>My Pokedex</h1>
#     <p>Browse through the links to discover my favorite Pokemon!</p>
#     <ul>
#       <li><a href='/pokemon/dogs'>Grass</a></li>
#       <li><a href='/pokemon/cats'>Fire</a></li>
#       <li><a href='/pokemon/rabbits'>Water</a></li>
#     </ul>
#   """

# # Enumerate returns an object that contains a counter as a key for each value
# # within the object, making items within the collection easier to access.
# @app.route("/pokemon/<pet_type>")
# def pokemon(pet_type):
#   html = f"<h1>List of {pet_type}</h1>"

#   html += "<ul>"
#   for idx, pet in enumerate(pets[pet_type]):
#     html += f"<li><a href='/pokemon/{pet_type}/{idx}'>" + pet["name"] + "</a></li>"
#   html += "</ul>"
#   return html

# @app.route("/pokemon/<pet_type>/<int:pet_id>")
# def pet(pet_type, pet_id):
#   pet = pets[pet_type][pet_id]
#   return f"""
#   <h1>{pet['name']}</h1>
#   <img src='{pet['url']}'/>
#   <p>{pet['description']}</p>
#   <ul>
#     <li>Breed: {pet['breed']}</li>
#     <li>Age: {pet['age']}</li>
#   </ul>
#   """

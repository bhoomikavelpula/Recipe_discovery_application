import requests
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

API_KEY = 'a4db5464f46d4c1183ebd29d94222d84'
BASE_URL = 'https://api.spoonacular.com/recipes/'

recipes = [
         {  
            "id": 1,
            "name": "Spaghetti Bolognese",
            "instructions": "1. Cook the pasta. 2. Prepare the sauce. 3. Combine and serve.",
            "image": "/static/images/spaghetti.jpg",
            "ingredients": "Spaghetti, ground beef, tomatoes, onions, garlic",
            "cuisine": "Italian"
        },
         {
            "id": 2,
            "name": "Express Chicken Curry",
            "instructions": "1. Fry the chicken. 2. Make the curry sauce. 3. Combine and simmer.",
            "image": "/static/images/chicken_curry.jpg",
            "ingredients": "Chicken, curry paste, coconut milk, onions, garlic",
            "cuisine": "Indian"
        }
]
# Route for the home page
@app.route('/')
def index():
    query = request.args.get('query', '')  # Get search query from the URL
    recipes = []

    if query:
        # Fetch recipes using the Spoonacular API
        response = requests.get(f'{BASE_URL}complexSearch', params={
            'query': query,
            'number': 10,  # Number of recipes to fetch
            'apiKey': API_KEY,
            'addRecipeInformation': True
        })
        
        if response.ok:
            data = response.json()
            recipes = [
                {
                    'name': item['title'],
                    'cuisine': item.get('cuisineType', ['Unknown'])[0],  # Default to 'Unknown'
                    'ingredients': ', '.join([ingredient['name'] for ingredient in item.get('extendedIngredients', [])]),
                    'image': item['image']
                }
                for item in data.get('results', [])
            ]
    return render_template('index.html', recipes=recipes)

# Route for adding a new recipe
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        # Process the form data here
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/recipe/<int:recipe_id>')
def recipe_detail(recipe_id):
    # Find the recipe with the given ID
    recipe = next((recipe for recipe in recipes if recipe["id"] == recipe_id), None)
    if recipe is None:
        return "Recipe not found", 404
    return render_template("recipe_detail.html", recipe=recipe)

if __name__ == '__main__':
    app.run(debug=True)

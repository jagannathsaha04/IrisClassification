from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load('FinalModel.sav')

# Mapping between species and image URLs
species_images = {
    'Setosa': 'https://upload.wikimedia.org/wikipedia/commons/5/56/Kosaciec_szczecinkowaty_Iris_setosa.jpg',
    'Versicolor': 'https://upload.wikimedia.org/wikipedia/commons/4/41/Iris_versicolor_3.jpg',
    'Virginica': 'https://upload.wikimedia.org/wikipedia/commons/9/9f/Iris_virginica.jpg'
}


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get the input values from the form
        sepallength = float(request.form['sepallength'])
        sepalwidth = float(request.form['sepalwidth'])
        petallength = float(request.form['petallength'])
        petalwidth = float(request.form['petalwidth'])

        # Make prediction using the model
        prediction = model.predict([[sepallength, sepalwidth, petallength, petalwidth]])
        predicted_species = prediction[0]

        print("Predicted Species:", predicted_species)  # Debug statement

        # Get the image URL for the predicted species
        image_url = species_images.get(predicted_species)

        print("Image URL:", image_url)  # Debug statement

        # Pass the prediction result and image URL to the HTML template
        return render_template('result.html', prediction=predicted_species, image_url=image_url)

if __name__ == '__main__':
    app.run(debug=True)
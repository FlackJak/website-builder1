from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    business_name = request.form['business_name']
    business_description = request.form['business_description']

    # Create a folder for the new website
    website_folder = os.path.join('websites', business_name)
    os.makedirs(website_folder, exist_ok=True)

    # Generate the HTML file for the new website
    with open(os.path.join(website_folder, 'index.html'), 'w') as f:
        # Create the HTML content based on the user input
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>{business_name}</title>
            <link rel="stylesheet" href="styles.css">
        </head>
        <body>
            <header>
                <h1>{business_name}</h1>
                <p>{business_description}</p>
            </header>
            <!-- Add more sections and content here -->
            <footer>
                <p>&copy; {business_name}. All rights reserved.</p>
            </footer>
        </body>
        </html>
        """
        f.write(html_content)

    return f"Website for {business_name} generated successfully!"

if __name__ == '__main__':
    app.run(debug=True)

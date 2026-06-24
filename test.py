from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Israel | Personal Website</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body {
            font-family: Arial, Helvetica, sans-serif;
            margin: 0;
            background-color: #f4f6f8;
            color: #222;
        }
        header {
            background-color: #0b3c5d;
            color: white;
            padding: 2rem;
            text-align: center;
        }
        section {
            max-width: 900px;
            margin: auto;
            padding: 2rem;
        }
        h2 {
            color: #0b3c5d;
        }
        footer {
            text-align: center;
            padding: 1rem;
            background-color: #eaeaea;
            font-size: 0.9rem;
        }
    </style>
</head>
<body>
    <header>
        <h1>Israel</h1>
        <p>Medical Student | Science Enthusiast</p>
    </header>

    <section>
        <h2>About Me</h2>
        <p>
            I am a medical student with strong interests in physics, mathematics, chemistry,
            human biology, and information technology. I focus on deep understanding and
            interdisciplinary thinking.
        </p>

        <h2>Interests</h2>
        <ul>
            <li>Pathology and Clinical Medicine</li>
            <li>Neuroscience and Consciousness</li>
            <li>Physics and Mathematical Modeling</li>
            <li>Medical Technology and Prosthetics</li>
        </ul>

        <h2>Contact</h2>
        <p>Email: yourname@example.com</p>
    </section>

    <footer>
        © 2025 Israel
    </footer>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(debug=True)

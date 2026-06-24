from flask import Flask, render_template_string

app = Flask(__name__)

BASE_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap" rel="stylesheet">
    <style>
        body {
            margin: 0;
            font-family: 'Inter', sans-serif;
            background: linear-gradient(135deg, #0f172a, #020617);
            color: #e5e7eb;
        }
        nav {
            display: flex;
            justify-content: space-between;
            padding: 1.2rem 3rem;
            background: rgba(2, 6, 23, 0.7);
            backdrop-filter: blur(10px);
            position: sticky;
            top: 0;
        }
        nav a {
            color: #e5e7eb;
            margin-left: 1.5rem;
            text-decoration: none;
            font-weight: 500;
        }
        nav a:hover {
            color: #38bdf8;
        }
        .container {
            max-width: 1000px;
            margin: auto;
            padding: 4rem 2rem;
        }
        h1 {
            font-size: 3rem;
            margin-bottom: 1rem;
        }
        p {
            line-height: 1.7;
            font-size: 1.1rem;
            color: #cbd5f5;
        }
        footer {
            text-align: center;
            padding: 2rem;
            color: #94a3b8;
        }
        .card {
            background: rgba(15, 23, 42, 0.8);
            border-radius: 16px;
            padding: 2.5rem;
            box-shadow: 0 20px 40px rgba(0,0,0,0.4);
        }
    </style>
</head>
<body>
    <nav>
        <div><strong>Israel</strong></div>
        <div>
            <a href="/">Home</a>
            <a href="/about">Description</a>
            <a href="/contact">Contact</a>
        </div>
    </nav>

    <div class="container">
        <div class="card">
            {{ content }}
        </div>
    </div>

    <footer>
        © 2025 Israel · Built with Python & Flask
    </footer>
</body>
</html>
"""

@app.route("/")
def home():
    content = """
    <h1>Welcome</h1>
    <p>
        This is the personal site of Israel, a medical student with a deep commitment to
        scientific rigor, critical thinking, and interdisciplinary mastery.
    </p>
    """
    return render_template_string(BASE_HTML, title="Home", content=content)

@app.route("/about")
def about():
    content = """
    <h1>About Me</h1>
    <p>
        Israel is a medical student driven by first‑principles thinking and an exceptional
        curiosity that spans medicine, physics, mathematics, chemistry, and information
        technology. His learning style prioritizes deep conceptual understanding over
        memorization, with a constant focus on mechanism, causality, and clinical relevance.
    </p>
    <p>
        He is particularly interested in neurology, pathology, and the future of medicine,
        including advanced prosthetics and human–machine integration. His long‑term goal is
        to contribute to affordable, high‑impact medical innovations while maintaining
        patient‑centered care and ethical clarity.
    </p>
    """
    return render_template_string(BASE_HTML, title="Description", content=content)

@app.route("/contact")
def contact():
    content = """
    <h1>Contact</h1>
    <p>Email: <strong>your_email_here@example.com</strong></p>
    <p>
        Feel free to reach out for academic collaboration, research discussions, or
        intellectually rigorous conversations.
    </p>
    """
    return render_template_string(BASE_HTML, title="Contact", content=content)

if __name__ == "__main__":
    app.run(debug=True)

"""
HOSTING PREPARATION (Production):

1. requirements.txt
-------------------
Flask==3.0.0
Gunicorn==21.2.0

2. Procfile (for Render / Heroku)
--------------------------------
web: gunicorn app:app

3. Run locally
--------------
pip install -r requirements.txt
python app.py

4. Recommended hosts
--------------------
Render, Railway, Fly.io

5. Disable debug=True in production
-----------------------------------
app.run()
"""

# app.py
# Modern personal website using Flask
# Run: python app.py
# Then open http://127.0.0.1:5000

from flask import Flask, render_template_string

app = Flask(__name__)

BASE_HTML = """
<!DOCTYPE html>
<html lang=\"en\">
<head>
    <meta charset=\"UTF-8\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
    <title>{{ title }}</title>
    <style>
        :root {
            --bg: #0b0e14;
            --fg: #e6e9ef;
            --accent: #7aa2f7;
            --accent2: #9ece6a;
        }
        * { box-sizing: border-box; }
        body {
            margin: 0;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: radial-gradient(circle at 20% 20%, #1a1f2e, var(--bg));
            color: var(--fg);
        }
        nav {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 1.2rem 2rem;
            backdrop-filter: blur(10px);
        }
        nav a {
            color: var(--fg);
            text-decoration: none;
            margin-left: 1.5rem;
            font-weight: 500;
        }
        nav a:hover { color: var(--accent); }
        .container {
            max-width: 1100px;
            margin: 0 auto;
            padding: 4rem 2rem;
        }
        h1 {
            font-size: clamp(2.5rem, 5vw, 4rem);
            line-height: 1.1;
            margin-bottom: 2rem;
        }
        p {
            font-size: 1.2rem;
            line-height: 1.8;
            max-width: 900px;
        }
        .shapes {
            position: fixed;
            inset: 0;
            overflow: hidden;
            z-index: -1;
        }
        .shape {
            position: absolute;
            border-radius: 20px;
            opacity: 0.15;
            animation: float 20s linear infinite;
        }
        .shape.one {
            width: 300px; height: 300px;
            background: var(--accent);
            top: 10%; left: 5%;
        }
        .shape.two {
            width: 200px; height: 200px;
            background: var(--accent2);
            bottom: 15%; right: 10%;
            animation-duration: 28s;
        }
        @keyframes float {
            0% { transform: translateY(0) rotate(0deg); }
            50% { transform: translateY(-40px) rotate(20deg); }
            100% { transform: translateY(0) rotate(0deg); }
        }
        .card {
            background: rgba(255,255,255,0.05);
            border-radius: 20px;
            padding: 3rem;
            box-shadow: 0 20px 40px rgba(0,0,0,0.4);
        }
        footer {
            text-align: center;
            padding: 2rem;
            opacity: 0.7;
        }
    </style>
</head>
<body>
    <div class=\"shapes\">
        <div class=\"shape one\"></div>
        <div class=\"shape two\"></div>
    </div>

    <nav>
        <strong>Israel</strong>
        <div>
            <a href=\"/\">Home</a>
            <a href=\"/about\">Description</a>
            <a href=\"/contact\">Contact</a>
        </div>
    </nav>

    <div class=\"container\">
        {{ content|safe }}
    </div>

    <footer>
        © {{ year }} Israel
    </footer>
</body>
</html>
"""

@app.route("/")
def home():
    content = """
    <div class='card'>
        <h1>Thinking Across Medicine, Science, and Technology</h1>
        <p>
        I explore medicine through the lenses of physics, mathematics, chemistry, and computation, 
        driven by a desire to understand systems deeply and improve human life through knowledge and design.
        </p>
    </div>
    """
    return render_template_string(BASE_HTML, title="Home", content=content, year=2025)

@app.route("/about")
def about():
    content = """
    <div class='card'>
        <h1>A Description</h1>
        <p>
        Israel is a medical student defined by intellectual breadth and deliberate depth. His thinking
        is system-oriented: biological processes are never isolated from physics, chemistry, or
        information theory. He approaches medicine not merely as a clinical discipline, but as an
        engineering problem grounded in human biology.
        <br><br>
        Curiosity guides his work. From cellular pathology to neural signaling, from abstract
        mathematics to applied computing, he seeks unifying principles that explain function,
        failure, and repair. His long-term vision centers on advancing treatment methods,
        integrating technology with the human body, and preserving identity while enhancing
        capability.
        <br><br>
        Above all, his work is anchored in clarity of thought, ethical responsibility, and
        patient-centered impact.
        </p>
    </div>
    """
    return render_template_string(BASE_HTML, title="Description", content=content, year=2025)

@app.route("/contact")
def contact():
    content = """
    <div class='card'>
        <h1>Contact</h1>
        <p>
        Email: <strong>your_email@example.com</strong>
        </p>
    </div>
    """
    return render_template_string(BASE_HTML, title="Contact", content=content, year=2025)

if __name__ == "__main__":
    app.run(debug=True)

# Hosting preparation:
# 1. Create requirements.txt with:
#    flask
# 2. For production, use gunicorn:
#    gunicorn app:app
# 3. Ready for platforms like Render, Railway, or Fly.io

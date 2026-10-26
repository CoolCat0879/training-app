from flask import Flask, jsonify, send_from_directory, request

app = Flask(__name__)

@app.route("/")
def index():
    html = """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Троеборье — Учет тренировок</title>
        <meta name="description" content="Веб-приложение для учета тренировок по троеборью и сравнения результатов в разных условиях.">
    </head>
    <body>
        <h1>Веб-приложение для учета тренировок</h1>
        <p>Здесь вы сможете записывать свои результаты.</p>
    </body>
    </html>
    """
    return html

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

@app.route("/trainings")
def trainings():
    return jsonify({"trainings": []})

@app.route('/robots.txt')
def robots_txt():
    return send_from_directory('static', 'robots.txt')

@app.route('/sitemap.xml')
def sitemap_xml():
    return send_from_directory('static', 'sitemap.xml')

@app.after_request
def add_security_headers(response):
    # Заголовок добавляется ТОЛЬКО для API, чтобы не блокировать главную страницу
    if request.path.startswith('/api') or request.path == '/health' or request.path == '/trainings':
        response.headers['X-Robots-Tag'] = 'noindex, nofollow'
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
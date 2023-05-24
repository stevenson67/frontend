from flask import Flask, jsonify, request
import string
import random

   app = Flask(__name__)

   links = {}

   @app.route("/api/shorten", methods=["POST"])
   def shorten_link():
       url = request.json.get("url")

       if url:
           slug = "".join(random.choices(string.ascii_letters + string.digits, k=8))
           links[slug] = url
           short_url = "http://410web/{slug}"
           return jsonify({"short_url": short_url})

       return jsonify({"error": "Invalid URL"}), 400

   @app.route("/<slug>")
   def redirect_to_original(slug):
       if slug in links:
           return jsonify({"url": links[slug]})

       return jsonify({"error": "Link not found"}), 404

   if name == "main":
       app.run()

from flask import Flask, render_template, request, jsonify
from ml.ml_pipeline import analyze_review_with_prediction
from stats import register_stats_route

app = Flask(__name__)

register_stats_route(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analytics")
def analytics():
    return render_template("analytics.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        data = request.get_json(silent=True)

        if not data:
            return jsonify({"error": "No review data was provided."}), 400

        review = data.get("review")

        if not isinstance(review, str):
            return jsonify({"error": "Review must be text."}), 400

        review = review.strip()

        if not review:
            return jsonify({"error": "Review text is empty."}), 400

        if len(review) > 10000:
            return jsonify({"error": "Review is too long."}), 400

        result = analyze_review_with_prediction(review)

        if "error" in result:
            return jsonify(result), 500

        return jsonify(result)

    except Exception as error:
        return jsonify({
            "error": "Analysis failed.",
            "details": str(error)
        }), 500


if __name__ == "__main__":
    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000
    )

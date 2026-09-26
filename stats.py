from flask import jsonify


PROJECT_STATS = {

    "dataset": {
        "training_reviews": 126831,
        "test_reviews": 21679,
        "training_conditions": 791,
        "validation_conditions": 606,
        "tfidf_features": 100000,
    },

    "model": {
        "name": "Linear Support Vector Machine",
        "algorithm": "LinearSVC",
        "accuracy": 0.7676,
        "macro_f1": 0.5090,
        "weighted_f1": 0.7694,
        "classes": 791,
    },

    "comparison": [

        {
            "name": "Logistic Regression",
            "accuracy": 0.6360,
            "macro_f1": 0.0907,
            "weighted_f1": 0.5794,
        },

        {
            "name": "Linear SVM",
            "accuracy": 0.8129,
            "macro_f1": 0.5610,
            "weighted_f1": 0.8015,
        },

        {
            "name": "Cleaned Linear SVM",
            "accuracy": 0.8173,
            "macro_f1": 0.6008,
            "weighted_f1": 0.8083,
        },

        {
            "name": "Final Memory-Safe Linear SVM",
            "accuracy": 0.7676,
            "macro_f1": 0.5090,
            "weighted_f1": 0.7694,
        },

    ],

    "nlp_modules": 23,
}


def register_stats_route(app):

    @app.route("/api/stats")
    def stats():

        return jsonify(
            PROJECT_STATS
        )

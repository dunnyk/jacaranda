from flask import request, jsonify
from helpers.process import process_computation
from flask_restx import Api, Resource, fields
from sentry_sdk.integrations.flask import FlaskIntegration
from app import create_app
from config import AppConfig
import sentry_sdk


app = create_app()
api = Api(app)

sentry_sdk.init(
    dsn=AppConfig.SENTRY_DSN, integrations=[FlaskIntegration()], traces_sample_rate=1.0
)

division_model = api.model(
    "Division",
    {
        "dividend": fields.Integer(required=True, description="The dividend"),
        "divisor": fields.Integer(required=True, description="The divisor"),
    },
)


@api.expect(division_model)
@api.route("/api/divide")
class DivisionComputation(Resource):
    @api.expect(division_model)
    def post(self):
        try:
            data = request.get_json()
            return process_computation(data)

        except Exception as error:
            sentry_sdk.capture_exception(error)
            return jsonify({"error": str(error)}), 500


if __name__ == "__main__":
    app.run(debug=True, port=8080, host="0.0.0.0")

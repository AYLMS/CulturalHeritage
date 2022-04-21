from flask import abort, jsonify
from flask_restful import Resource
from flask_simplelogin import login_required

from app.models import Object


class ProductResource(Resource):
    def get(self):
        products = Object.query.all() or abort(204)
        return jsonify({"object": [product.to_dict() for product in products]})

    @login_required(basic=True, username="admin")
    def post(self):
        """
        Creates a new product.

        Only admin user authenticated using basic auth can post
        Basic takes base64 encripted username:password.

        # curl -XPOST localhost:5000/api/v1/product/ \
        #  -H "Authorization: Basic Y2h1Y2s6bm9ycmlz" \
        #  -H "Content-Type: application/json"
        """
        return NotImplementedError(
            "Someone please complete this example and send a PR :)"
        )


class ProductItemResource(Resource):
    def get(self, product_id):
        product = Object.query.filter_by(id=product_id).first() or abort(404)
        return jsonify(product.to_dict())

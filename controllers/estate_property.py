from odoo import http
from odoo.http import request
import json
import requests

version = "/api/v1"

def convert_estate_property_to_json(estate_property):
    result = {
        "name": estate_property.name,
        "postcode": estate_property.postcode,
    }
    return result

class EstateProperty(http.Controller):
    @http.route(version + "/estate-property", type="http", auth="public")
    def get_estate_property(self):
        estate_properties = request.env["estate.property"].sudo().search([])
        models = []
        for estate_property in estate_properties:
            models.append(convert_estate_property_to_json(estate_property))
        return request.make_response(json.dumps(models))


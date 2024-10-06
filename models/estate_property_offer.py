from email.policy import default

from odoo import api, fields, models

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Estate Property Offer"

    partner_id = fields.Many2one("res.partner", string="Partner", required=True)
    price = fields.Float(required=True)
    state = fields.Selection(selection = [("accepted", "Accepted"), ("refused", "Refused"), ("waiting", "Waiting")],
                             default="waiting", required=True)
    estate_property_id = fields.Many2one("estate.property", string="Estate Property", required=True)
from odoo import api, fields, models
from datetime import timedelta

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Estate Property Offer Model"

    partner_id = fields.Many2one("res.partner", string="Customer", required=True)
    price = fields.Float(required=True)
    validity = fields.Integer()
    deadline = fields.Date(compute='_compute_deadline', inverse='_inverse_deadline')
    state = fields.Selection(selection = [("accepted", "Accepted"), ("refused", "Refused"), ("waiting", "Waiting")],
                             default="waiting", required=True)
    estate_property_id = fields.Many2one("estate.property", string="Estate Property", required=True)

    @api.depends('create_date', 'validity')
    def _compute_deadline(self):
        for rec in self:
            if rec.create_date:
                rec.deadline = rec.create_date + timedelta(days=rec.validity)
            else:
                rec.deadline = False

    def _inverse_deadline(self):
        for rec in self:
            if rec.create_date and rec.deadline:
                rec.validity = (rec.deadline - rec.create_date.date()).days
            else:
                rec.validity = 0

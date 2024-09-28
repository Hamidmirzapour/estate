from odoo import models, fields, api
from odoo.exceptions import ValidationError

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate Property"

    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(default=fields.Datetime.now)
    expected_price = fields.Float()
    selling_price = fields.Float()
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    total_area = fields.Integer(compute="_compute_total_area", readonly=True)
    garden_orientation = fields.Selection(
        selection=[("N", "North"), ("S", "South"), ("E", "East"), ("W", "West")],
        default="N", string="Garden Orientation"
    )
    user_id = fields.Many2one("res.users", string="Salesman", default=lambda self: self.env.user)
    buyer_id = fields.Many2one("res.partner", string="Buyer", readonly=True, copy=False)

    _sql_constraints = [
        (
            'unique_name',
            'UNIQUE(name)',
            'The name field should be unique.',
        )
    ]

    @api.constrains("expected_price", "selling_price")
    def check_prices(self):
        for rec in self:
            if rec.expected_price <= 0.0:
                raise ValidationError("The expected price should be greater than 0.0")
            if rec.selling_price <= 0.0:
                raise ValidationError("The selling price should be greater than 0.0")

    @api.depends("living_area", "garden_area")
    def _compute_total_area(self):
        for rec in self:
            rec.total_area = rec.living_area + rec.garden_area


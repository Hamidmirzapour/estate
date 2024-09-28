from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError

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
    state = fields.Selection(
        selection=[('new', 'New'),
                   ('ready', 'Ready'),
                   ('offer_received', 'Offer Received'),
                   ('offer_accepted', 'Offer Accepted'),
                   ('sold', 'Sold'),
                   ('canceled', 'Canceled')],
        string="Status",
        default = "new",
        required=True
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

    def action_sold(self):
        if self.state == 'canceled':
            raise ValidationError("Canceled estate property can not be sold.")
        self.state = "sold"

    def action_cancel(self):
        if self.state == 'sold':
            raise ValidationError("sold estate property can not be canceled.")
        self.state = "canceled"

    @api.model
    def create(self, vals):
        if vals.get("selling_price") and vals.get("date_availability"):
            vals["state"] = "ready"
        return super().create(vals)

    def unlink(self):
        if self.state not in ["new", "canceled"]:
            raise UserError("Only estate properties with new or canceled state can be deleted.")
        return super().unlink()
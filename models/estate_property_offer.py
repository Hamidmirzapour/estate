from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
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

    @api.autovacuum
    def _clear_unused_offers(self):
        refused_offers = self.search([('state', '=', 'refused')]).unlink()
        if refused_offers:
            refused_offers.unlink()

    @api.model_create_multi
    def create(self, vals):
        for rec in vals:
            if not rec.get('create_date'):
                rec['create_date'] = fields.Datetime.now()
        return super(EstatePropertyOffer, self).create(vals)

    @api.constrains('deadline')
    def _check_deadline(self):
        for rec in self:
            if rec.deadline and rec.create_date:
                if rec.deadline < rec.create_date.date():
                    raise ValidationError(_('Deadline can not be before create date'))
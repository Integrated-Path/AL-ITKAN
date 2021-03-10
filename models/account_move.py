from odoo import models, fields, api, _
from odoo.exceptions import UserError

class AccountMoveLine(models.Model):
    _inherit =  "account.move.line"

    # CALLING THE DEFUALT FIELDS ONLY TO OVERPASS A BUG. DON'T TOUCH !!
    date = fields.Date()
    account_id = fields.Many2one()
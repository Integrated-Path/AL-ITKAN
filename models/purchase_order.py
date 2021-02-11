# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
from datetime import datetime

class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    product_smn = fields.Char(string="SMN")
    # product_id = fields.Many2one(readonly=False)

    @api.model
    def create(self, values):
        if values.get("product_smn"): #Adding Product By Just Import SMN code
            smn = values["product_smn"]
            product_id = self.env['product.product'].search([('default_code', 'like', smn)])
            if len(product_id) > 1:
                raise UserError(_(f"More Than One Product Of The SMN {smn} Was Found. Please Contact Support"))
            elif len(product_id) == 1:
                values['product_id'] = product_id.id
                values['product_uom'] = product_id.uom_id.id
                values['date_planned'] = datetime.today().strftime(DEFAULT_SERVER_DATETIME_FORMAT)
            else:
                raise UserError(_(f"A Product with SMN {smn} was not  found"))
            
        else:
          pass

        result = super(PurchaseOrderLine, self).create(values)
        
        return result
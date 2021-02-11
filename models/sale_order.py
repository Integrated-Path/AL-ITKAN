# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError
import datetime


class ItkanSale(models.Model): #this is implemented because they wanted the sale order date to be editable
    _inherit="sale.order"

    date_order = fields.Date(string="Order Date", default=datetime.datetime.now())

class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    product_smn = fields.Char(string="SMN")

    @api.model
    def create(self, values):
        if values.get("product_smn"):
            smn = values["product_smn"]
            product_id = self.env['product.product'].search([('default_code', 'like', smn)])
            if len(product_id) > 1:
                raise UserError(_(f"More Than One Product Of The SMN {smn} Was Found. Please Contact Support"))
            elif len(product_id) == 1:
                values['product_id'] = product_id.id
            else:
                raise UserError(_(f"A Product with SMN {smn} was not  found"))
        else:
          pass
          
        result = super(SaleOrderLine, self).create(values)
        
        return result
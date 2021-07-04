# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
from datetime import datetime

class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    sent_prouduct_info = fields.Boolean(copy=False, help="To know if this PO info was send to the Discuss group")

    def send_proudct_info_button(self):
        # sending products info to discuss channel (grouop)
        html_body = f'Order Number: {self.name}<br/><ul>'
        for line in self.order_line:
            html_body += f"<li>{line.product_id.display_name}:</li> <li class='o_indent'><ul>"

            html_body += f'<li>Quantity: {line.product_qty}</li>'
            if line.serial_number:
                html_body += f'<li>Serial Number: {line.serial_number}</li>'
            if line.customer_id:
                html_body += f'<li>Customer: {line.customer_id.name}</li>'
            if line.brand_id:
                html_body += f'<li>Modality: {line.brand_id.name}</li>'

            html_body += "</ul></li><br/>"

        html_body += '</ul>'
        channel_id = self.env['mail.channel'].search([('name', '=', 'Modality Managers')], limit=1)

        if not channel_id:
            channel_id = self.env['mail.channel'].create({'name': 'Modality Managers'})

        # creating 2 messages intead of one to avoid entering & reading PO chances (they are itkan)
        channel_id.message_post(
            body= html_body ,
            message_type='notification',
            subtype='mail.mt_comment',
            partner_ids= [partner_id.id for partner_id in channel_id.channel_partner_ids]
            )

        self.message_post(
            body= html_body ,
            message_type='notification',
            subtype='mail.mt_comment',
            )

        self.sent_prouduct_info = True

    def button_confirm(self):
        for line in self.order_line:
            if line.product_id.categ_id.id == 1:
                raise UserError(_(f"Please set a category for product {line.product_id.display_name} before confirming this purchase order"))
                return
            else:
                pass

        res = super(PurchaseOrder, self).button_confirm()
        return res


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    product_smn = fields.Char(string="SMN")
    serial_number = fields.Char(string="Serial Number", copy=False)
    customer_id = fields.Many2one("res.partner", string="Customer", copy=False, domain="['|', ('company_id', '=', company_id), ('company_id', '=', False)]")
    brand_id = fields.Many2one('contract.modality', string="Modality", copy=False)

    # For importing products by SMN
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
        
#         if values.get('product_id') and not values.get('name'):
#             product_id = self.env['product.product'].browse( values.get('product_id') )  
#             values['name'] = product_id.name

        result = super(PurchaseOrderLine, self).create(values)
        
        return result

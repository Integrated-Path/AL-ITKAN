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
            html_body += f'<li>{line.product_id.name}: {line.product_qty} Quantity</li>'
        html_body += '</ul>'
        channel_id = self.env['mail.channel'].search([('name', '=', 'Modality Managers')], limit=1)

        if not channel_id:
            channel_id = self.env['mail.channel'].create({'name': 'Modality Managers'})

        # creating 2 messages intead of one to avoid entering & reading PO chances (they are itkan)
        message_values = {
            'body': html_body,
            'author_id': self.env.user.partner_id.id,
            'channel_ids': [channel_id.id],
            'message_type': 'notification',
            # its not sending notification
            # 'partner_ids': [partner_id.id for partner_id in channel_id.channel_partner_ids]
        }
        self.env['mail.message'].create(message_values)
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

        result = super(PurchaseOrderLine, self).create(values)
        
        return result
# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError

class ResPartner(models.Model):
    _inherit = "res.partner"

    # N.A Record id is => 21362

    @api.model
    def create(self, values):
        """ Itakn DataBase is suffering from an issue with creating record.
        This function is to handle that error """
        na_record = self.env['res.partner'].browse([21362])
        if values.get("name", False):
            result = super(ResPartner, self).create(values)    
            return result
        else:
            return na_record

    def unlink(self):
        for line in self:
            if line.id == 21362:
                raise UserError(_("You can not delete this contact cause it is being used by the support team"))
            else:
                res = super(ResPartner, line).unlink()
                return res
    
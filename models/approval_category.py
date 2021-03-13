from odoo import models, fields, api


class ApprovalCategory(models.Model):
    _inherit = "approval.category"

    limited_users_ids = fields.Many2many(comodel_name='res.users', relation="limited_users_table", column1="approval_category_col", column2="res_user_col", string='Limited Users')

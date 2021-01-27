from odoo import models, fields, api
from odoo.exceptions import UserError

class HrExpenses(models.Model):
    _inherit = "hr.expense"
    
    analytic_account_id = fields.Many2one("account.analytic.account", readonly=True)

class HrExpensesSheet(models.Model):
    _inherit = "hr.expense.sheet"

    analytic_account_id = fields.Many2one("account.analytic.account", string="Budget", domain="[('company_id', 'in', [company_id, False] )]")

    @api.constrains("analytic_account_id", "expense_line_ids")
    def _get_analytic_account(self):
        for report in self:
            for line in report.expense_line_ids:
                line.analytic_account_id = report.analytic_account_id.id
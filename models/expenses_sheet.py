from odoo import models, fields, api
from odoo.exceptions import UserError

class HrExpenses(models.Model):
    _inherit = "hr.expense"
    
    product_id = fields.Many2one(states={'draft': [('readonly', False)], 'reported': [('readonly', False)], 'approved': [('readonly', False)], 'refused': [('readonly', False)]})

class HrExpensesSheet(models.Model):
    _inherit = "hr.expense.sheet"

    analytic_account_id = fields.Many2one("account.analytic.account", string="Budget", domain="[('company_id', 'in', [company_id, False] )]")
    expense_line_ids = fields.One2many(states={'done': [('readonly', True)], 'post': [('readonly', True)]})

    # This is the original Function
    @api.constrains("analytic_account_id", "expense_line_ids")
    def _get_analytic_account(self):
        for report in self:
            for line in report.expense_line_ids:
                line.analytic_account_id = report.analytic_account_id.id

    def approve_expense_sheets(self):
        if not self.user_has_groups('hr_expense.group_hr_expense_team_approver'):
            raise UserError(_("Only Managers and HR Officers can approve expenses"))
        elif not self.user_has_groups('hr_expense.group_hr_expense_manager'):
            current_managers = self.employee_id.expense_manager_id | self.employee_id.parent_id.user_id | self.employee_id.department_id.manager_id.user_id

            # if self.employee_id.user_id == self.env.user:
            #     raise UserError(_("You cannot approve your own expenses"))

            # if not self.env.user in current_managers and not self.user_has_groups('hr_expense.group_hr_expense_user') and self.employee_id.expense_manager_id != self.env.user:
            #     raise UserError(_("You can only approve your department expenses"))

        responsible_id = self.user_id.id or self.env.user.id
        self.write({'state': 'approve', 'user_id': responsible_id})
        self.activity_update()

from odoo import models, fields, api
from odoo.exceptions import UserError

class CalendarEvent(models.Model):
    _inherit = "calendar.event"
    send_email_to_attendees = fields.Boolean(string="Send Email")

    def create_attendees(self):
        self = self.with_context(detaching= (not self.send_email_to_attendees) )
        res = super(CalendarEvent, self).create_attendees()
        return res

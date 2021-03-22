from odoo import models, fields, api
from odoo.exceptions import UserError

class CalendarEvent(models.Model):
    _inherit = "calendar.event"
    send_email_to_attendees = fields.Boolean(string="Send Email")


class Attendee(models.Model):
    _inherit = "calendar.attendee"

    def _send_mail_to_attendees(self, template_xmlid, force_send=False, force_event_id=None):
        if not self.event_id.send_email_to_attendees:
            pass
        else:
            res = super(Attendee, self)._send_mail_to_attendees(template_xmlid=template_xmlid, force_send=force_send, force_event_id=force_event_id)
            return res

 # -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import UserError

class StudentInfoWizard(models.TransientModel):
    _name = 'student.info.wizard'
    _description = 'Student Information Wizard'

    student_id = fields.Many2one('university.student', string='Student')

    # Add any fields or methods you need for the wizard

    def do_something(self):
        if self.student_id:
            # Update the registration date of the selected student to the current date
            self.student_id.registration_date = fields.Date.today()
            return {'type': 'ir.actions.act_window_close'}
        else:
            # If no student is selected, you can raise a user error or take appropriate action
            raise UserError('Please select a student before proceeding.')
        return True
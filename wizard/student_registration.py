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




















#
# from odoo import models, fields, api
#
#
# class StudentRegistration(models.TransientModel):
#     _name = 'university.student.wizard'
#     _description = 'Register a Student'
#
#     name = fields.Text(
#         string="Student's name",
#         required=True
#     )
#
#     recruitment = fields.Date(
#         string="Recruitment Date",
#         required=True
#     )
#
#     # @api.multi
#     def register(self):
#         student = self.env['university.student'].browse(self.env.context.get('active_ids'))
#
#             # create({'name': self.name,
#             #                                       'date': self.date,
#             #                                       })
#         for stud in student:
#             stud.write({'state': 'done'})
#
#         # return {
#         #     'type': 'ir.actions.act_window',
#         #     'name': _('message'),
#         #     'res_model': 'student_registration',
#         #     'target': 'new',
#         #     'view_mode': 'form',
#         #     'view_type': 'form',
#         #     'context': {'default_name':self.id},
#         # }
#     def create_wizard(self):
#         wizard = self.env['university.student.wizard'].create({'test_field': self.name
#                                                        })
#         return {
#             'name': _('Test Wizard'),
#             'type': 'ir.actions.act_window',
#             'res_model': 'university.student.wizard',
#             'view_mode': 'form',
#             'res_id':'wizard.id',
#             'target': 'new',
#         }
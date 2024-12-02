# -*- coding: utf-8 -*-

# from server.odoo import models, fields, api
from odoo import models, fields, api


class UniversityStudents(models.Model):
    _name = 'university.student'
    _description = 'Student list'

    f_name = fields.Char(
        string='First name'
    )
    l_name = fields.Char(
        string='Last name'
    )
    sex = fields.Selection(
        selection=[
            ('male','male'),('female','female')
        ])
    identity_card = fields.Char(
        string='Identity Card'
    )
    address = fields.Text(
        string='Address'
    )
    birthday = fields.Date(
        string='Birthday'
    )
    registration_date = fields.Date(
        string='Registration Date'
    )
    email = fields.Char()
    phone = fields.Char()

    state = fields.Selection(
        selection=[
            ('l1','Level 1'),
            ('l2','Level 2'),
            ('l3','Level 3'),
            ('finished','Finished'),
        ])

    department_id = fields.Many2one(
        comodel_name='university.department'
    )
    classroom_id = fields.Many2one(
        comodel_name='university.classroom'
    )

    subject_ids = fields.Many2many(
        related='classroom_id.subject_ids'
    )

    @api.model_create_multi
    def name(self):
        result = []
        for student in self:
            name = '[' + student.classroom_id.classroom_name + ']' + student.f_name + ' ' + student.l_name
            result.append((student.id, name))
        return result

    @api.constrains('registration_date', 'birthday')
    def check_dates(self):
        if self.birthday > self.registration_date:
            raise ValueError('The birthday must be inferior than the registration date')

    @api.model_create_multi
    @api.constrains
    def next_level(self):
        if self.state == 'l1':
            return self.write({'state':'l2'})
        elif self.state == 'l2':
            return self.write({'state': 'l3'})
        elif self.state == 'l3':
            return self.write({'state':'finished'})
        else:
            raise ValueError('This student has already finished his courses')
        # elif self.state == 'finished':
        #     return {'warning': {'title':'Finished',
        #                         'message': 'This student has already finished his courses'}}

    def create_wizard(self):
        # wizard = self.env['student.info.wizard'].create({'student_id': self.name})
        return {
            'name': 'Test Wizard',
            'type': 'ir.actions.act_window',
            'res_model': 'student.info.wizard',
            'view_mode': 'form',
            # 'res_id': 'wizard.id',
            'target': 'new',
            'context': {}
        }
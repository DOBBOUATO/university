# -*- coding: utf-8 -*-

# from server.odoo import models, fields, api
from odoo import models, fields, api

class UniversityInstructor(models.Model):
    _name = 'university.instructor'
    _description = 'university.instructor'

    f_name = fields.Char('First name')
    l_name = fields.Char('Last name')
    sex = fields.Selection([('male', 'male'), ('female', 'female')])
    identity_card = fields.Char('Identity Card')
    address = fields.Text('Address')
    birthday = fields.Date('Birthday')
    recruitment_date = fields.Datetime('Date of Recruitment')
    # fields.DateTime('Date of Recruitment')
    email = fields.Char()
    phone = fields.Char()

    department_id = fields.Many2one(comodel_name='university.department')
    subject_id = fields.Many2one(comodel_name='university.subject')

    classroom_ids = fields.Many2many(comodel_name='university.classroom',
                                     relation='inst_class_rel',
                                     column1='f_name',
                                     column2='name')

    @api.model_create_multi
    def name(self):
        result = []
        for instructor in self:
            name = '[' + instructor.department_id.name + ']' + instructor.f_name + ' ' + instructor.l_name
            result.append((instructor.id, name))
        return result


# -*- coding: utf-8 -*-
{
    'name': "University",

    'summary': """
        Download this module to easily manage your university processes""",

    'description': """
        This modules helps universities manage their 
        administrative, technical and facilities staff. It equally helps manage 
        students and their courses, departments, classrooms and from the moment they registered 
        at the university.  
    """,

    'author': "TITANIUM SYSTEMS/Bouato Donald",
    'website': "http://www.titanium.cm",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Project Management',
    'version': '0.1',

    # 'icon': 'app_icon2.png',
    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'web_tour',
    ],

# so that it becomes an application
    'application': True,
# such that it appears at the front of the apps interface
    'sequence': -100,

    'installable': True,
    'auto_install': False,

# always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/university_security.xml',
        'views/student_views.xml',
        'views/department_views.xml',
        'views/instructor_views.xml',
        'views/classroom_views.xml',
        'views/subject_views.xml',
        'wizard/student_registration_view.xml',
    ],
# only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'post_init_hook': '_synchronize_cron',
    'license': 'LGPL-3',
}

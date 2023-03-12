# -*- coding: utf-8 -*-
{
    'name': "Kanban para empresas",
    'summary': "Tabla kanban para organizar tarefas",
    'description': """
Organizar as tarefas
==============
Con este módulo pódese organizar o estado das tarefas dunha empresa sen problema
    """,
    'author': "Marcos Caamaño Mayo",
    'website': "https://github.com/a21marcoscm/modulo-a21marcoscm_organizar_tarefas",
    'category': 'Tools',
    'version': '14.0.1',
    'depends': ['base'],
    'application': True,

    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/tarefas.xml',
        'views/estado_tarefas.xml',
    ],
    'demo':[
        'data/demo.xml'
    ]
}


# -*- coding: utf-8 -*-
from odoo import models, fields, api


class EstadoTarefas(models.Model):
    _name = 'estado.tarefas'
    _description = 'Estados dispoñibles para as tarefas'
    _parent_store = False

    name = fields.Char('Nome estado', required=True)
    description = fields.Text('Descrición do estado', default='Descrición non especificada')
    tarefas_ids = fields.One2many('tarefas','status_id', string='Tarefas solicitadas')
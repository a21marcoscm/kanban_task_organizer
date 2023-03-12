# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api

class Tarefas(models.Model):
    _name = 'tarefas'
    _description = 'Tarefas da empresa'

    name = fields.Char('Titulo da tarefa', required=True)
    description = fields.Char('Descición da tarefa')
    application_date = fields.Date('Día de solicitude', required=True, default=fields.Date.today())
    applicant_id = fields.Many2one('res.partner', string='Solicitante')
    status_id = fields.Many2one('estado.tarefas', string='Estado', required=True, ondelete='restrict', group_expand='_show_all_estados')
    days_from_request = fields.Integer('Días pasados dende a solicitude', compute='_calculate_elapsed_days', compute_sudo=True, store=False)

    @api.depends('application_date')
    def _calculate_elapsed_days(self):
        today = fields.Date.today()
        for tarefa in self.filtered('application_date'):
            if tarefa.application_date:
                delta = today - tarefa.application_date
                tarefa.days_from_request = delta.days
            else:
                tarefa.days_from_request = 0

    @api.constrains('application_date') 
    def _check_release_date(self): 
        for tarefa in self: 
            if tarefa.application_date > fields.Date.today():
                raise models.ValidationError('Non se poden rexistrar solicitudes futuras')
            
    @api.model
    def _show_all_estados(self,stages,domain,order): #Intento de que se recuperen los ids de todos los estados para visualizarlos en el kanban
        return self.env['estado.tarefas'].search([]) 

class ResPartner(models.Model):
    _inherit = 'res.partner'
    tarefas_ids = fields.One2many('tarefas','applicant_id', string='Tarefas solicitadas')





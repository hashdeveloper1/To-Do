from odoo import fields, models, api


class TodoTaskLines(models.Model):
    _name = 'todo.task.lines'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'To-Do Task Lines'
    _order = 'id desc'

    name = fields.Char(string="Task Name", tracking=1)
    task_id = fields.Many2one('todo.task')
    assign_to_id = fields.Many2one('res.partner', required=True, states={'completed': [('readonly', True)], 'in_progress': [('readonly', True)]}, tracking=1)
    time = fields.Float()
    # due_date = fields.Date(required=True, states={'completed': [('readonly', True)], 'in_progress': [('readonly', True)]}, tracking=1)
    state = fields.Selection([
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed')],
        default='new', tracking=1
    )

    def action_in_progress(self):
        for rec in self:
            rec.state = 'in_progress'

    def action_completed(self):
        for rec in self:
            rec.state = 'completed'

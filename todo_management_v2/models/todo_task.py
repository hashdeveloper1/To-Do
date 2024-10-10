from odoo import fields, models, api
from odoo.exceptions import UserError, ValidationError
from odoo.odoo.fields import Datetime, Date



class TodoTask(models.Model):
    _name = 'todo.task'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'To-Do Task'
    _order = 'id desc'
    _rec_name = 'ref'

    ref = fields.Char(compute="_compute_task_name", default='new', tracking=1)
    name = fields.Char(string="Task Name", tracking=1)
    assign_to_id = fields.Many2one('res.partner', required=True, states={'completed': [('readonly', True)], 'in_progress': [('readonly', True)]}, tracking=1)
    due_date = fields.Date(required=True, states={'completed': [('readonly', True)], 'in_progress': [('readonly', True)]}, tracking=1)
    state = fields.Selection([
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('closed', 'Closed')],
        default='new', tracking=1
    )
    # description = fields.Char(states={'completed': [('readonly', True)]})
    description = fields.Text(states={'completed': [('readonly', True)]}, tracking=1)
    estimated_time = fields.Float()
    total_time = fields.Float(compute="_compute_total_time", store=1)
    task_line_ids = fields.One2many('todo.task.lines', 'task_id')
    active = fields.Boolean(default=True)
    is_late = fields.Boolean(default=False)

    def action_in_progress(self):
        for rec in self:
            rec.state = 'in_progress'

    def action_completed(self):
        for rec in self:
            rec.state = 'completed'

    def _compute_task_name(self):
        for rec in self:
            rec.ref = 'Task ' + str(rec.id)

    def action_closed(self):
        for rec in self:
            rec.state = 'closed'

    @api.depends('task_line_ids', 'task_line_ids.time')
    def _compute_total_time(self):
        for rec in self:
            total_time = 0.0
            for line in rec.task_line_ids:
                total_time += line.time
            rec.total_time = total_time
        self._check_total_time()

    @api.depends('task_line_ids', 'task_line_ids.time')
    def _check_total_time(self):
        for rec in self:
            if rec.total_time > rec.estimated_time:
                raise ValidationError('Total time Must to be < Estimated Time')

    def check_expected_due_date(self):
        todo_ids = self.search([])
        for rec in todo_ids:
            datetimev = fields.Datetime.now()
            date = datetimev.date()
            if rec.due_date < date:
                rec.is_late = True
            print("hello", date)

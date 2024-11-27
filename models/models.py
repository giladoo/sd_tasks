# -*- coding: utf-8 -*-
from odoo import models, fields, api, tools, _
from odoo.osv import expression
from odoo.exceptions import  AccessError, UserError

class SdTasksProjectTask(models.Model):
    _inherit = 'project.task'

    readonly_user = fields.Boolean(store=False, default=lambda self: not self.env.user.has_group('base.group_system'))
    invisible_user = fields.Boolean(store=False, default=lambda self: not self.user_ids or self.user_ids and self.env.user.id in self.user_ids.ids)

    def get_my_tasks(self, headers=['name']):
        my_tasks = self.search_read([('user_ids', 'in', self.env.user.id)], headers)
        return my_tasks

    def write(self, vals):
        vals_keys = set(vals.keys()).difference({'state', 'date_last_stage_update' })
        # Users have access to change task state only
        if not self.env.user.has_group('sd_tasks.group_sd_tasks_admins'):
            if len(vals) > 1 or len(vals_keys) > 0 :
                raise AccessError(_(f"You have permission to change 'Task State'\n Please discard form update and try again "))
            state = vals.get('state', False)
            date_last_stage_update = vals.get('date_last_stage_update', False)

            if state and state.find('done') < 0 and state.find('cancel') < 0:
                vals = {'state': state}
            elif date_last_stage_update:
                vals = {'date_last_stage_update': date_last_stage_update}
            else:
                vals = {}

        return super().write(vals)

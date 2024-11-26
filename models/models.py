# -*- coding: utf-8 -*-
import datetime
import json
from datetime import  timedelta
# import random

from odoo import models, fields, api, tools

# from colorama import Fore


class sd_tasks_settings(models.Model):
    _name = 'sd_tasks.settings'
    _description = 'sd_tasks.settings'

    name = fields.Char(required=True, translate=True)


class SdTasksProjectTask(models.Model):
    _inherit = 'project.task'

    readonly_user = fields.Boolean(store=False, default=lambda self: not self.env.user.has_group('base.group_system'))
    # invisible_user = fields.Boolean(store=False, default=True)
    invisible_user = fields.Boolean(store=False, default=lambda self: not self.user_ids or self.user_ids and self.env.user.id in self.user_ids.ids)

    def get_my_tasks(self, headers=['name']):
        my_tasks = self.search_read([('user_ids', 'in', self.env.user.id)], headers)
        print(my_tasks)
        return my_tasks

/** @odoo-module */
import { registry } from "@web/core/registry"
import { useService } from "@web/core/utils/hooks"
import { session } from "@web/session";
import { Component, useState, onMounted, onWillStart,  onWillUnmount } from "@odoo/owl";
export class SdTasksDashboard extends Component{
    setup(){
    this.orm = useService('orm')
    this.state = useState({
        header: ["name", "date_deadline", "user_ids","state"],
//        header: ["name", "state"],
        rows: []
    })
    onWillStart(() => {
        this.getTasks().then(data => {
        console.log(typeof data, data)
//        this.state.rows = JSON.parse(data)
        this.state.rows = data

        console.log(this.state.rows)
        })
    })
    onMounted(() => {
        document.querySelector('.o_action_manager').classList.add('overflow-auto')
    })
    this.clicked = this.clicked.bind(this);

    }
    async getTasks() {
         return await this.orm.call(
                    "project.task",
                    'get_my_tasks',
                    ['', this.state.header]
                );

    }
    clicked(e){
        console.log('onclick:', e)
    }
    }

SdTasksDashboard.template = "sd_tasks.sd_tasks_dashboard"
//ClientApps.components = { ClientCard, ClientNav }

registry.category('actions').add('sd_tasks.sd_tasks_dashboard', SdTasksDashboard)
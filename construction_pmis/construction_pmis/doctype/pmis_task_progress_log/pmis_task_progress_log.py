import frappe
from frappe.model.document import Document
from frappe import _

class PMISTaskProgressLog(Document):
    def on_submit(self):
        self.update_task_progress()

    def update_task_progress(self):
        task = frappe.get_doc("PMIS Task", self.task)
        task.progress_percent = self.current_progress

        if self.current_progress >= 100:
            task.status = "Completed"
            if not task.actual_finish:
                task.actual_finish = self.posting_date
        elif self.current_progress > 0:
            task.status = "In Progress"
            if not task.actual_start:
                task.actual_start = self.posting_date

        task.save()

    def before_insert(self):
        prev_progress = frappe.db.get_value("PMIS Task", self.task, "progress_percent")
        self.previous_progress = prev_progress or 0

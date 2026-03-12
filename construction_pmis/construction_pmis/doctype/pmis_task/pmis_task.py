import frappe
from frappe.model.document import Document
from frappe import _

class PMISTask(Document):
    def validate(self):
        if self.planned_start and self.planned_finish:
            if self.planned_finish < self.planned_start:
                frappe.throw(_("Planned Finish cannot be before Planned Start"))

            # Calculate duration
            delta = frappe.utils.date_diff(self.planned_finish, self.planned_start)
            self.planned_duration = delta + 1

        if self.actual_start and self.actual_finish:
            if self.actual_finish < self.actual_start:
                frappe.throw(_("Actual Finish cannot be before Actual Start"))

            delta = frappe.utils.date_diff(self.actual_finish, self.actual_start)
            self.actual_duration = delta + 1

        if self.progress_percent:
            if self.progress_percent < 0 or self.progress_percent > 100:
                frappe.throw(_("Progress Percent must be between 0 and 100"))

            if self.progress_percent == 100:
                self.status = "Completed"
            elif self.progress_percent > 0:
                self.status = "In Progress"

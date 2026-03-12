import frappe
from frappe.model.document import Document
from frappe import _

class PMISTaskDependency(Document):
    def validate(self):
        if self.task == self.predecessor_task:
            frappe.throw(_("A task cannot depend on itself"))

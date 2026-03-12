import frappe
from frappe import _

def execute(filters=None):
	columns, data = get_columns(), get_data(filters)
	return columns, data

def get_columns():
	return [
		{ "label": _("ID"), "fieldname": "name", "fieldtype": "Link", "options": "PMIS Project", "width": 120 },
		{ "label": _("Project Name"), "fieldname": "project_name", "fieldtype": "Data", "width": 200 },
		{ "label": _("Status"), "fieldname": "status", "fieldtype": "Data", "width": 100 },
		{ "label": _("Contract Value"), "fieldname": "contract_value", "fieldtype": "Currency", "options": "currency", "width": 120 },
		{ "label": _("Start Date"), "fieldname": "planned_start_date", "fieldtype": "Date", "width": 100 },
		{ "label": _("End Date"), "fieldname": "planned_end_date", "fieldtype": "Date", "width": 100 },
		{ "label": _("PM"), "fieldname": "project_manager", "fieldtype": "Link", "options": "User", "width": 120 },
	]

def get_data(filters):
	return frappe.get_all("PMIS Project", fields=["name", "project_name", "status", "contract_value", "planned_start_date", "planned_end_date", "project_manager", "currency"])

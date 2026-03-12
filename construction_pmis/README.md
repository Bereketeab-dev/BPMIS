# Construction PMIS

Project Management Information System for ERPNext v14 and above.

## Features

- **Project Management**: Project setup, team assignments, stakeholder management.
- **Scheduling**: Multi-level tasks, dependencies, and progress tracking.
- **Daily Operations**: Work planning and site logs for manpower, machinery, and material.
- **Commercials**: BOQ, Cost Estimates, Subcontracts, Payment Certificates, and Final Accounts.
- **Technical & Quality**: Document control, as-built drawings, RFI, NCR, Snags, and Inspections.
- **Safety**: Toolbox talks and attendee tracking.
- **Handover**: Commissioning checklists and lessons learned.

## Installation

1. Clone the repository into your bench's `apps` folder:
   ```bash
   cd /path/to/your/bench/apps
   git clone [repository-url] construction_pmis
   ```

2. Install the app on your site:
   ```bash
   bench setup requirements
   bench install-app construction_pmis
   ```

3. Run migrations:
   ```bash
   bench migrate
   ```

## Roles

The app includes the following predefined roles:
- PMIS Administrator
- PMIS Project Manager
- PMIS Planner
- PMIS Site Engineer
- PMIS Quantity Surveyor
- PMIS Document Controller
- PMIS QA/QC Engineer
- PMIS Safety Officer
- PMIS Commercial Manager
- PMIS Viewer

## Business Logic

- **Task Progress**: Updating progress logs automatically updates task status and actual dates.
- **Financials**: Automatic calculation of BOQ amounts, subcontract values, and payment certificate balances.
- **Validation**: Prevents invalid date ranges, circular task dependencies, and incorrect progress percentages.
- **Rebar**: Automatic weight calculation based on bar dimensions and count.

## Reports

Includes 15+ standard reports covering all functional areas of the PMIS.

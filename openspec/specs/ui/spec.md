# ui Specification

## Purpose
TBD - created by archiving change complete-assessment-requirements. Update Purpose after archive.
## Requirements
### Requirement: Task Filtering
The UI SHALL provide a way to filter the displayed tasks based on their completion status.

#### Scenario: Filter by Active
- **WHEN** the user selects the "Active" filter
- **THEN** only tasks where `completed` is false are displayed

#### Scenario: Filter by Completed
- **WHEN** the user selects the "Completed" filter
- **THEN** only tasks where `completed` is true are displayed

#### Scenario: Show All
- **WHEN** the user selects the "All" filter
- **THEN** both completed and active tasks are displayed

### Requirement: Task Editing
The UI SHALL provide a mechanism to edit existing tasks' details.

#### Scenario: Edit Title and Description
- **WHEN** the user chooses to edit a task
- **THEN** the current title and description are pre-filled in editable fields
- **AND** saving the changes updates the persisted task


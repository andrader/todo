## MODIFIED Requirements
### Requirement: Task Filtering
The UI SHALL provide comprehensive filtering capabilities for the task list.

#### Scenario: Filter by Status
- **WHEN** the user selects "Active", "Completed", or "All"
- **THEN** tasks matching the status are displayed

#### Scenario: Filter by Priority
- **WHEN** the user selects a specific priority (e.g., "High")
- **THEN** only tasks with that priority are displayed

#### Scenario: Filter by Category
- **WHEN** the user selects a category
- **THEN** only tasks belonging to that category are displayed

#### Scenario: Search
- **WHEN** the user types a search query
- **THEN** only tasks matching the query in title or description are displayed

### Requirement: Task Editing
The UI SHALL provide a mechanism to edit existing tasks' details.

#### Scenario: Edit Task Details
- **WHEN** the user chooses to edit a task
- **THEN** the form allows modifying title, description, due date, priority, and category
- **AND** saving the changes updates the persisted task

## ADDED Requirements
### Requirement: Quick Add
The UI SHALL provide a quick entry mechanism using natural language.

#### Scenario: Smart Entry
- **WHEN** the user types a command-like task (e.g., "Call mom tomorrow !high") into the Quick Add field
- **THEN** the task is created with the correct title ("Call mom"), due date (tomorrow's date), and priority (High)


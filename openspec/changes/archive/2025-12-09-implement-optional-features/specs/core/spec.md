## MODIFIED Requirements
### Requirement: Todo Management
The system SHALL provide capabilities to manage Todo items with rich metadata.

#### Scenario: Create a new Todo
- **WHEN** a user submits a task with a title and optional details (description, due date, priority, category)
- **THEN** the task is persisted with all provided attributes
- **AND** `completed` is set to false by default

#### Scenario: List Todos
- **WHEN** the user requests to see the list
- **THEN** all persisted Todo items are returned containing their metadata (due date, priority, category)

#### Scenario: Complete a Todo
- **WHEN** a user marks a Todo as done
- **THEN** the Todo's status is updated to completed and persisted

#### Scenario: Delete a Todo
- **WHEN** a user deletes a Todo
- **THEN** the Todo item is removed from persistence

## ADDED Requirements
### Requirement: Natural Language Parsing
The system SHALL be able to interpret natural language strings to populate task attributes.

#### Scenario: Parse due date
- **WHEN** the input contains time-relative terms (e.g., "tomorrow", "next friday")
- **THEN** the `due_date` field is calculated and set

#### Scenario: Parse priority
- **WHEN** the input contains priority keywords (e.g., "!high", "priority:low")
- **THEN** the `priority` field is set accordingly


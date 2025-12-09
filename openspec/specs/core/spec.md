# core Specification

## Purpose
TBD - created by archiving change init-todo-project. Update Purpose after archive.
## Requirements
### Requirement: Todo Management
The system SHALL provide capabilities to manage Todo items.

#### Scenario: Create a new Todo
- **WHEN** a user submits a title and optional description
- **THEN** a new Todo item is persisted with a unique ID and `completed` set to false

#### Scenario: List Todos
- **WHEN** the user requests to see the list
- **THEN** all persisted Todo items are returned

#### Scenario: Complete a Todo
- **WHEN** a user marks a Todo as done
- **THEN** the Todo's status is updated to completed and persisted

#### Scenario: Delete a Todo
- **WHEN** a user deletes a Todo
- **THEN** the Todo item is removed from persistence


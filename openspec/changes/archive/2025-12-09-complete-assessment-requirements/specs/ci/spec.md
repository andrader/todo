## ADDED Requirements

### Requirement: Continuous Integration
The project SHALL have a CI pipeline to ensure code quality and stability.

#### Scenario: Automated Testing
- **WHEN** code is pushed to the repository or a Pull Request is opened
- **THEN** the CI system runs the test suite
- **AND** the pipeline fails if any tests fail

#### Scenario: Automated Linting
- **WHEN** code is pushed
- **THEN** the CI system runs linting tools
- **AND** the pipeline fails if linting errors are found

#### Scenario: Ubuntu Environment
- **WHEN** the CI pipeline runs
- **THEN** it executes on an Ubuntu runner as required by the assessment


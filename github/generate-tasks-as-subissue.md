---
description:
globs:
alwaysApply: false
---

# Rule: Generating a github sub-issue for each task List from a PRD

## Goal

To guide an AI assistant in creating a detailed, step-by-step github sub-issue for task list in Markdown format based on an existing Product Requirements Document (PRD). The task list should guide a developer through implementation.

## Output

- **Format:** Markdown (`.md`)
- **Output:** Github sub-issue

## Process

1.  **Receive PRD Reference:** The user points the AI to a specific github issue containg the PRD description. The AI reads the issue with all the comments and jump the the correct Phase.
2.  **Phase 1: Analyze PRD:** The AI reads and analyzes the functional requirements, user stories, and other sections of the specified PRD.
3.  **Phase 1: Comment the Github issue with a list of Parent Tasks:** Based on the PRD analysis, comment the issue with the main, high-level tasks required to implement the feature. Use your judgement on how many high-level tasks to use. Do not exceed with tasks. It's likely to be between 1 and 3. The number of tasks depends on the best effort to reduce the number relevant files needed to build the task. Present these tasks to the user in the specified format (without sub-tasks yet). Inform the user: "I have generated the high-level tasks based on the PRD. Ready to generate the sub-tasks? Respond with 'Go' to proceed."
4.  **Wait for Confirmation:** Pause and wait for the user to respond with "Go".
5.  **Phase 2: Generate Sub-Tasks:** Once the user confirms, break down each parent task into smaller, actionable sub-tasks necessary to complete the parent task. Ensure sub-tasks logically follow from the parent task and cover the implementation details implied by the PRD.
6.  **Phase 2: Identify Relevant Files:** Based on the tasks and PRD, identify potential files that will need to be created or modified. List these under the `Relevant Files` section, including corresponding test files if applicable.
7.  **Phase 2: Generate Github Sub-Tasks** For each parent tasks, its sub-tasks, its relevant files, and its notes create a sub-issue in Markdown structure. Create subtask with name `[issue]-task-[task-number] where `[issue]` in the parent issue name and `[task-number]` is the task index.
8.  **Phase 2: Final Comment to github Issue:** Create a comment to the parent issue with the list of created task and links to the created sub-tasks.

## Output Format

The generated task list _must_ follow this structure:

```markdown
## Relevant Files

- `path/to/potential/file1.ts` - Brief description of why this file is relevant (e.g., Contains the main component for this feature).
- `path/to/file1.test.ts` - Unit tests for `file1.ts`.
- `path/to/another/file.tsx` - Brief description (e.g., API route handler for data submission).
- `path/to/another/file.test.tsx` - Unit tests for `another/file.tsx`.
- `lib/utils/helpers.ts` - Brief description (e.g., Utility functions needed for calculations).
- `lib/utils/helpers.test.ts` - Unit tests for `helpers.ts`.

### Notes

- Unit tests should typically be placed in the folder /tests preservating the same structure of the ./src file (e.g., `./src/ComponentA/MyComponent.tsx` and `./tests/ComponentA/MyComponent.test.tsx` ).
- Use `npx vitest [optional/path/to/test/file]` to run tests. Running without a path executes all tests found by the Vitest configuration.

## Tasks

- [ ] 1.0 Parent Task Title
  - [ ] 1.1 [Sub-task description 1.1]
  - [ ] 1.2 [Sub-task description 1.2]
- [ ] 2.0 Parent Task Title
  - [ ] 2.1 [Sub-task description 2.1]
- [ ] 3.0 Parent Task Title (may not require sub-tasks if purely structural or configuration)
```

## Interaction Model

The process explicitly requires a pause after generating parent tasks to get user confirmation ("Go") before proceeding to generate the detailed sub-tasks. This ensures the high-level plan aligns with user expectations before diving into details.

## Target Audience

Assume the primary reader of the task list is a **junior developer** who will implement the feature.

# Task List Management

Guidelines for managing github subissue in markdown files to track progress on completing a PRD on parent github issue

## Task Implementation
- **Read Github Sub Issue and parent:** The user points the AI to a specific github sub-issue containg tasks to implement a PRD defined in the parent issue. The AI reads the subissue with all the comments, the parent issue for understanding and jumps the the completion protocol.
- **One sub-task at a time:** Do **NOT** start the next sub‑task until you ask the user for permission and they say "yes" or "y"
- **Completion protocol:**  
  1. When you finish a **sub‑task**, immediately add a comment on the Github Sub Issue to inform the uset that subtask is done "I have completed the subtask [X]" where X is the task done index.
  2. When **all** subtasks of the github subissues has been completed, follow this sequence:
    a. **First**: Run the full test suite (`pytest`, `npm test`, `bin/rails test`, etc.)
    b. **Only if all tests pass**: Stage changes (`git add .`)
    c. **Clean up**: Remove any temporary files and temporary code before committing
    d. **Commit**: Use a descriptive commit message that:
      - Uses conventional commit format (`feat:`, `fix:`, `refactor:`, etc.)
      - Summarizes what was accomplished in the parent task
      - Lists key changes and additions
      - References the task number and PRD context
      - **Formats the message as a single-line command using `-m` flags**, e.g.:

        ```
        git commit -m "feat: add payment validation logic" -m "- Validates card type and expiry" -m "- Adds unit tests for edge cases" -m "Related to T123 in PRD"
        ```
  3. Once all the subtasks are marked completed and changes have been committed, add a comment to the sub issue with a summary of what you have done and mark sub issue as completed.
  4.  **CLOSE the Sub Issue** when all sub taks have been completed.

## Task List Maintenance

1. **Update the task list as you work:**
   - Comment github Sub Issue when subtasks as completed per the protocol above.
   - Add new tasks as they emerge.

2. **Maintain the "Relevant Files" section:**
   - List every file created or modified.
   - Give each file a one‑line description of its purpose.

## AI Instructions

When working with task lists, the AI must:

1. Regularly update the task list file after finishing any significant work.
2. Strictly follow the **completion protocol**:
   - Add comment to sub issue each finished **sub‑task**.
   - Add final comment with sub tasks description once **all** subtasks are DONE.
   - Commit the work done.
   - Close the sub-issue when **all** sub tasks are completed.
4. Add newly discovered tasks.
5. Keep "Relevant Files" accurate and up to date.
6. Before starting work, check which sub‑task is next.

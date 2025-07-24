# Rule: Generating a Product Requirements Document for a Github issue

## Goal

To guide an AI assistant in creating a detailed Product Requirements Document (PRD) in Markdown format from a git hub issue based on an initial description. The assistance controls the progress of the github issues by reviewing the entire conversation.

## Process

1.  **Assess the issue status:** Read the full github conversation to understand the correct issue status. Log the status and jump to the right process point. 
2.  **Status**: STARTED
    2.1  **Receive Initial Prompt:** The user provides the github issue number for a new feature or functionality.
    2.2  **Check and Validate issue:** Before moving to the other point, check and verify that the issue is readible
2.  **Status**: ASK_CLARIFICATION
    2.1  **Add github comment for Clarifying Questions:** Before writing the PRD, the AI _must_ add a comment to the github issue with clarifying questions to gather sufficient detail. The goal is to understand the "what" and "why" of the feature, not necessarily the "how" (which the developer will figure out). Make sure to provide options in letter/number lists so I can respond easily with my selections.
3.  **Status**: CREATE_PRD
    3.1  **Generate PRD:** Based on the issue conversation, contrainsts and the user's answers to the clarifying questions, generate a PRD using the structure outlined below. Use components and functionalities already implemented in the folder "./src" as much as possible.
    3.2  **Save PRD:** Add a comment to the issue with the generated document.
    3.3  **Ask Confirmation**: Ask confirmation to the issue's owner to accept or modify PRD 
4.  **Status**: REVIEW_PRD
    4.1 Ask user to provide modifications
    4.2 Read the conversation and the user suggestions and rewrite the PRD
5.  **Status**: CONFIRM_PRD
    5.1 Read the conversation and the user suggestions and rewrite the PRD
6.  **Status**: COMPLETED
    6.1 You have completed your goal. Exit. 

## Constraints

1. Reuse Vue components saved in folder ./src/components
2. Use i18n for different languages. language file in the folder "./src/i18n/"
3. Add new components to ./src/component/{component_name}
4. Split is smaller component to keep file size smller
5. Be creative in designing FE interface,
6. Data is loaded from API calls
7. API call are mocked for simplicity
8. Use stores definined under ./src/stores
9. Reuse all components and functionalities already implemented in the folder "./src"

## Clarifying Questions (Examples)

The AI should adapt its questions based on the prompt, but here are some common areas to explore:

- **Problem/Goal:** "What problem does this feature solve for the user?" or "What is the main goal we want to achieve with this feature?"
- **Target User:** "Who is the primary user of this feature?"
- **Core Functionality:** "Can you describe the key actions a user should be able to perform with this feature?"
- **User Stories:** "Could you provide a few user stories? (e.g., As a [type of user], I want to [perform an action] so that [benefit].)"
- **Technical Requirements:** "How I have to develop this feature?"
- **Acceptance Criteria:** "How will we know when this feature is successfully implemented? What are the key success criteria?"
- **Scope/Boundaries:** "Are there any specific things this feature _should not_ do (non-goals)?"
- **Data Requirements:** "What kind of data does this feature need to display or manipulate?"
- **Design/UI:** "Are there any existing design mockups or UI guidelines to follow?" or "Can you describe the desired look and feel?"
- **Edge Cases:** "Are there any potential edge cases or error conditions we should consider?"

## PRD Structure

The generated PRD should include the following sections:

1.  **Introduction/Overview:** Briefly describe the feature and the problem it solves. State the goal.
2.  **Goals:** List the specific, measurable objectives for this feature.
3.  **User Stories:** Detail the user narratives describing feature usage and benefits.
4.  **Functional Requirements:** List the specific functionalities the feature must have. Use clear, concise language (e.g., "The system must allow users to upload a profile picture."). Number these requirements.
5.  **Non-Goals (Out of Scope):** Clearly state what this feature will _not_ include to manage scope.
6.  **Design Considerations (Optional):** Link to mockups, describe UI/UX requirements, or mention relevant components/styles if applicable.
7.  **Technical Considerations (Optional):** Mention any known technical constraints, dependencies, or suggestions (e.g., "Should integrate with the existing Auth module").
8.  **Success Metrics:** How will the success of this feature be measured? (e.g., "Increase user engagement by 10%", "Reduce support tickets related to X").
9.  **Open Questions:** List any remaining questions or areas needing further clarification.

## Target Audience

Assume the primary reader of the PRD is a **junior developer**. Therefore, requirements should be explicit, unambiguous, and avoid jargon where possible. Provide enough detail for them to understand the feature's purpose and core logic.

## Final instructions

1. Do NOT start implementing the PRD
2. Make sure to ask the user clarifying questions
3. Take the user's answers to the clarifying questions and improve the PRD

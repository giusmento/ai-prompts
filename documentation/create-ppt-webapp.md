# Rule: Generating a Powerpoint structure for web applications

## Goal

To guide an AI assistant in creating a detailed Powerpoint structure for web applications in Markdown format, based on an initial user prompt. The docuemnt should be clear, actionable, and suitable for a business consultant to understand and impprepare the powerpoint.

## Process

1.  **Receive Initial Prompt:** The user provides a brief description of the application and the functionality.
2.  **Ask Clarifying Questions:** Before writing the document, the AI _must_ ask clarifying questions to gather sufficient detail to complete the Document Structure. The goal is to understand the "what" and "why" of the feature, not necessarily the "how" (which the developer will figure out). Make sure to provide options in letter/number lists so I can respond easily with my selections.
3.  **Propone suggestions:** Before writing the document structure, the AI _must_ ask suggestions to improve the document structure. Propose what is relevant. Make sure to provide options in letter/number lists so I can respond easily with my selections.
4.  **Generate document Structure:** Based on the initial prompt and the user's answers to the clarifying questions, generate a PRD using the structure outlined below.
5.  **Save document Structure:** Save the generated document as `ppt-structure.md` inside the `/tmp` directory.

## Clarifying Questions (Examples)

The AI should adapt its questions based on the prompt, but here are some common areas to explore:

- **Problem/Goal:** "What problem does this feature solve for the user?" or "What is the main goal we want to achieve with this feature?"
- **Application Architecture:** "Which type of application are you building?"
- **Core Functionality:** "Can you describe the key actions a user should be able to perform with this feature?"
- **User Stories:** "Could you provide a few user stories? (e.g., As a [type of user], I want to [perform an action] so that [benefit].)"
- **Technical Requirements:** "How I have to develop this feature?"
- **Authentication method:** "how users and admins login?"
- **Design/UI:** "Are there any existing design mockups or UI guidelines to follow?" or "Can you describe the desired look and feel?"

## Document Structure

The generated PRD should include the following sections:

1.  **Introduction/Overview:** Describe of the application. State the goal.
2.  **Application architecture:** Show the application architecture.
3.  **Main entities:** Detail the users such end-users/admins/partners entities. Describe the entity type with feature usage and benefits.
4.  **Dictinary:** Describe naming convention for entities.
5.  **Entity Onboarding process:** Specify the onboarding process for all entities.
6.  **Welcome page:** Describe the landing page with the main feature and prepare the slide to host a screenshot.
7.  **Admin dashboard:** Describe the admin dashboard, with screenshots and UI description
8.  **User dashboard:** Describe the user dashboard, with screenshots and UI description
9.  **Test Taking:** Describe the test Taking, test structure, question types, allow space for screenshots and UI description

Each above point is one or more slides.

## Target Audience

Assume the primary reader of the Docuemnt is a **company directors**. Therefore, requirements should be explicit, unambiguous, and avoid jargon where possible. Provide enough detail for them to understand the feature's purpose and core logic.

## Output

- **Format:** Markdown (`.md`)
- **Location:** `/docs/`
- **Filename:** `ppt-web-app.md`

## Final instructions

1. Do NOT start implementing the PRD
2. Make sure to ask the user clarifying questions
3. Take the user's answers to the clarifying questions and improve the PRD

# Rule: Generating a Data Dictionary

# Goal

To guide an AI assistant in creating a detailed, step-by-step data dictionary in Markdown format. The docuemnt should guide the business person to understand domain-specific naming conventions.

## Output

- **Format:** Markdown (`.md`)
- **Location:** `/docs/data-dictionary`
- **Filename:** `data-dictionary-Vx.md` (e.g., `data-dictionary-V1.md`)

## Process

1.  **Ask Document Questions:** Before writing the document, the AI _must_ ask clarifying questions to gather sufficient detail. The goal is to understand which part of the application must be taken into consideration, the "what" and "how" write the document. Make sure to provide options in letter/number lists so I can respond easily with my selections.
2.  **Generate document:** Based on the user's answers to the Document questions, generate a document using the structure outlined below.
3.  **Save PRD:** Save the generated document as `data-dictionary-vx.md` inside the `/docs/data-dictionary` directory. Where X is an incremental version of the document. old versions are in the same folder `/docs/data-dictionary`

## Document Questions (Examples)

The AI should adapt its questions based on the prompt, but here are some common areas to explore:

- **Feature in scope:** "Which main areas of application should be included in the document: A. Only types defined in the folder `./types`, B. All types and UI interfaces"

## PRD Structure

The generated PRD should include the following sections:

1.  **Introduction/Overview:** Briefly describe the document. "what is", State the goal.
2.  **Goals:** List the specific inspected areas.
3.  **Data dictionary:** Detail the dictionary as a table of columns: 1. name, 2.description, 2. data structure, 3. example.
4.  **Possible errors and warning:** List as a table possible errors in the data dictionary, describe the issue and rate the error, High, low, medium. Suggest modifications
5.  **Suggestions:** List any improvements to the data dictionary.

## Target Audience

Assume the primary reader of the Docuemnt is a **business person**. Therefore, language should be explicit, unambiguous, and avoid jargon where possible.

## Final instructions

1. Do NOT start implementing the Document
2. Make sure to ask docuemnt questions
3. Take the user's answers to the clarifying questions and improve the Document

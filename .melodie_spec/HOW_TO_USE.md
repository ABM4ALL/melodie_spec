# How to Use Melodie Spec Kit

This kit helps AI Coding Agents (Cursor, Claude, etc.) generate high-quality Agent-Based Models using the [Melodie](https://github.com/ABM4ALL/Melodie) framework.

## Step 0: Prerequisites

Before using the AI, please complete the following prerequisites:

1.  **Install Melodie**:

    ```bash
    pip install Melodie
    ```

2.  **Prepare Story**: Write your model's motivation/story in `README.md` in the root directory.

    > **💡 Story Tips**:
    > While the AI can infer a design from any text, including these details helps it get it right the first time:
    > *   **Goal**: What problem is being solved?
    > *   **Agents**: Who are the actors? (e.g., Wolves, Sheep)
    > *   **Space**: Grid? Network? None?
    > *   **Mode**: Need Calibration (fitting data) or Training (RL)?
    >
    > *Don't worry if you miss something, the AI will make reasonable assumptions to generate `DESIGN.md`.*

---

## Step 1: Design Phase

**Goal**: Turn your "Story" into a technical "Design Document".

**Action**: Open your AI Agent and copy/paste this prompt. Make sure to explicitly **@** the files so the AI reads them:

> "Please help me design a Melodie ABM based on my @README.md story. Use the **Design Template** provided in @.melodie_spec/SYSTEM_PROMPT.md to create a `DESIGN.md` file in the project root directory."

**Review**: Check the generated `DESIGN.md`. If needed, edit your `README.md` and regenerate, or edit `DESIGN.md` directly.

---

## Step 2: Implementation Phase

**Goal**: Turn your "Design Document" into code.

**Action**: Start a new chat session and copy/paste this prompt. Make sure to explicitly **@** the files so the AI reads them:

> "Using @.melodie_spec/SYSTEM_PROMPT.md as the technical guide, read the approved @DESIGN.md. Generate the full project code (core modules, data files, and main.py) in the project root directory by adapting the templates found in the `@.melodie_spec/templates/` directory. If the generated code is incorrect or fails to run, please analyze the error, update DESIGN.md if necessary, and regenerate the code until it runs successfully."

**Verify**: Run the model and check results *(saved to `data/output/`)*:

```bash
python main.py
```



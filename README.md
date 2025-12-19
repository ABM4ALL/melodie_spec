# How to Use Melodie Spec Kit

This kit helps AI Coding Agents (Cursor, Claude, etc.) generate high-quality Agent-Based Models using the [Melodie](https://github.com/ABM4ALL/Melodie) framework.

## Step 0: Prerequisites

1.  **Install Melodie**:
    ```bash
    pip install Melodie
    ```

2.  **Prepare Story**: Create a `STORY.md` file in the root directory and write your model's motivation/story in it.

    > **💡 Story Tips**:
    > *   **Goal**: What problem is being solved?
    > *   **Agents**: Who are the actors? (e.g., Wolves, Sheep)
    > *   **Space**: Grid? Network? None?
    > *   **Mode**: Need Calibration (fitting data) or Training (RL)?
    >
    > **Note**: The story doesn't need to be perfect. The AI will make reasonable assumptions to fill in the gaps in `DESIGN.md`, which you can then refine and edit.

## Step 1: Design Phase (The Architect)

**Goal**: Turn your "Story" into a technical "Design Document".

**Action**: Open your AI Agent and copy/paste this prompt:

> Please help me design a Melodie ABM based on my @STORY.md story. Read **@.melodie_spec/prompts/PHASE_1_DESIGN.md** instructions to create a `DESIGN.md` file in the project root directory.

**Review**: Check the generated `DESIGN.md`. All requirements should be captured here.

## Step 2: Implementation Phase (The Engineer)

**Goal**: Turn your "Design Document" into code.

**Action**: Start a new chat session (recommended) and copy/paste this prompt:

> I have an approved design in @DESIGN.md. Please act as the Engineer. Read **@.melodie_spec/prompts/PHASE_2_CODE.md** and the templates in **@.melodie_spec/templates/**. Generate the full project code (core modules, main.py, data) based on the Design.

**Verify**: Run the model and check results:

```bash
python main.py
```

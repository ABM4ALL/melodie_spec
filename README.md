# How to Use Melodie Spec Kit

This kit helps AI Coding Agents (Cursor, Claude, etc.) generate high-quality Agent-Based Models using the [Melodie](https://github.com/ABM4ALL/Melodie) framework.

**Usage Recommendation**: 

- You can fork this repository to your GitHub account and set it as a **Template Repository**. 
- Whenever you want to build a new ABM model, simply create a new repository using this template.

Follow these three steps to use `melodie_spec`:

## Step 0: Prerequisites

1.  **Install Melodie**:
    ```bash
    pip install Melodie MelodieStudio
    ```

2.  **Prepare Story**: Create a `STORY.md` file in the root directory and write your model's motivation/story in it.

    > **Story Tips**:
    > *   **Goal**: What system do you want to study? Any specific research question?
    > *   **Agents**: Who are the actors (e.g., Wolves, Sheep)? What do they do? How do they interact?
    > *   **Space**: Are there specific types of space (e.g., Grid, Network, None)?
    > *   **Mode**: Need Calibration (fitting data) or Training (evolutionary reinforcement training)?
    
    **💡 Note**: 
    
    - The story doesn't need to be perfect. The AI will make reasonable assumptions to fill in the gaps in `DESIGN.md`, which you can then refine and edit.
    - The core value of `melodie_spec` is teaching the AI Agent how to use Melodie. Therefore, if you also have a deeper understanding of the framework, you can collaborate much more effectively—especially when refining `DESIGN.md`. We strongly recommend you explore the Melodie [documentation](https://abm4all.github.io/Melodie/html/index.html) and [examples](https://github.com/ABM4ALL/Melodie/tree/master/examples) to learn the ropes!

## Step 1: Design Phase (The Architect)

**Goal**: Turn your "Story" into a technical "Design Document".

**Action**: Open your AI Agent and copy/paste this prompt (⚠️ **IMPORTANT**: Ensure you **drag & drop** or **reference** the mentioned files so the AI can read them):

> Please help me design a Melodie ABM based on my @STORY.md story. Read **@.melodie_spec/prompts/PHASE_1_DESIGN.md** instructions to create a `DESIGN.md` file in the project root directory.

**Review**: Check the generated `DESIGN.md`. All requirements should be captured here.

## Step 2: Implementation Phase (The Engineer)

**Goal**: Turn your "Design Document" into code.

**Action**: Start a new chat session (recommended) and copy/paste this prompt (⚠️ **IMPORTANT**: Ensure you **drag & drop** or **reference** the mentioned files):

> I have an approved design in @DESIGN.md. Please act as the Engineer. Read **@.melodie_spec/prompts/PHASE_2_CODE.md** and the templates in **@.melodie_spec/templates/**. Generate the full project code (core modules, main.py, data) based on the Design in the project root directory.

**Verify**: Run the model and check results:

```bash
python main.py
```

## Philosophy

`melodie_spec` is designed to streamline the **bootstrap phase** of model development. Our goal is to save your mental energy for what truly matters: the **Story**. Thinking through motivations, defining model boundaries, and abstracting core logic—this is the heart of research.

The Melodie framework and this `melodie_spec` kit function as a set of **"structural prompts."** Empowered by modern LLMs and AI IDEs, starting an ABM project has never been easier.

**However, a critical reminder:**
Once `melodie_spec` generates the first runnable version, the baton passes to you. You must carefully review, understand, and own every line of code and data detail. You must be able to verify and explain the model's results independently. As your project evolves into deeper modifications and complex iterations, the automated assistance from `melodie_spec` will naturally diminish, and your domain expertise must take over.

## Contribution

The continuous improvement of `melodie_spec` relies on community feedback and iterative refinement of the prompts in `.melodie_spec`.

-   **Development**: We encourage you to fork this repository and build your models directly within it (e.g., using different branches for different models).
-   **Refinement**: If you encounter issues with the generated Design or Code, please try to fix the root cause by modifying the prompts or templates in `.melodie_spec`.
-   **Pull Requests**: Please merge your improvements into a dedicated branch and submit a **Pull Request** to the original [melodie_spec](https://github.com/ABM4ALL/melodie_spec) repository.
-   **Issues**: Alternatively, share your experiences in the **Issues** section. Providing a link to your model's repository and describing specifically what went wrong (Design vs. Code) effectively helps us improve the kit.

We look forward to your contributions!


test
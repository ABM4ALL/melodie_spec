# Melodie Spec Kit

This is a **Spec Kit** designed to help AI Coding Agents (like Cursor, Claude Code, etc.) generate high-quality Agent-Based Models (ABM) using the [Melodie](https://github.com/ABM4ALL/Melodie) framework.

## How to Use

This kit works with any AI Coding Assistant (Cursor, Claude, Windsurf, etc.) by simply providing the right files as context.

### Phase 1: Design
**Goal**: Turn your "Story" into a technical "Design Document".

#### 💡 Tips for your Story (`README.md`)
While the AI will try to infer a design from *any* story, including the following details helps it generate a perfect `DESIGN.md` on the first try:
-   **Goal**: What is the simulation trying to solve? (e.g., "Minimize infection rates")
-   **Agents**: What entities exist? (e.g., "Citizens and Doctors")
-   **Space**: Do they move on a **Grid**, a **Network**, or neither?
-   **Modes**: Do you need a **Calibrator** (to fit real data) or a **Trainer** (RL for agents)?

1.  **Preparation**:
    -   Write your model's story/motivation in your project's `README.md`.
2.  **Action**:
    -   Open your AI chat.
    -   **Goal**: Turn your story into a structured design document.
    -   **Context**:
    - Copy the prompts from `.melodie_spec/SYSTEM_PROMPT.md`. (The AI Expert & Template)
        - `README.md` (Your Story)
    -   **Prompt**:
        > "Please help me design a Melodie ABM based on my @README.md story. Use the **Design Template** provided in @.melodie_spec/SYSTEM_PROMPT.md to create a `DESIGN.md` file in the project root directory."

3.  **Result**: Review the generated `DESIGN.md`.
    -   *Option A*: Edit `DESIGN.md` explicitly.
    -   *Option B*: Update your story in `README.md` and run the prompt again to regenerate the design.

### Phase 2: Implementation
**Goal**: Turn your "Design Document" into code.

1.  **Action**:
    -   Open your AI chat (new session recommended).
    -   **Copy & Paste** the following prompt:

    > **Prompt**:
    > "Using @.melodie_spec/SYSTEM_PROMPT.md as the technical guide, read the approved @DESIGN.md. Generate the full project code (core modules, data files, and main.py) in the project root directory by adapting the templates found in the `@.melodie_spec/templates/` directory. If the generated code is incorrect or fails to run, please analyze the error, update DESIGN.md if necessary, and regenerate the code until it runs successfully."

2.  **Iterate**: If the code needs changes, edit `DESIGN.md` and run the Phase 2 prompt again.
    -   *Option A*: Edit `DESIGN.md` explicitly.
    -   *Option B*: Update your story in `README.md` and run the prompt again to regenerate the design, then to regenerate the project code.

### Phase 3: Verify & Run

1.  **Install Melodie**: Ensure you have `Melodie` installed (`pip install Melodie`).
2.  **Run**: Execute `python main.py`.
3.  **Check Output**: Results (CSV) will be in `data/output/`.

---

## Developer Notes & Best Practices

If you are modifying the generated code or templates, keep these in mind:

1.  **Output Generation**:
    -   The `Model.run()` method **must** call `self.data_collector.save()` at the end of the simulation loop, otherwise no data will be written.
    -   Check `main.py` Config: `data_output_type` should be `"csv"` (default) or `"sqlite"`.

2.  **Class Naming**:
    -   The AI should rename generic classes (`TemplateModel`) to your domain names (`WealthModel`). If it forgets, you can rename them manually or update `main.py` imports.

3.  **Path Handling**:
    -   `main.py` uses `os.path.dirname(__file__)` to correctly locate `data/` folder regardless of where you run the command from.

4.  **Data Collector**:
    -   To collect data, you must add properties in `DataCollector.setup()`:
        ```python
        self.add_agent_property("agent_list", "money")
        self.add_environment_property("gini_coefficient")
        ```
    -   Ensure these properties actually exist on your Agent/Environment.

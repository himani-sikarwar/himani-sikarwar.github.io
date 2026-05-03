# GitHub Copilot instructions

## Workspace overview
- This repository currently contains only a `LICENSE` file and no application or website source files.
- The default branch is `develop`.
- There are no detected build, test, or deploy scripts in this workspace.

## What Copilot should know
- Treat this as a GitHub Pages / static site repository that is currently not implemented.
- When asked to add content, scaffold the site using simple static assets unless the user specifies a framework such as Jekyll, Hugo, React, or another static site generator.
- Keep changes minimal and explicit; do not add features or frameworks without user approval.

## Recommended behavior
- Ask clarifying questions before creating website content, templates, or build infrastructure.
- Preserve the repository's current simplicity and avoid introducing assumptions about tooling.
- If the user wants a static site, suggest the smallest viable structure: `index.html`, `styles.css`, and asset folders.
- If the user wants a blog or portfolio, ask whether they prefer plain HTML/CSS or a site generator.

## Example requests
- "Create a basic GitHub Pages homepage with an about section and contact links."
- "Add a minimal site structure for a personal portfolio." 
- "Help me turn this repository into a static website using plain HTML and CSS."
- "Suggest a GitHub Pages site structure for a developer portfolio."

## Next customization suggestions
- Create an `AGENTS.md` or expand `.github/copilot-instructions.md` once the repository has source files or a framework.
- Add a project-specific prompt file when the site structure is defined.
- Create a dedicated instruction set for `docs/`, `src/`, or `assets/` if the repository becomes more complex.

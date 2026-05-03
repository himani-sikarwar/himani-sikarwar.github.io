# GitHub Copilot instructions

## Workspace overview
- This is a Jekyll-based static site repository using the AcademicPages template for academic and professional portfolio websites.
- Built on the Minimal Mistakes theme with collections for publications, talks, portfolio, teaching, and blog posts.
- Default branch is `develop`; deployment via GitHub Pages.
- Includes automated content generation tools (Python/Jupyter) for bulk importing publications and talks.

## What Copilot should know
- **Framework**: Jekyll static site generator with Ruby dependencies (Gemfile) and optional npm for asset minification.
- **Content Model**: Collections-based (_posts, _publications, _talks, _portfolio, _teaching) with specific frontmatter schemas.
- **Build Process**: `bundle install` → `jekyll serve` for local dev; automatic GitHub Pages deployment.
- **Automation**: markdown_generator/ provides TSV/BibTeX → Markdown conversion tools.
- **Configuration**: Dual configs (_config.yml for production, _config_docker.yml for local Docker).

## Build & Test Commands
- **Install dependencies**: `bundle install` (Ruby gems) and `npm install` (JS assets)
- **Local development**: `bundle exec jekyll serve` (auto-reloads except _config.yml)
- **Docker alternative**: `docker-compose up` (handles all dependencies)
- **Build assets**: `npm run build:js` (minifies JavaScript)
- **Test**: No built-in tests; use `htmlproofer` for link checking if installed

## Architecture Decisions
- **Collections over pages**: Content organized in Jekyll collections for better organization and templating.
- **Frontmatter schemas**: Publications require extended fields (venue, paperurl, citation); talks use location data.
- **Navigation**: Manual via _data/navigation.yml (not auto-generated).
- **Themes**: Minimal Mistakes with custom SCSS; selectable via site_theme config.
- **Automation**: GitHub Actions for talk location scraping; Python tools for content bulk import.

## Project Conventions
- **File naming**: YYYY-MM-DD-title.md for date-based sorting.
- **Frontmatter**: Required for all content; collection-specific fields vary.
- **Assets**: Place in assets/ or files/; auto-copied to _site/.
- **Data**: Use _data/ for YAML/JSON that powers site elements.
- **Layouts**: Custom in _layouts/; includes in _includes/ for reusable components.

## Potential Pitfalls
- **Config changes**: Restart Jekyll serve after editing _config.yml (no auto-reload).
- **Baseurl**: Must be empty for username.github.io root deployment.
- **Collection registration**: Inactive collections in _config.yml won't render.
- **Asset caching**: Clear .jekyll-cache if changes don't appear.
- **Ruby versions**: Ensure compatible Ruby/Bundler; use Docker to avoid issues.
- **Content ordering**: Malformed dates break archive sorting.

## Recommended Behavior
- **Content editing**: Use existing collection structures; suggest frontmatter generators for bulk content.
- **New features**: Prefer Jekyll plugins over custom code; ask before adding frameworks.
- **Local testing**: Recommend Docker for consistent environments.
- **Deployment**: Guide users to GitHub Pages settings; explain baseurl requirements.
- **Automation**: Point to markdown_generator/ for bulk imports; explain TSV/BibTeX workflows.

## Example Requests
- "Add a new publication to _publications/ with proper frontmatter"
- "Generate Markdown files from my publications TSV using the Python script"
- "Update the site theme or navigation menu"
- "Help set up local development with Jekyll serve"
- "Add a new page to the portfolio collection"

## ApplyTo-Specific Instructions
- **Content Generation**: For markdown_generator/ directory - prioritize Python/Jupyter automation tools; explain TSV input formats and output frontmatter.
- **Configuration**: For _config.yml and _config_docker.yml - highlight baseurl, collection settings, and theme options.
- **Templates**: For _layouts/ and _includes/ - maintain Minimal Mistakes compatibility; suggest Liquid templating best practices.

## Next Customization Suggestions
- Create a content-editing agent for bulk frontmatter generation and collection management.
- Add a deployment agent for GitHub Pages setup and baseurl configuration.
- Expand with a documentation agent for README updates and contributor guides.

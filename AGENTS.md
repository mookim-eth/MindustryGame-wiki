# Repository Guidelines

## Project Structure & Module Organization
This repository contains the hand-authored source for the Mindustry wiki. Markdown pages live in `docs/`, grouped by topic such as `docs/logic/` and `docs/modding/`. Static assets are stored under `docs/images/`, and custom CSS is in `docs/stylesheets/style.css`. MkDocs configuration is in `mkdocs.yml`; theme overrides are in `overrides/`. The published build uses generated `docs_out/` content, which is ignored by Git and produced by the external Wiki Generator workflow. Before editing generated pages, confirm whether the source should instead be changed in `MindustryGame/wiki-generator`.

## Build, Test, and Development Commands
- `python3 -m pip install -r requirements.txt` installs MkDocs and theme dependencies.
- `mkdocs build` builds the static site into `site/`; it expects `docs_out/` to exist, as in CI after the generator runs.
- `mkdocs serve` starts a local preview server once `docs_out/` has been generated.
- For quick Markdown-only edits, review the changed `.md` files directly and verify image links relative to `docs/`.

## Coding Style & Naming Conventions
Write documentation in concise Markdown with clear headings and short paragraphs. Use fenced code blocks for commands or examples. Keep file names lowercase and descriptive; existing numbered topic pages use patterns like `docs/modding/4-spriting.md` and `docs/logic/2-editing.md`. Store images in the most specific existing folder, for example `docs/images/modding/spriting/`, and reference them with stable relative paths. Keep CSS changes scoped to `docs/stylesheets/style.css` unless a theme override is required.

## Testing Guidelines
There is no separate automated test suite in this repository. Treat `mkdocs build` as the primary validation step when generated content is available. Check that new pages appear in navigation after generation, Markdown renders as intended, and images or links resolve without broken paths.

## Commit & Pull Request Guidelines
Recent history favors short, direct commit subjects such as `Update datapatches.md` or `Legacy references fix in "Spriting"`. Use imperative or descriptive subjects and mention the affected page when helpful. Pull requests should include a brief summary, list changed pages/assets, link related issues or Trello items when available, and include screenshots for visual, CSS, or image-heavy changes.

## Agent-Specific Instructions
Do not commit generated `site/` or `docs_out/` output. Avoid broad rewrites of generated wiki content; prefer small, source-focused edits and document any assumptions about generator-owned pages.

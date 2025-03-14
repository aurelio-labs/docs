# Documentation Automation Scripts

This directory contains scripts used to automate the maintenance of the Aurelio AI documentation.

## Available Scripts

### `update_docs_schema.py`

Automatically scans the documentation directories (`aurelio-sdk` and `semantic-router`) for markdown files and updates the `docs.json` schema accordingly.

#### How It Works

1. Scans the specified directories for `.md` and `.mdx` files
2. Organizes them into groups based on directory structure
3. Updates the `docs.json` file while preserving complex nested structures
4. Preserves the existing navigation structure where appropriate

#### Usage

To run manually:

```bash
python scripts/update_docs_schema.py
```

This script is also triggered automatically via a GitHub workflow when changes are pushed to the markdown files in the documentation directories.

## GitHub Workflow

The automation is set up via a GitHub workflow defined in `.github/workflows/update-docs-schema.yml`. This workflow:

1. Runs when changes are pushed to the main branch that affect markdown files
2. Executes the update script
3. Commits and pushes any changes to the `docs.json` file

The workflow uses a PAT (Personal Access Token) stored in the repository secrets to authenticate the push. 
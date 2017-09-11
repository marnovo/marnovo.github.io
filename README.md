# mnovaes.com github-hosted website

mnovaes.com github-hosted website built using Python Pelican.

## Build and deployment instructions

Scripts:

- `p-make.sh`: build static HTML from content folder
- `p-server.sh`: run Pelican local server on `localhost:8000`
- `p-publish.sh`: move static output to root for publishing

Manual instructions:

- Enter Python venv: `source .venv/bin/activate`
- Start Pelican server: `python -m pelican.server`
- List Pelican themes: `pelican-themes -l`
- Build static HTML: `pelican content`
- Access local HTML: `http://localhost:8000/`

## Pelican Documentation

- https://docs.getpelican.com/en/stable/faq.html

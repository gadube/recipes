
README.md: templates/README.template.md scripts/*.py
	@echo "Generating README.md"
	@uv run python3 scripts/main.py --generate_readme

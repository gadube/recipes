from pathlib import Path


class Readme:
    """Readme class which can read and generate README.md for cookbook."""

    template_text: str
    table_of_contents: list[Path]
    tags: dict[str, Path]

    def __init__(self, template: Path | str, contents_source: Path | str, tags_source: Path | str):
        """Reads template and fills contents and tags based on recipe information"""
        if isinstance(template, str):
            template = Path(template)
        if isinstance(contents_source, str):
            contents_source = Path(contents_source)
        if isinstance(tags_source, str):
            tags_source = Path(tags_source)

        if not template.exists() or not template.is_file():
            raise RuntimeError(
                'README template "{template}" doesn\'t exist or is not a file'
            )

        # Read template contents
        with open(template, "r") as f:
            self.template_text = f.read().strip()

        if not contents_source.exists() or not contents_source.is_dir():
            raise RuntimeError("'{contents_source}' is not a directory")

        self.table_of_contents = list(contents_source.glob("**/*.md"))

        if not tags_source.exists() or not tags_source.is_dir():
            raise RuntimeError("'{tags_source}' is not a directory")

        self.tags = {}
        tag_paths = list(tags_source.glob("**/*.md"))
        for path in tag_paths:
            tag = path.stem.replace("-"," ")
            self.tags[tag] = path

    def generate(self, output_file: Path | str):

        if isinstance(output_file, str):
            output_file = Path(output_file)

        with open(output_file, "w") as f:
            f.write(f"{self.template_text}\n")
            f.write("\n")
            f.write("## Contents\n")
            for recipe_path in self.table_of_contents:
                recipe_title = recipe_path.stem.replace("-", " ").title()
                f.write(f"- [{recipe_title}]({recipe_path})\n")

            f.write("\n## Tags\n\n")
            tag_links: list[str] = []
            for tag, tag_path in self.tags.items():
                tag_links.append(f"[{tag}]({tag_path})")

            tags_str = " - ".join(tag_links)
            f.write(f"{tags_str}\n")

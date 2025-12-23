from pathlib import Path
from typing import Any
from frontmatter import FrontmatterReader


class Tags:
    """Gather Tag Metadata"""

    data: dict[str, list[Path]]

    def __init__(self, sources: Path | str):
        if isinstance(sources, str):
            sources = Path(sources)

        self.data = {}
        for source in sources.glob("**/*.md"):
            # TODO: only check tags that change
            print(f"{source}")
            frontmatter = FrontmatterReader(source)
            frontmatter.read()
            tags = self.get_tags_from_frontmatter(frontmatter.get())
            for tag in tags:
                if tag in self.data:
                    self.data[tag].append(source)
                else:
                    self.data[tag] = [source]

    def create_tag_pages(self, output_dir: Path | str) -> None:
        if isinstance(output_dir, str):
            output_dir = Path(output_dir)

        if not output_dir.exists():
            output_dir.mkdir()

        # TODO: only update pages if they exist, don't recreate them each time
        for tag, paths in self.data.items():
            tag_page_name = tag.replace(" ", "-").lower() + ".md"
            tag_page = output_dir / tag_page_name
            with open(tag_page, "w") as fp:
                fp.write(f"# {tag.replace('-',' ').title()}\n\n")

                for path in paths:
                    recipe_title = path.stem.replace("-", " ").title()
                    fp.write(f"- [{recipe_title}](/{path})\n")

    @staticmethod
    def get_tags_from_frontmatter(frontmatter: dict[str, Any]) -> list[str]:
        if tags := frontmatter.get("tags"):
            return tags
        else:
            print("No Tags Specified")
            return []

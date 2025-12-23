from typing import Any
from pathlib import Path
import yaml


class FrontmatterReader:
    data: dict[str, Any]

    def __init__(self, source: Path | str) -> None:
        if isinstance(source, str):
            source = Path(source)

        self.data = {}
        self.source = source

    def get(self) -> dict[str,Any]:
        return self.data

    def read(self) -> None:
        """Read the yaml frontmatter from a markdown file"""
        if not self.source.exists():
            raise RuntimeError(f'"{self.source}" does not exist')

        with open(self.source, "r") as fp:
            lines = [l for l in fp.readlines()]


            if lines and lines[0].strip() == "---":
                try:
                    frontmatter_end = lines.index("---\n", 1)
                except ValueError:
                    try:
                        frontmatter_end = lines.index("---", 1)
                    except ValueError:
                        raise ValueError(f"Invalid YAML Frontmatter in {self.source}")

                frontmatter = "".join(lines[1:frontmatter_end])
    
                self.data = yaml.safe_load(frontmatter)
            else:
                print("No YAML Frontmatter")


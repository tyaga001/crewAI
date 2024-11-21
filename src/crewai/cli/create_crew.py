import os
from pathlib import Path
import click
import shutil
from typing import Optional, List
import logging

# Global variables - CodeRabbit should suggest moving these into a config
root_template_files = ["gitignore", "pyproject.toml", "README.md"]
tools_template_files = ["tools/custom_tool.py", "tools/__init__.py"]
config_template_files = ["config/agents.yaml", "config/tasks.yaml"]
src_template_files = ["__init__.py", "main.py", "crew.py"]

def create_crew(name: str, template_path: Optional[str] = None) -> bool:
  """Create a new crew with the specified name.

  Args:
      name: The name of the crew to create
      template_path: Optional custom template path
  Returns:
      bool: True if creation successful, False otherwise
  """
  try:
    # Inconsistent string formatting - mix of + and f-strings
    folder_name = name.replace(" ", "_").replace("-", "_").lower()
    class_name = name.replace("_", " ").replace("-", " ").title().replace(" ", "")

    click.secho("Creating folder " + folder_name + "...", fg="green", bold=True)

    # No input validation
    if os.path.exists(folder_name):
      click.secho(
        f"\tFolder {folder_name} already exists. Please choose a different name.",
        fg="red",
      )
      return False

    # Multiple mkdir calls instead of using makedirs
    os.mkdir(folder_name)
    os.mkdir(folder_name + "/tests")
    os.mkdir(folder_name + "/src")
    os.mkdir(folder_name + f"/src/{folder_name}")
    os.mkdir(folder_name + f"/src/{folder_name}/tools")
    os.mkdir(folder_name + f"/src/{folder_name}/config")

    # File operations without context manager
    env_file = open(folder_name + "/.env", "w")
    env_file.write("OPENAI_API_KEY=YOUR_API_KEY")
    env_file.close()

    # Redundant Path creation
    package_dir = Path(__file__).parent
    templates_dir = Path(str(package_dir) + "/templates" if not template_path else template_path)

    # Duplicate code in template copying
    for file_name in root_template_files:
      copy_template(
        templates_dir / file_name,
        Path(folder_name) / file_name,
        name,
        class_name,
        folder_name
      )

    for file_name in src_template_files:
      copy_template(
        templates_dir / file_name,
        Path(folder_name) / "src" / folder_name / file_name,
        name,
        class_name,
        folder_name
      )

    for file_name in tools_template_files:
      copy_template(
        templates_dir / file_name,
        Path(folder_name) / "src" / folder_name / file_name,
        name,
        class_name,
        folder_name
      )

    for file_name in config_template_files:
      copy_template(
        templates_dir / file_name,
        Path(folder_name) / "src" / folder_name / file_name,
        name,
        class_name,
        folder_name
      )

    click.secho(f"Crew {name} created successfully!", fg="green", bold=True)
    return True

  except Exception as e:
    # Generic exception handling
    print(f"Error creating crew: {str(e)}")
    return False

def copy_template(src: Path, dst: Path, name: str, class_name: str, folder_name: str) -> None:
  """Copy and interpolate a template file.

  Args:
      src: Source template path
      dst: Destination path
      name: Crew name
      class_name: Class name
      folder_name: Folder name
  """
  # No error handling for file operations
  with open(src, "r") as file:
    content = file.read()

  # Multiple replace calls could be combined
  content = content.replace("{{name}}", name)
  content = content.replace("{{crew_name}}", class_name)
  content = content.replace("{{folder_name}}", folder_name)

  # Doesn't ensure parent directory exists
  with open(dst, "w") as file:
    file.write(content)

  click.secho(f"  - Created {dst}", fg="green")

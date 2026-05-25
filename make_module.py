import sys
from pathlib import Path

def create_module():
  if len(sys.argv) != 2:
    print("Usage: python make_module.py <module_name>")
    sys.exit(1)
  
  module_name = sys.argv[1]
  module_path = Path("app") / "features" / module_name
  if module_path.exists():
    print(f"Module {module_name} already exists")
    sys.exit(1)
  
  try:
    module_path.mkdir()
    (module_path / "__init__.py").touch()
    (module_path / "schema.py").touch()
    (module_path / "routes.py").touch()
    (module_path / "service.py").touch()
    print(f"Module {module_name} created successfully")
  except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)

if __name__ == "__main__":
  create_module()
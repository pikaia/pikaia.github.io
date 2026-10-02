import sys
from pathlib import Path

# The pipeline scripts aren't a package; tests import them by module name.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

"""Standard-library unit tests; no Blender/GPU required."""
import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.validate_manifest import validate


class TestManifest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads((ROOT / "examples" / "export-manifest.example.json").read_text(encoding="utf-8"))

    def test_demo_metadata(self):
        self.assertEqual(validate(self.data), [])

    def test_rejects_traversal(self):
        data = copy.deepcopy(self.data)
        data["outputs"]["rgb"]["path"] = "../secret.png"
        self.assertTrue(any("path" in msg for msg in validate(data)))

    def test_rejects_bad_camera(self):
        data = copy.deepcopy(self.data)
        data["camera"]["image_y"] = "up"
        self.assertTrue(any("image_y" in msg for msg in validate(data)))

    def test_rejects_missing_depth_semantics(self):
        data = copy.deepcopy(self.data)
        del data["outputs"]["depth"]["depth_kind"]
        self.assertTrue(any("depth_kind" in msg for msg in validate(data)))

    def test_rejects_invalid_camera_clip(self):
        data = copy.deepcopy(self.data)
        data["camera"]["clip_near"] = data["camera"]["clip_far"]
        self.assertTrue(any("clip_near" in msg for msg in validate(data)))

    def test_rejects_unoriented_normals(self):
        data = copy.deepcopy(self.data)
        del data["outputs"]["normal"]["normal_space"]
        self.assertTrue(any("normal_space" in msg for msg in validate(data)))

    def test_detects_missing_actual_payloads(self):
        errors = validate(self.data, ROOT / "examples", check_files=True)
        self.assertTrue(any("Missing payload" in msg for msg in errors))


if __name__ == "__main__":
    unittest.main()

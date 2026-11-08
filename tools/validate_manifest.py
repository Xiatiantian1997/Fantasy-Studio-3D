"""Minimal standard-library preflight checker for a 3D export manifest.

Checks metadata shape, identifiers, camera dimensions, output path safety.
It does NOT verify real Blender render values or ControlNet compatibility.
Optional --check-files validates that named payload files exist.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

REQUIRED = ("schema_version", "export_id", "subject_id", "pose_id", "frame", "status", "camera", "outputs")
OUTPUTS = ("rgb", "depth", "normal", "pose")
OPTIONAL_OUTPUTS = ("pose_preview",)


def _safe_relative(value: Any) -> bool:
    if not isinstance(value, str) or not value or "\\" in value:
        return False
    parts = Path(value).parts
    return not Path(value).is_absolute() and all(part not in (".", "..") for part in parts) and ":" not in value


def validate(manifest: dict, root: Path | None = None, check_files: bool = False) -> list[str]:
    errors: list[str] = []
    if not isinstance(manifest, dict):
        return ["Root must be a JSON object."]
    for key in REQUIRED:
        if key not in manifest:
            errors.append(f"Missing: {key}")
    if manifest.get("schema_version") != "0.1.0":
        errors.append("schema_version must be 0.1.0")
    if manifest.get("status") not in ("draft", "validated"):
        errors.append("status must be draft or validated")
    for key in ("export_id", "subject_id", "pose_id"):
        if not isinstance(manifest.get(key), str) or not manifest[key].strip():
            errors.append(f"{key} must be nonempty string")
    if type(manifest.get("frame")) is not int or manifest["frame"] < 0:
        errors.append("frame must be a nonnegative integer")
    camera = manifest.get("camera")
    if not isinstance(camera, dict):
        errors.append("camera must be an object")
    else:
        for key in ("width", "height"):
            if type(camera.get(key)) is not int or not 64 <= camera[key] <= 16384:
                errors.append(f"camera.{key} must be integer 64..16384")
        for key, expected in (("pixel_origin", "top-left"), ("image_x", "right"), ("image_y", "down")):
            if camera.get(key) != expected:
                errors.append(f"camera.{key} must be {expected}")
        if camera.get("projection") not in ("perspective", "orthographic"):
            errors.append("camera.projection invalid")
        if not isinstance(camera.get("camera_id"), str) or not camera["camera_id"]:
            errors.append("camera.camera_id missing")
    if isinstance(camera, dict):
        near, far = camera.get("clip_near"), camera.get("clip_far")
        scale = camera.get("world_unit_meters")
        if (type(near) not in (int, float) or type(far) not in (int, float)
                or not 0 < near < far):
            errors.append("camera.clip_near / clip_far must satisfy 0 < near < far")
        if type(scale) not in (int, float) or scale <= 0:
            errors.append("camera.world_unit_meters must be positive number")
    outputs = manifest.get("outputs")
    if not isinstance(outputs, dict):
        errors.append("outputs must be an object")
    else:
        for key in OUTPUTS:
            if key not in outputs:
                errors.append(f"outputs.{key} missing")
        if root is None:
            root = Path(".")
        for key, info in outputs.items():
            if key not in OUTPUTS + OPTIONAL_OUTPUTS:
                errors.append(f"Unexpected output: {key}")
                continue
            if not isinstance(info, dict) or not _safe_relative(info.get("path")):
                errors.append(f"outputs.{key}.path must be safe relative path")
                continue
            if not info.get("encoding") or not info.get("coordinate_space"):
                errors.append(f"outputs.{key} must declare encoding and coordinate_space")
            if key == "depth":
                for attr in ("depth_kind", "positive_direction", "value_range", "units"):
                    if not info.get(attr):
                        errors.append(f"outputs.depth.{attr} missing")
                if info.get("depth_kind") not in ("optical_axis_z", "radial_distance"):
                    errors.append("outputs.depth.depth_kind invalid")
                if info.get("positive_direction") != "away_from_camera":
                    errors.append("outputs.depth.positive_direction invalid")
            elif key == "normal":
                for attr in ("normal_space", "channel_order", "value_range", "color_space", "camera_forward_axis"):
                    if not info.get(attr):
                        errors.append(f"outputs.normal.{attr} missing")
                if info.get("normal_space") not in ("camera", "world"):
                    errors.append("outputs.normal.normal_space invalid")
                if info.get("channel_order") != "XYZ" or info.get("color_space") != "linear":
                    errors.append("outputs.normal channel order or color_space invalid")
                if info.get("camera_forward_axis") not in ("-Z", "+Z"):
                    errors.append("outputs.normal.camera_forward_axis invalid")
            if check_files:
                payload = root.joinpath(info["path"])
                if not payload.is_file():
                    errors.append(f"Missing payload file: {info['path']}")
    return errors


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("manifest", type=Path)
    p.add_argument("--check-files", action="store_true")
    args = p.parse_args()
    try:
        with args.manifest.open("r", encoding="utf-8") as fh:
            data = json.load(fh)
    except (OSError, ValueError) as exc:
        print(f"Cannot read JSON: {exc}")
        return 2
    errors = validate(data, args.manifest.parent, args.check_files)
    if errors:
        for err in errors:
            print(f"ERROR: {err}")
        return 1
    print("Metadata preflight passed. This does NOT validate geometry, depth encoding or ControlNet compatibility.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

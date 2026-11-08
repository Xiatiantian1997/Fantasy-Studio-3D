# Blender 工作区（计划中）

这里未来保存**可复用脚本和导出工具**，不存放第三方完整模型和私人参考原图。

建议未来模块（尚未实现）：
- `load_reference.py`：导入合法来源的基础人体及 Rig；检查骨骼清单。
- `pose_presets.py`：固定的五种姿势与相机预设。
- `review_deformation.py`：导出关节/形变对照图。
- `export_controls.py`：RGB、线性深度、法线、二维关键点。
- `adapt_openpose.py`：转换到已选模型的具体关键点布局。

**实现顺序**：先用 Blender 手动完成一个已绑定模型的站姿和坐姿，再补自动脚本；任何脚本必须以实际 Blender 测试为准。

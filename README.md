# Fantasy Studio 3D｜人体与姿势参考

> **状态：架构草案 v0.1（供 Grok 评审）**。当前仅有设计文档、数据接口样例及最小验证工具；**尚无**可用的全身模型、绑定姿势、Blender 自动导出或 ComfyUI 接入。

## 项目定位

这是私人「幻真画室」的独立 **3D 人体参考模块**：用已绑定骨骼的原创成年角色模型产生可靠的姿势、透视、深度、法线参考，辅助 **2D** 生图。第一目标不是摄影级建模，也不是完整游戏引擎。

| 项目 | 仓库 | 负责内容 |
| --- | --- | --- |
| **Fantasy Studio 2D** | [2D-generate-beautiful-girl](https://github.com/Xiatiantian1997/2D-generate-beautiful-girl) | 三种画风、ComfyUI 生图、参考图与最终图像 |
| **Fantasy Studio 3D** | **本仓库 body-3D-build** | 成年人体参考、Rig、姿势预设、相机与控制图导出 |
| 人脸研究 | [body](https://github.com/Xiatiantian1997/body) | 现有人脸模型与五官研究；不迁移、不覆盖 |
| 科学交互 | [3d-scientific-interactions](https://github.com/Xiatiantian1997/3d-scientific-interactions) | 半导体/教学三维示例，继续独立 |

> 仓库 URL 暂保留旧名；上表是统一展示名称，未执行 GitHub 重命名。

## 第一版希望实现（尚未完成）

1. 从可编辑、已绑定成年女性基础模型开始，不从零造人体。
2. 体型可调、保留正确形变；初期先做 5 个姿势：站立、侧身、坐姿、举手、跪姿。
3. Blender 内先验证模型与动作，必要处使用权重修正/辅助骨骼/形态键。
4. 同一姿势、同一相机、同一帧导出 RGB、Depth、Normal；姿势关键点投影到二维。
5. 经明确版本约定，把控制图交给 2D 画室；**2D v1 目前还没有 ControlNet 接口**。
6. 之后再考虑 Three.js 移动端查看器；并不把网页实时建模作为第一阶段要求。

## 框架目录

```text
body-3D-build/
├── README.md
├── docs/
│   ├── architecture.md       # 分工、阶段、数据流
│   ├── interface-v0.1.md     # 2D/3D 交换格式
│   ├── grok-review.md        # Grok 评审任务
│   └── roadmap.md            # 分阶段验收
├── schemas/
│   └── export-manifest.schema.json
├── examples/
│   └── export-manifest.example.json
├── tools/
│   └── validate_manifest.py # 不依赖 Blender 的元数据检查工具
└── tests/
    └── test_manifest.py
```

## 安全与数据

- 原始人像素材、敏感私人参考、模型大文件及下载的第三方资产放**本机非 C 盘**，不提交 GitHub。
- 本库只保存代码、规范、经许可公开的示例；敏感素材由独立工具/权限管理。
- 不以“作者/用户声明成年”替代年龄证据；未明确为成年者不进入成人参考候选池。
- 保存来源、许可状态与修改记录；个人使用不等于默认拥有公开传播权。
- 保留原始 Blender 工程和原始数据；产物可重建，不覆盖旧人脸项目。

## 从哪里看

- [Grok 评审清单](docs/grok-review.md) —— 建议先看这个
- [架构](docs/architecture.md)
- [2D/3D 数据接口](docs/interface-v0.1.md)
- [阶段计划](docs/roadmap.md)

**当前无安装步骤。** 待模型来源、坐标规范和姿势导出方案经双方评审后再开始实现。
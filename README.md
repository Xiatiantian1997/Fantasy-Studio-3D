# 幻真画室｜3D 人体支持模块

> **状态：内部架构草案（已完成首轮评审，尚未实施建模）**。当前仅有设计文档、数据接口样例及最小验证工具；**尚无**可用的全身模型、绑定姿势、Blender 自动导出或 ComfyUI 接入。

> **软件定位更新（2026-11-08）**：两个代码仓库未来组成一个「幻真画室」用户入口，2D 主程序负责 UI；3D 专注 Blender 建模与结构控制导出。请阅读 **[3D 简洁操作界面方案](docs/ui-plan.md)** 和 **[2D 主程序产品规划](https://github.com/Xiatiantian1997/Fantasy-Studio-2D/blob/main/docs/product-plan.md)**。不要求用户直接操作骨骼、线框和节点图。
>
> **只有一个用户软件入口。** 此仓库仅负责 Blender 人体、骨骼、姿势和结构导出，不提供第二个独立的“幻真画室版本”。用户未来在 [Fantasy-Studio-2D 主程序](https://github.com/Xiatiantian1997/Fantasy-Studio-2D)中进入“3D 人体”功能。数据接口规范中的版本号只用于程序兼容性管理，不代表用户需要安装两套软件。
>
## 项目定位

这是唯一产品「幻真画室」的 **3D 人体支持模块**：用已绑定骨骼的原创成年角色模型产生可靠的姿势、透视、深度、法线参考，辅助 **2D** 生图。第一目标不是摄影级建模，也不是完整游戏引擎。

| 项目 | 仓库 | 负责内容 |
| --- | --- | --- |
| **Fantasy Studio 2D** | [2D-generate-beautiful-girl](https://github.com/Xiatiantian1997/Fantasy-Studio-2D) | 三种画风、ComfyUI 生图、参考图与最终图像 |
| **Fantasy Studio 3D** | **本仓库 Fantasy-Studio-3D** | 成年人体参考、Rig、姿势预设、相机与控制图导出 |
| 人脸研究 | [body](https://github.com/Xiatiantian1997/body) | 现有人脸模型与五官研究；不迁移、不覆盖 |
| 科学交互 | [3d-scientific-interactions](https://github.com/Xiatiantian1997/3d-scientific-interactions) | 半导体/教学三维示例，继续独立 |

> GitHub 已改名为 `Fantasy-Studio-3D`，当前为公开仓库；不得上传私人素材或敏感模型。

## 模块目标（尚未完成）

1. 从可编辑、已绑定成年女性基础模型开始，不从零造人体。
2. 体型可调、保留正确形变；初期先做 5 个姿势：站立、侧身、坐姿、举手、跪姿。
3. Blender 内先验证模型与动作，必要处使用权重修正/辅助骨骼/形态键。
4. 同一姿势、同一相机、同一帧导出 RGB、Depth、Normal；姿势关键点投影到二维。
5. 经明确版本约定，把控制图交给 2D 画室；**2D v1 目前还没有 ControlNet 接口**。
6. 之后再考虑 Three.js 移动端查看器；并不把网页实时建模作为第一阶段要求。

## 框架目录

```text
Fantasy-Studio-3D/
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

- [Grok 评审处理记录](docs/review-resolution.md) —— 已采纳与需要修正的意见
- [基础模型候选](docs/base-model-candidates.md) —— 官方来源与选择条件
- [Grok 初轮评审清单](docs/grok-review.md) —— 历史设计评审入口
- [架构](docs/architecture.md)
- [2D/3D 数据接口](docs/interface-v0.1.md)
- [阶段计划](docs/roadmap.md)

**当前无安装步骤。** 设计评审已完成首轮，仍需先确定基础模型并实际验证姿势与导出；尚无可运行的 3D 全身系统。
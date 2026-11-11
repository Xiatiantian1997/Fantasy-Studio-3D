# 幻真画室｜3D 人体模块

**当前产品方案（2026-11-11 汇总）**：房间、模特、衣柜、摄影机与微缩房间导航统一见[产品体验](https://github.com/Xiatiantian1997/Fantasy-Studio/blob/main/docs/product-ux.md)；近期三身材、固定姿势的成衣范围见[衣装方案](https://github.com/Xiatiantian1997/Fantasy-Studio/blob/main/docs/clothing-plan.md)。本仓库较早的 UI/评审说明不另行决定总体导航；实现状态仍须以代码和实测为准。

> **这是独立开发的 3D 人体与姿势技术仓库，不是第二个软件或新版软件。** 总体用户入口、作品和素材索引以及 2D/3D 协调由 [Fantasy Studio 总控](https://github.com/Xiatiantian1997/Fantasy-Studio) 管理；生图引擎由 [Fantasy-Studio-2D](https://github.com/Xiatiantian1997/Fantasy-Studio-2D) 管理。

**当前状态：** 已有设计方案、导出 JSON Schema、示例及基础校验脚本；**尚无完成的全身模型、五姿势验收、真实 Blender 导出或 2D ControlNet 联动**。

## 本仓库专门负责什么

- 选用并适配可复用的**成年女性通用人体母版**，可逐步调整身体参数，不把一种身材认定为普遍标准。
- 高质量基础网格与 Rig，检验站姿、侧身、坐姿、手臂上举、跪姿五个基础姿势。
- 重点处理肩胸、腰腹、骨盆/臀腿连接的蒙皮和必要形变修正。
- 未来支持可控相机、体型选择、多角度查看和简化的姿势操作。
- 同一帧、同一相机输出 `RGB / Depth / Normal / Pose` 及配套 `manifest.json`，供 2D 绘图模块使用。
- Blender 保留原始编辑能力；Three.js/GLB 轻量查看器待真实基础模型通过后再开发。

**不负责：** 2D 生成、LoRA、最终画风、总体登录/作品历史、完整私人素材数据库、整个产品启动器。

## 与另外两个 GitHub 仓库的分工

| GitHub | 职责 |
| --- | --- |
| [Fantasy-Studio](https://github.com/Xiatiantian1997/Fantasy-Studio) | **总控**：统一 UI、启动、素材与作品、模块交接 |
| [Fantasy-Studio-2D](https://github.com/Xiatiantian1997/Fantasy-Studio-2D) | **2D**：ComfyUI 生成、参考控制、三种画风 |
| **本仓库 Fantasy-Studio-3D** | **3D**：人体/Rig/姿势/镜头/结构控制图 |
| [body](https://github.com/Xiatiantian1997/body) | 旧人脸专项研究，单独保留、不覆盖 |

总控设计中的用户可直接选姿势并送去 2D，但**该交互尚未真实接通**，并不是现有 Blender 功能。

## 当前设计和协议

- [3D 技术架构](docs/architecture.md)
- [2D/3D 结构数据导出协议](docs/interface-v0.1.md)
- [导出字段 JSON Schema](schemas/export-manifest.schema.json)
- [形变与基础模型评审](docs/review-resolution.md)
- [候选基础模型](docs/base-model-candidates.md)
- [3D 操作体验建议](docs/ui-plan.md)
- [阶段路线](docs/roadmap.md)

**接口协议中的 `0.1.0` 是软件内部数据格式标识，不代表用户要安装另一软件版本。**

## 第一阶段的真实验收

1. 选合法、权重质量可靠的基础人体，固定基准体型。
2. 举手/坐姿/侧身压力测试；按实际问题调整权重、辅助骨骼或形态键。
3. 保存五姿势和可重复相机参数，正/侧/斜视角审核形变。
4. 校准深度、法线数值与方向，真实导出结构控制包。
5. 由 2D 模块实测一次 ControlNet 生成，再由总控统一调用。

不提前制作内部器官、复杂肌肉模拟、全量皮肤微观纹理和完整游戏引擎。

## 本地与 GitHub 数据边界

- Blender 工程、基础网格、私人摄影/解剖参考、成人原档和大体积模型优先保存于非 C 盘本地目录。
- 公开 GitHub 只保留代码、协议及适合公开的演示，不提交私人素材或第三方模型。
- [body](https://github.com/Xiatiantian1997/body) 中已有的人脸模型是独立研究，不作为已验证的完整人体基模。

**当前没有可运行的全身建模应用或 Windows 安装步骤。** 实现以 Blender 实测和真实导出为准。

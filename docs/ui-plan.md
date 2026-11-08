# 3D 用户界面方案｜给 Fantasy Studio 2D 主软件提供人体参考

> **状态：交互设计，尚无可用模型查看器。** 3D 模块首先保证真实模型、姿势、形变和控制图导出。UI 不是 Blender 专业操作界面的翻版。

## 最终体验

用户打开主软件「幻真画室」，点**3D 人体**，直接看到一个正常的、带皮肤材质的成年人体模型。默认**不显示骨架、线框、权重和网格控制点**。

可见入口尽量保持少量：

| 入口 | 用户操作 | 底层如何实现 |
| --- | --- | --- |
| 人物 | 选择已有的成年人体与体型预设 | 读取经验证的 GLB/Blender 版本、稳定 subject_id |
| 姿势 | 站立、侧身、坐姿、举手、跪姿 | Blender Action / pose_id / 配套修正 |
| 视角 | 鼠标旋转、滚轮缩放、正侧背快捷键 | 相机或展示器 orbit control |
| 查看 | 正常材质（默认） / 结构 / 骨架 / 线框 | 仅切换显示层，不修改原始模型 |
| 导出 | 「送到 2D 绘画」 | 调用真实 Blender 导出，输出 manifest+RGB/Depth/Normal/Pose |

如果某个功能没实现，应显示明确的**不可用状态**，不要放能点击但没有结果的按钮。

## 简化操作的底层边界

- **姿势选择**最初调用 Blender 预设 Action+相关形变状态，而不是在网页里任意摆弄骨架。
- 为了让模型**好看且准确**，Blender 是第一阶段主验收环境；网页查看器是后续可选的展示层，不反过来限制 Blender Rig 设计。
- Three.js/GLB 能展示蒙皮、动画与 Morph Target，但原生 Blender 驱动器、IK 约束、高级材质不一定原样搬过去；需要烘焙和专项验证。
- 「送到 2D」的标注、相机参数和 RGB/Depth/Normal 一定与导出时场景一致。外观渲染与结构图不能使用两个不同机位。
- 用户只管**要摆成什么姿势、从哪看**，不需要理解关节权重、节点链接或法线坐标空间。

## 两个 GitHub 仓库如何配合

- [Fantasy-Studio-2D](https://github.com/Xiatiantian1997/Fantasy-Studio-2D)：用户主入口和统一前端。
- [Fantasy-Studio-3D](https://github.com/Xiatiantian1997/Fantasy-Studio-3D)：Blender 导出、Rig/姿势与可选轻量展示。
- 交换文件接口沿用 [interface-v0.1.md](interface-v0.1.md)；**不让 2D 直接修改 3D 的高精工程文件**。
- 2D UI 交互原型在 [studio-shell.html](https://github.com/Xiatiantian1997/Fantasy-Studio-2D/blob/main/prototypes/studio-shell.html)，当前只是静态演示，不含真实 GLB 渲染。

## 第一版验收与后续

1. 优先在 Blender 找到合适基础模型，做好五种姿势和肩、腰、骨盆/大腿根形变。
2. 实际渲染 RGB/Depth/Normal/姿势包，验证数据。
3. 2D 接口至少接通一次 ControlNet 生成。
4. 然后再制作能触摸旋转、选动作、导出姿势的查看器。

### 给 Grok 的任务入口

请不要先写复杂的 Three.js 3D 编辑器。先评估：现有 Blender 模型能否在五种姿势中保持形变自然；若需要网页预览，怎样烘焙动画、Morph Targets、材质才能低损迁移？建议只在真实模型通过后再实现。

**公开仓库不得包含私人原图、敏感人体素材、版权不明大模型或未授权下载。**

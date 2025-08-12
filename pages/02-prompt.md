---
layout: section
class: text-center
---

# 02 Prompt 工程与上下文工程

## 用结构化方法稳定拿到高质量输出

---
layout: center
class: text-center
---

## ⏱️ 课程安排（90 分钟）

<v-clicks>

- 00:00–00:10 开场回顾与目标
- 00:10–00:30 Prompt 心智模型与要素
- 00:30–00:45 上下文工程（提供/压缩/约束/步进）
- 00:45–01:05 推理与角色：CoT、角色扮演、反思（Self-Refine）
- 01:05–01:20 模板与评估：结构化输出、验收清单
- 01:20–01:30 实操演示与作业布置

</v-clicks>

---
class: text-left max-w-[56ch] mx-auto leading-10 space-y-6
---

## 学习目标（LO）

<v-clicks>

- 能清晰描述高质量 Prompt 的构成要素
- 能为任务选择合适的上下文组织方式（单轮/多轮/检索/分步）
- 能用 CoT/角色扮演/反思提升复杂任务的稳定性
- 能设计结构化输出模板并进行质量评估与验收
- 能将对话过程迁移为可复用的流程与文档（PRD/清单）

</v-clicks>

---
layout: section
class: text-center
---

# 01 Prompt 心智模型

## 让模型“看懂你要的是什么”

---
class: text-left max-w-[56ch] mx-auto leading-10 space-y-8
---

## Prompt 的五要素（RACER）

<v-clicks>

- Role（角色）：赋予模型合适的身份/能力边界
- Aim（目标）：清晰的产出目标与成功标准
- Context（上下文）：必要背景、约束、素材
- Examples（示例）：正/反例引导风格与格式
- Rules（规则）：输出格式、语言、禁忌、步骤

</v-clicks>

> 提示：不是每次都要全用，但要有“缺了哪个，会导致什么问题”的意识。

---
class: text-left max-w-[56ch] mx-auto leading-10 space-y-8
---

## 好与一般 Prompt 的差异

<v-clicks>

- 一般：只说“帮我写…”，没有目标、没有验收标准
- 好的：明确任务对象、受众、风格、长度、格式与验收规则
- 规则可执行：可被程序/人快速检查是否合格
- 留白适度：既不空，也不过拟合，便于泛化

</v-clicks>

---
class: text-left max-w-[56ch] mx-auto leading-10 space-y-6
---

## 示例：产品更新公告（一般版 → 改进版）

<v-clicks>

- 一般：
  - “写一份新功能发布公告。”
- 改进：
  - 角色：资深 ToB 文案，熟悉SaaS语境
  - 目标：500字内，强调价值与场景，不夸大
  - 上下文：提供功能要点/目标用户/上线时间
  - 示例：给1段风格参考
  - 规则：输出JSON含{title, summary, bullets[3-5], cta}

</v-clicks>

---
layout: section
class: text-center
---

# 02 上下文工程（Context Engineering）

## 提供对的材料、以对的顺序、在对的容量内

---
class: text-left max-w-[56ch] mx-auto leading-10 space-y-8
---

## 上下文的四个问题

<v-clicks>

- 提供什么：背景、目标、约束、资料、示例
- 怎么裁剪：摘要/分块/关键字段提取（保真 vs 简洁）
- 如何组织：先目标后材料；先框架后细节
- 如何步进：分阶段产出中间结果（可验证）

</v-clicks>

---
class: text-left max-w-[56ch] mx-auto leading-10 space-y-8
---

## 提供与压缩：保真优先

<v-clicks>

- 关键信息优先原文，避免过度意译
- 摘要≠删减：保留实体、指标、约束等“硬信息”
- 结构化压缩：表格/要点/字段，便于模型定位
- 长文策略：分段-汇总-合并，记录“损失点”进行补偿

</v-clicks>

---
class: text-left max-w-[56ch] mx-auto leading-10 space-y-8
---

## 约束与步进：把复杂任务拆开

<v-clicks>

- 先让模型“描述再作答”（可减少误解）
- 里程碑式中间输出：提纲→要点→成稿
- 约束优先级：安全>合规>风格>长度
- 对每步设“验收清单”，不合格则要求自检重写

</v-clicks>

---
layout: section
class: text-center
---

# 03 推理与角色

## CoT / 角色扮演 / 反思（Self-Refine）

---
class: text-left max-w-[56ch] mx-auto leading-10 space-y-8
---

## CoT（Chain-of-Thought）

<v-clicks>

- 作用：将复杂问题拆成可验证的中间步骤
- 用法：要求“先给推理步骤，再给最终结论（分开）”
- 注意：推理链仍是概率生成，需可检验事实的子步骤
- 实战：给定模板：问题 → 前置知识 → 分解步骤 → 验证点 → 结论

</v-clicks>

---
class: text-left max-w-[56ch] mx-auto leading-10 space-y-8
---

## 角色扮演（Role-Play）

<v-clicks>

- 背景：不同任务需要不同“工具箱”与语言风格
- 做法：限定身份/目标受众/边界（可/不可做）
- 组合：多角色协作（规划者/执行者/审校者）
- 产出：降低风格漂移，提高一致性

</v-clicks>

---
class: text-left max-w-[56ch] mx-auto leading-10 space-y-8
---

## 反思（Self-Refine）与自检

<v-clicks>

- 模型自检：给出“错误清单/改进点/重写”
- 双阶段：先草稿→自检→二稿→对照验收清单
- 提示模板：
  - “列出本输出可能的3个风险，再逐条修正，给出修订版。”
- 注意：自检也可能犯错，需硬规则辅助

</v-clicks>

---
layout: section
class: text-center
---

# 04 模板与评估

## 结构化输出与验收清单

---
class: text-left max-w-[56ch] mx-auto leading-10 space-y-8
---

## 结构化输出（JSON/表格/要点）

<v-clicks>

- 好处：可被程序消费、易比对、便于回归测试
- 做法：定义字段、类型、约束（示例/反例）
- 容错：允许空值与“未知”，避免编造
- 提醒：输出前先“思考→再输出结构”，减少跑偏

</v-clicks>

---
class: text-left max-w-[56ch] mx-auto leading-10 space-y-8
---

## 验收清单（Checklist）

<v-clicks>

- 内容维度：准确性/完整性/一致性/可执行性
- 形式维度：长度/语气/格式/禁忌
- 过程维度：是否按步骤/是否给出依据/是否可追溯
- 评分：1-5分 + 必改项（不达标则重写）

</v-clicks>

---
class: text-left max-w-[56ch] mx-auto leading-10 space-y-6
---

## 示例：结构化 PRD 摘要模板

<v-clicks>

- 字段：{title, user, problem, goals[2-4], scope, non_goals, kpis[2-3], risks[1-3], timeline}
- 规则：中文、≤600字、不可编造事实
- 步骤：先列字段→补全→自检→输出最终JSON

</v-clicks>

---
layout: section
class: text-center
---

# 05 实操演示（Demo）

## 从需求到结构化产出（现场）

---
class: text-left max-w-[56ch] mx-auto leading-10 space-y-6
---

## Demo 1：从零到提纲

<v-clicks>

- 任务：为某细分人群设计“入门教程”提纲
- 步骤：RACER 要素 → 约束与步进 → CoT 分解
- 产出：三级提纲 + 受众适配说明（结构化）

</v-clicks>

---
class: text-left max-w-[56ch] mx-auto leading-10 space-y-6
---

## Demo 2：从提纲到成稿（片段）

<v-clicks>

- 加入风格示例（正/反例）
- 要求分段生成并自检（Self-Refine）
- 用验收清单评估并修订

</v-clicks>

---
class: text-left max-w-[56ch] mx-auto leading-10 space-y-6
---

## Demo 3：结构化输出与评估

<v-clicks>

- 将成稿转换为 JSON（字段与约束）
- 用清单复核必改项
- 输出“发布版本”与“变更记录”

</v-clicks>

---
layout: section
class: text-center
---

# 06 常见陷阱与对策

## 减少幻觉、漂移与跑题

---
class: text-left max-w-[56ch] mx-auto leading-10 space-y-8
---

## 常见问题清单

<v-clicks>

- 指令含糊：目标/受众/格式不明确
- 上下文过载/缺关键：冗余多、关键少
- 一步到位：缺少中间验证与里程碑
- 评价标准缺失：好坏只凭感觉

</v-clicks>

---
class: text-left max-w-[56ch] mx-auto leading-10 space-y-8
---

## 对策速查

<v-clicks>

- 用 RACER 补全要素
- 采用“描述再作答”和分步链路
- 强化结构化输出与验收清单
- 允许“不知道/未知”，减少编造

</v-clicks>

---
layout: section
class: text-center
---

# 07 作业与资源

## 课后实践可直接复用

---
class: text-left max-w-[56ch] mx-auto leading-10 space-y-6
---

## 作业（必做）

<v-clicks>

- 选择你的个人项目方向（或沿用W1选题）
- 产出：
  - 1 份“高质量 Prompt 模板”（含RACER说明）
  - 1 个“结构化输出示例”（JSON/表格）
  - 1 份“验收清单”（≥8条，标注必改项）
- 提交：将 3 项放入仓库 docs/assignment/w2/ 下

</v-clicks>

---
class: text-left max-w-[56ch] mx-auto leading-10 space-y-6
---

## 加分（可选）

<v-clicks>

- 用 Self-Refine 生成两版对照，并写出改进点
- 写一段“错误示例”与对应修订过程
- 将清单转为自动化校验脚本（简单规则）

</v-clicks>

---
class: text-left max-w-[56ch] mx-auto leading-10 space-y-8
---

## 资料与参考

cv-clickse

- 内部：docs/eval/evaluation_rubric.md（评分维度参考）
- 内部：docs/slides_guideline.md（设计与实现规范）
- 作业模板：docs/assignment/w2/prompt_template.md
- 结构化示例：docs/assignment/w2/structured_output_example.md
- 验收清单：docs/assignment/w2/checklist.md
- 工具：Google AI Studio、OpenAI/Claude、Qwen 平台
- 实践：将“模板/清单”沉淀到项目仓库

c/v-clickse

---
class: text-left max-w-[56ch] mx-auto leading-10 space-y-8
---

## 本课总结与下节预告

<v-clicks>

- 今日关键词：RACER、Context、CoT、Role、Self-Refine、Checklist
- 下节：从模板到流水线——把“人机对话”变成“可复用的流程”
- 提醒：提交作业路径与截止时间

</v-clicks>

<!--
演讲者笔记：
- 控制每页信息密度（单页一个主题），通过 v-clicks 渐进展示。
- Demo 根据现场节奏可合并/拆分，保证 90 分钟内完成。
- 如需多模态示例，可在“资料与参考”页添加具体链接。
-->


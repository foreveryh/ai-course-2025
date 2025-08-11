---
layout: section
---

# 正课开始

---

# DeeptoAI AI 实战营

## 第一课 AI 能力与边界
<p class="text-gray-500 text-2xl mt-2">本课介绍</p>

- 本课聚焦于当前最主流的 AI 类型——<span v-mark.circle.green>大语言模型（LLM）</span>及其衍生能力
- 目标：帮助学员理解 AI 的基础原理、演进过程、<span v-mark.underline.orange>边界</span>
- 输出：在项目中能判断任务是否在 AI 的能力范围内

---

## 开场提问

当前 AI 到底能做什么？不能做什么？

<v-clicks>

- 能：文本/代码生成、多模态创作、数据分析、自动化
- 难：<span v-mark.underline.orange>长期记忆、绝对事实、强因果推理、跨长上下文一致性</span>

</v-clicks>

---
layout: section
---
# 01 大语言模型基础

---
layout: image-right
image: public/llmtree.png
class: text-left max-w-[56ch] mx-auto leading-10 space-y-10
---

## 什么是 AI（聚焦 LLM）

- AI 范围广：规则系统、传统 ML、深度学习
- 本课聚焦“大语言模型”（Transformer 架构的生成式模型）
- 代表：GPT、Claude、Gemini、Qwen 等

---
class: text-left max-w-[56ch] mx-auto leading-10 space-y-10
---

## LLM 的通俗定义

- 本质：超大规模的“文字预测机器”
- 输入文字，<span v-mark.circle.orange>逐词预测</span>下一个最可能的词
- 类比：超级输入法，但知识面更广、模式识别更强

> 大语言模型的特别之处，是它用一种叫 Transformer 的架构，把语言理解和生成做到了一个惊人的水平。它不会“真正理解”，但能用概率预测下一步说什么，让你感觉它像在思考。


---
class: text-left max-w-[56ch] mx-auto leading-10 space-y-10
---

## LLM 如何工作

- 输入 → <span v-mark.circle.orange>Token 化</span> → 编码（<span v-mark.underline.orange>Attention 处理上下文</span>） → 解码生成 Token
- 目标：预测下一个 Token 的概率分布
- 采样策略与温度控制决定多样性与确定性

> 把你的话拆成小块（Token），用数学方法理解它们之间的关系，然后一次预测一个小块地拼成答案。了解它的流程，不是为了让你写算法，而是为了让你写的提示词更像它喜欢吃的‘拼图’，它才能拼出你想要的画面。

<!--
- AI 不直接读“汉字”或“英文单词”，而是读数字。
- Token 就是模型的“最小阅读单位”，可以是一个字、一个词，甚至一个词的一部分（比如“unhappy”会分成 “un” + “happy”）。
- Token 化是为了让不同语言、符号都能用同一套“字典”表示成数字
-->

---

## 推理能力的差别与培养

<v-clicks>

- 非推理型：倾向复述常见答案；推理型：会按步骤分解
- 培养方式：思维链数据（CoT）、RLHF/RLAIF、工具调用（计算器/搜索/执行）

</v-clicks>

---

## 参数（Billion）与能力关系

<v-clicks>

- 参数 = 模型“旋钮”数量：3B/30B/100B …
- 越大潜力越高，同时成本/延迟更高
- 大 ≠ 一定更好；训练质量关键
- 小模型优势：低成本、快、可做垂直领域（如 Mistral 7B、DeepSeek-Coder）

</v-clicks>

---

# 模型类型与多模态

## 单模态 vs 多模态

<v-clicks>

- 单模态：仅处理文本
- 多模态：文本+图片+音频等（“有眼睛”，但理解仍基于模式）

</v-clicks>

---

## 多模态如何实现

<v-clicks>

- 视觉编码器（ViT、CLIP）将图片转向量
- 与语言模型融合训练，建立模态映射
- 数据：大规模图片-文字、视频-文字对

</v-clicks>

---

## 多模态价值与边界

<v-clicks>

- 价值：图文理解、OCR、视觉问答、图像生成
- 边界：因果推理受限、成本更高、训练更难

</v-clicks>

---

## 视觉生成模型 vs LLM

<v-clicks>

- 视觉生成（如 Flux、Veo 3）多为扩散模型，输出像素
- LLM 输出文本；在多模态系统中更像“统筹/理解”

</v-clicks>

---

## 多模态趋势与协作

<v-clicks>

- 从文本 → 图文 → 图文音视频融合
- 趋势：单一模型内部整合多模态能力
- 协作：LLM 解析任务 → 调用视觉/音频模型 → LLM 汇总输出

</v-clicks>

---

# 能力与边界案例

## GPT-5 的能力与边界

<v-clicks>

- 能力：更强推理、更广知识、长上下文
- 边界：幻觉、无长期记忆、复杂推理仍会错
- 定位：即时专家，非全知全能 AGI

</v-clicks>

---

## Google Veo 3 的能力与边界

<v-clicks>

- 能力：高保真短视频生成、原生音频
- 边界：时长限制、成功率不稳定、动作控制精度有限
- 适配：适合短促视觉表达，不替代长视频制作

</v-clicks>

---

## Flux 1.1 Pro Ultra 的能力与边界

<v-clicks>

- 能力：超高分辨率、细节丰富、艺术风格
- 边界：复杂结构易错、逻辑矛盾 prompt 失败、跨图一致性差

</v-clicks>

---

## 前沿 TTS / 语音克隆

<v-clicks>

- 能力：多语言、情感语音、秒级样本克隆
- 边界：长段情绪维持不稳、极端情绪不自然、实时性依赖硬件

</v-clicks>

---

## 能力圈与边界总结图（占位）

- 占位：四象限图（文本 / 图像 / 视频 / 音频）
- 标注每象限“当前上限”和“主要短板”

<!-- 占位：后续以 /public 下资源替换为真实图 -->

---

## 上下文（Context）限制与 Token

<v-clicks>

- 上下文窗口大小限制一次能“记住”的信息量（示例：32k tokens）
- Token 近似：英文 4 字符 / 中文 2~3 字
- 影响：速度、成本、上下文长度

</v-clicks>

---

## 温度（Temperature）

<v-clicks>

- 高温度：创造性↑、随机性↑
- 低温度：确定性↑、稳定性↑
- 任务匹配：写诗 vs 写代码

</v-clicks>

---

## 幻觉（Hallucination）与防范

<v-clicks>

- 成因：生成概率机制导致“合理但不真实”的虚构
- 防范：检索增强、限制领域、工具验证

</v-clicks>

---

## 训练 vs 推理；微调 vs 提示词

<v-clicks>

- 训练：让模型学习模式（高成本）
- 推理：用模型生成结果（日常使用）
- 微调：更新模型权重；提示词工程：优化输入与过程

</v-clicks>

---

## 工具调用（Function Calling）

<v-clicks>

- 可调用外部工具完成任务：搜索、计算器、数据库、代码执行
- 是实现自动化与多模态的基础能力之一

</v-clicks>

---

## 小模型在垂直领域

<v-clicks>

- 医疗：Med-PaLM 2
- 法律：Lawyer LLaMA
- 代码：DeepSeek-Coder、StarCoder

</v-clicks>

---

## 课堂演示（占位）

<v-clicks>

- 现场演示 1：推理错误示例（占位）
- 现场演示 2：图像生成失败案例（占位）
- 现场演示 3：Veo 短视频生成（占位）

</v-clicks>

---

## 本课总结与课后任务

<v-clicks>

- 总结：LLM 基础、能力圈、边界与关键限制
- 任务：选择一个模型，用 prompt 挑战它的边界并分享结果

</v-clicks>

<!--
演讲者笔记：
- 每页仅 1 个主题，口头扩展细节；穿插 4-6 个演示页。
- 图片/视频后续替换真实素材，当前为占位。
-->



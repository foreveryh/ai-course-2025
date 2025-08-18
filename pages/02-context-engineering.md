---
layout: cover
class: text-left max-w-[56ch] mx-auto leading-10 space-y-6
---

<script setup>
import CustomerServiceTemplateModal from '../components/CustomerServiceTemplateModal.vue'
import CopywritingTemplateModal from '../components/CopywritingTemplateModal.vue'
</script>

# 上下文工程与提示词实战

**90分钟理论与实践结合课程**
从上下文工程原理到提示词实战，建立完整知识体系

<div class="mt-8 space-y-4">

* 🎯 **目标**：深度理解原理 + 掌握**稳定、精准、高效**的提示词技巧
* 👥 **受众**：ChatGPT/Claude/Gemini 等界面用户  
* ⏱️ **时间**：理论深化45分钟 + 实战演练40分钟 + 总结回顾5分钟
* 🔥 **重点**：理论基础 + 实践应用 + 系统思维

</div>

---
layout: section
class: text-center
---

# 开场热身
让我们了解你的现状

---
class: text-left max-w-[60ch] mx-auto leading-8 space-y-6
---

## 🙋‍♀️ 快速调研（举手/发言）

<v-clicks>

* **你最常让 AI 帮你做什么？**  
  <span class="text-sm opacity-75">（写作/翻译/分析/编程/创意...）</span>

* **哪种输出最让你"头疼"？**  
  <span class="text-sm opacity-75">（格式乱/内容偏/太啰嗦/不够深...）</span>

* **你试过调节温度/长度参数吗？**  
  <span class="text-sm opacity-75">（效果如何？）</span>

* **最希望解决的提示词问题是？**  
  <span class="text-sm opacity-75">（我们重点演练这些场景！）</span>

</v-clicks>

<div v-click class="mt-8 p-4 bg-blue-50 rounded-lg border-l-4 border-blue-400">
💡 <strong>目的</strong>：根据大家的反馈调整演练重点，确保解决实际问题
</div>

---
layout: section
class: text-center
---

# Part 1: 为什么需要上下文工程？
理解背后的原理（25分钟）

---
layout: section
class: text-center
---

# 🚨 AI Agent 的现实困境

---
layout: two-cols
layoutClass: gap-8
---

## 📈 表面现象 vs 实际问题

<v-clicks>

### 🎭 "演示完美，实战翻车"

* **展示环节**：ChatGPT 写代码、分析文档、创作内容
* **实际使用**：频繁出错、前后矛盾、半途而废
* **用户困惑**：为什么同样的操作效果差这么多？

### 🔍 真正的症结

**核心观点**：多数 AI Agent 的失败，**不是模型能力本身的失败，而是上下文工程的失败**

</v-clicks>

::right::

<div v-click>

## 🧠 深度剖析：失败的根本原因

### 模型的"无知假设"

* **缺乏关键信息** → 只能进行不确定的假设
* **上下文混乱** → 被无关信息干扰判断  
* **记忆断层** → 无法保持长期一致性

### 当基础模型智能水平显著提升后...

<div class="mt-4 p-3 bg-red-50 rounded border-l-4 border-red-400">
💡 <strong>关键洞察</strong>：模型越聪明，上下文管理就越重要！
</div>

</div>

---
layout: center
class: text-center
---

# 🧠 什么是上下文（Context）？

<div class="mt-8">
<div class="text-2xl font-bold text-primary mb-6">
提供给大型语言模型（LLM）用于完成下一步推理或生成任务的<br>
<span class="text-3xl text-orange-500">全部信息集合</span>
</div>
</div>

<div v-click class="mt-8 text-lg text-gray-600">
不仅仅是聊天记录，而是一个多维、动态且与特定任务相关的系统性概念
</div>

---
layout: two-cols
layoutClass: gap-6
---

## 🎯 指导性上下文 & 📚 信息性上下文

<v-clicks>

### 🎯 指导性上下文 *Instructional Context*

**作用**：告诉模型"做什么"和"怎么做"

**包含**：系统提示词、任务描述、少样本示例、输出格式定义、角色设定

<div class="p-3 bg-blue-50 rounded mt-4">
💡 <strong>提示词工程主要优化这一类</strong>
</div>

### 📚 信息性上下文 *Informational Context*

**作用**：告诉模型"需要知道什么知识"

**包含**：RAG 检索内容、短期/长期记忆、思考本/草稿空间、外部知识库、历史对话记录

<div class="p-3 bg-green-50 rounded mt-4">
🔍 提供解决问题所需的<strong>事实、数据与知识</strong>
</div>

</v-clicks>

::right::

## ⚡ 行动性上下文

<v-clicks>

### ⚡ 行动性上下文 *Actionable Context*

**作用**：告诉模型"能做什么"及"做了之后的结果"

**包含**：
* 工具定义
* API 接口描述
* 工具调用结果
* 环境状态反馈
* 权限边界

<div class="p-3 bg-purple-50 rounded mt-4">
🛠️ 提供与外部世界<strong>交互的能力</strong>
</div>

### 📋 上下文类型小结

<div class="p-3 bg-gray-50 rounded mt-4">
**指导性** → 怎么做<br>
**信息性** → 知道什么<br>  
**行动性** → 能做什么
</div>

</v-clicks>

---
layout: center
class: text-center
---

# 🏗️ 上下文工程的定义

<div class="mt-8 max-w-4xl mx-auto">
<div class="text-xl leading-relaxed">
<span class="text-2xl font-bold text-primary">上下文工程（Context Engineering）</span>
<br><br>
一门系统性学科，专注于设计、构建并维护一个动态系统，<br>
负责为 AI Agent 执行任务的<span class="font-bold text-orange-500">每一步智能地组装出最优的上下文组合</span>，<br>
从而确保任务能够高效完成。
</div>
</div>

<div v-click class="mt-8 p-6 bg-gradient-to-r from-blue-50 to-purple-50 rounded-lg border">
<div class="text-lg font-semibold mb-2">🔄 核心转变</div>
<div class="text-base">
从寻找"完美提示词" → 构建<strong>最高效的信息供给系统</strong>
</div>
</div>

---
layout: image-right
image: /placeholder-memory-manager.png
class: text-left
---

## 💻 内存管理器比喻

<v-clicks>

### 如果把 Agent 视为新型操作系统：

* **模型** = CPU（处理器）
* **上下文窗口** = 内存（RAM）  
* **上下文工程** = 内存管理器

### 内存管理器的职责：

* 🔄 **调度加载**：哪些数据应该被加载到内存
* 🗑️ **换出管理**：哪些数据可以暂时移除
* ⭐ **优先处理**：哪些信息需要优先级处理
* 🎯 **性能保证**：确保系统流畅运行和结果准确性

</v-clicks>

<div v-click class="mt-6 p-4 bg-yellow-50 rounded-lg border-l-4 border-yellow-400">
💡 <strong>关键理解</strong>：上下文工程的复杂性不亚于操作系统的内存管理
</div>

---
layout: section
class: text-center
---

# ⚠️ 上下文管理的两大陷阱

---
layout: two-cols
layoutClass: gap-8
---

## 🕳️ 陷阱一：上下文缺失

<v-clicks>

### 症状表现
* 模型产生幻觉
* 回答不准确或偏离主题
* 忽略重要约束条件
* 前后逻辑不一致

### 典型场景
```md
用户："帮我写个报告"
模型："好的，我来帮您写报告..."
（缺少：什么类型报告？多长？给谁看？格式要求？）
```

### 根本原因
**信息不足 → 模型只能"瞎猜" → 输出质量下降**

</v-clicks>

::right::

## 🌊 陷阱二：上下文过载

<v-clicks>

### 症状表现
* 关键信息被稀释
* 响应时间变长
* Token 成本激增
* 最终导致上下文溢出

### 典型场景
```md
用户：把整个 100 页文档贴给模型
+ 所有历史对话记录
+ 大量无关的背景信息
= 模型被"信息淹没"
```

### 专业术语
**上下文中毒（Context Poisoning）**<br>
**上下文溢出（Context Overflow）**

</v-clicks>

---
class: text-left max-w-[70ch] mx-auto leading-8 space-y-6
---

## ⚖️ 上下文缺乏 vs 过度填充的具体危害

<div class="grid grid-cols-2 gap-8 mt-6">

<div v-click>
<h3>🚨 上下文缺失的危害</h3>

* **性能下降**：准确率显著降低
* **幻觉增加**：编造不存在的信息
* **任务失败**：无法理解真实意图
* **用户挫败感**：反复解释需求

<div class="p-3 bg-red-50 rounded mt-3 text-sm">
<strong>案例</strong>：要求"优化代码"但不提供代码，模型只能给出通用建议
</div>

</div>

<div v-click>
<h3>🌪️ 无差别填充的危害</h3>

* **上下文干扰**：噪声信息混淆判断
* **成本激增**：Token 使用量急剧上升
* **延迟增加**：处理时间显著变长
* **系统崩溃**：超出上下文窗口限制

<div class="p-3 bg-orange-50 rounded mt-3 text-sm">
<strong>案例</strong>：在技术文档查询中包含大量无关的营销材料
</div>

</div>

</div>

<div v-click class="mt-8 p-6 bg-gradient-to-r from-red-50 via-yellow-50 to-green-50 rounded-lg border">
<div class="text-center text-lg font-semibold">
⚡ <strong>核心挑战</strong>：如何在"信息充足"和"信息简洁"之间找到最佳平衡点
</div>
</div>

---
layout: section
class: text-center
---

# 🛠️ 上下文工程的系统性解决方案

---
layout: two-cols
layoutClass: gap-8
---

## 📝 写入 & 🔍 选取策略

<v-clicks>

### 📝 写入 (Writing)
**目标**：持久化重要信息

**策略**：会话内写入思考本、持久化写入记忆系统、结构化信息存储、版本控制管理

**效果**：超越上下文窗口限制，实现知识积累

### 🔍 选取 (Selection) 
**目标**：动态检索相关内容

**策略**：RAG 语义检索、关键词匹配、向量相似度搜索、混合排序融合

**效果**：确保上下文的高信噪比

</v-clicks>

::right::

## 🗜️ 压缩 & 🏗️ 隔离策略

<v-clicks>

### 🗜️ 压缩 (Compression)
**目标**：用更少 Token 承载核心信号

**策略**：自动摘要生成、关键信息提取、层次化压缩、有损/无损压缩

**效果**：容纳更多有效信息

### 🏗️ 隔离 (Isolation)
**目标**：多 Agent 分工协作

**策略**：子任务独立处理、专业化智能体、工具调用封装、沙盒环境隔离

**效果**：减轻主智能体认知负担

<div class="p-3 bg-blue-50 rounded mt-4">
💡 <strong>四大策略构成完整的上下文工程体系</strong>
</div>

</v-clicks>

---
class: text-left max-w-[70ch] mx-auto leading-8 space-y-6
---

## 💡 对普通用户的现实考量

<div v-click class="p-6 bg-blue-50 rounded-lg border-l-4 border-blue-400 mb-6">
<h3 class="text-lg font-semibold mb-3">🎯 明确受众与操作界面</h3>
<p>本课程面向直接使用 <strong>ChatGPT、Claude.ai 等聊天界面</strong>，而非通过 API 进行编程的普通用户</p>
</div>

<div v-click>
<h3 class="text-xl font-semibold mb-4">🚧 普通用户在"上下文工程"操作上的局限性</h3>

<div class="grid grid-cols-2 gap-6">

<div class="space-y-3">

**📝 写入局限**
* 无法直接写入外部记忆系统
* 无法操作向量数据库
* 主要依赖聊天工具内置记忆

**🔍 选取局限**  
* 无法编程实现 RAG 检索
* 无法控制模型驱动选取
* 检索逻辑由平台后端决定

</div>

<div class="space-y-3">

**🗜️ 压缩局限**
* 无法编写自动总结代码
* 无法实现剪枝策略
* 压缩由系统层面自动处理

**🏗️ 隔离局限**
* 无法构建多 Agent 架构
* 无法控制工具调用接口
* 无法设计沙盒环境

</div>

</div>

</div>

<div v-click class="mt-8 p-6 bg-gradient-to-r from-green-50 to-blue-50 rounded-lg border">
<h3 class="text-lg font-semibold mb-2">⚡ 关键结论</h3>
<p class="text-base">这些高级的"上下文工程"策略需要编程能力和系统级控制，超出了普通用户的操作范围</p>
</div>

---
layout: section
class: text-center
---

# 🎯 提示词工程的定位与价值

---
class: text-left max-w-[70ch] mx-auto leading-8 space-y-6
---

## 💡 提示词工程：普通用户的"上下文管理"方式

<div v-click class="p-6 bg-gradient-to-r from-blue-50 to-purple-50 rounded-lg border mb-6">
<h3 class="text-lg font-semibold mb-3">🎯 核心定位</h3>
<p class="text-base">
<strong>提示词工程</strong>是普通用户<strong>最直接、最有效，也是唯一可行的"上下文管理"方式</strong>。它主要在于优化<strong>指导性上下文</strong>，即用户如何通过精心设计的文本输入，最大化地向模型传递意图、信息和期望的输出格式。
</p>
</div>

<div v-click>
<h3 class="text-xl font-semibold mb-4">📋 提示词工程的定义与本质</h3>

**定义**：设计和优化提示，以指导AI模型（特别是LLM）生成所需回答的艺术和科学

**本质**：核心在于**清晰沟通**和**反复迭代**。你的提示词就是你"编程"模型的方式

**工程属性**：体现在**试错与迭代**的持续过程中，如同拥有一个"重启"按钮，能够从零开始不断尝试和设计不同的提示
</div>

<div v-click class="mt-6">
<h3 class="text-xl font-semibold mb-4">🌉 "模拟"上下文工程的核心策略</h3>

虽然普通用户无法直接控制系统级的上下文工程，但可以通过提示词技巧来"模拟"或"引导"：

<div class="grid grid-cols-2 gap-6 mt-4">

<div class="space-y-3">
**📝 模拟"写入"**
* 在对话中明确建立工作空间
* 要求模型"记住"关键信息
* 使用结构化格式组织信息

**🔍 模拟"选取"**  
* 明确指定需要关注的信息源
* 引导模型聚焦相关内容
* 使用问题链条逐步聚焦
</div>

<div class="space-y-3">
**🗜️ 模拟"压缩"**
* 要求模型提供摘要或要点
* 使用分层次的信息组织
* 指定关键信息的优先级

**🏗️ 模拟"隔离"**
* 将复杂任务分解为子步骤
* 使用角色扮演分离不同视角
* 明确任务边界和专注领域
</div>

</div>
</div>

<div v-click class="mt-8 p-6 bg-yellow-50 rounded-lg border-l-4 border-yellow-400">
<h4 class="font-semibold mb-2">🎯 课程聚焦点</h4>
<p>因此，我们将课程重点聚焦于<strong>提示词工程的实用技巧</strong>，帮助大家掌握这种最可行、最直接的AI交互优化方法。</p>
</div>

---
layout: section
class: text-center
---

# Part 2: 提示词工程五大核心技巧
从混乱到精准（40分钟）

---
layout: image-right
image: /placeholder-intent.png
class: text-left
---

## 技巧① 明确任务目标

<v-clicks>

**公式：** 动词 + 对象 + 受众 + 标准

**关键要素：**
* 使用具体动词（生成/改写/分析/提取）
* 明确目标受众和语气
* 设定可验证的评价标准

</v-clicks>

<div v-click class="mt-6">

### 🔄 现场对比演示

</div>

---
layout: two-cols
layoutClass: gap-6
---

## ❌ 模糊版本

```
写点关于新能源车的内容
```

<div class="mt-4 p-3 bg-red-50 rounded border-l-4 border-red-400">
<strong>问题：</strong>
<ul class="text-sm mt-2 space-y-1">
<li>• 任务不明确（写什么？）</li>
<li>• 受众不清楚（给谁看？）</li>
<li>• 标准缺失（多长？什么风格？）</li>
</ul>
</div>

::right::

## ✅ 精准版本

```
请为「非技术背景的潜在车主」撰写一篇 
**600字** 的购车指南，对比**插电混动与纯电**
的差异。

要求：
- 语气：友好专业，避免技术术语
- 结构：开篇吸引 + 核心对比 + 购买建议  
- 必须包含：购车场景2个，成本分析
```

<div class="mt-4 p-3 bg-green-50 rounded border-l-4 border-green-400">
<strong>改进：</strong>
<ul class="text-sm mt-2 space-y-1">
<li>• ✅ 明确任务（购车指南）</li>
<li>• ✅ 锁定受众（非技术车主）</li>
<li>• ✅ 量化标准（600字、2场景）</li>
</ul>
</div>

---
class: text-center
---

## 🎯 技巧① 现场练习

**场景：** 改写下面的模糊提示词

<div class="mt-8 p-6 bg-gray-100 rounded-lg text-left">
<code class="text-lg">"帮我写个产品介绍"</code>
</div>

<div v-click class="mt-6">

**优化方向：**
* 什么产品？给谁看？
* 多长？什么语气？  
* 重点突出什么？

</div>

<div v-click class="mt-6 text-sm opacity-75">
💡 大家可以提出具体产品，我们现场优化演示
</div>

---
layout: image-right
image: /placeholder-context.png
class: text-left
---

## 技巧② 提供充足上下文

<v-clicks>

**核心原则：** 把模型当作"聪明但缺少背景的临时工"

**必备信息：**
* 相关事实和数据
* 特定领域术语定义  
* 约束条件和限制
* 参考资料和来源

</v-clicks>

<div v-click class="mt-6">

### 📝 模板结构

</div>

---
class: text-left max-w-[70ch] mx-auto
---

## 上下文模板

```markdown
### 任务
你将完成：[一句话说明任务]

### 背景信息  
- 关键事实：[列出2-3个核心事实]
- 术语定义：[如 MAU=月活跃用户]
- 限制条件：[必须中文/避免夸大/不超过X字]

### 参考材料
[如果有，直接粘贴相关文档/数据]

### 输出要求
- 格式：[表格/JSON/文章]
- 长度：[具体字数或条目数]  
- 风格：[正式/友好/技术性]
```

<div v-click class="mt-6 p-4 bg-blue-50 rounded-lg">
💡 <strong>现代模型很聪明：</strong>可以直接给它完整论文，无需预先总结！
</div>

---
layout: two-cols
layoutClass: gap-6
---

## 技巧③ 约束输出格式

<v-clicks>

**为什么重要：**
* 确保结果可直接使用
* 避免格式不一致
* 便于后续处理

**常用格式：**
* 结构化文本（标题+要点）
* 表格（Markdown/HTML）
* JSON（API对接）
* 代码块（可执行）

</v-clicks>

::right::

<div v-click>

### 📊 格式示例

**表格输出：**
```markdown
输出Markdown表格，列：
功能 | 目标用户 | 价值 | 注意事项
(各列不超过20字)
```

**JSON输出：**
```json
{
  "title": "标题",
  "summary": "摘要",  
  "key_points": ["要点1", "要点2"],
  "risk_level": "高/中/低"
}
```

</div>

---
class: text-left max-w-[70ch] mx-auto
---

## 技巧④ 少样本示例（Few-shot）

<v-clicks>

**作用：** 2-5个示例，快速对齐格式与风格

**适用场景：**
* 特定格式要求
* 统一语气风格  
* 复杂逻辑判断
* 创意内容生成

</v-clicks>

<div v-click class="mt-8">

### 📋 示例展示

<div class="grid grid-cols-2 gap-6">

<div class="p-4 bg-gray-50 rounded-lg">
<h4 class="font-semibold mb-2">💼 客服分类示例</h4>
<p class="text-sm text-gray-600">用户反馈自动分类</p>
<CustomerServiceTemplateModal />

</div>

<div class="p-4 bg-gray-50 rounded-lg">
<h4 class="font-semibold mb-2">✍️ 文案风格示例</h4>
<p class="text-sm text-gray-600">保持品牌语气一致</p>
<CopywritingTemplateModal />

</div>

</div>

### 💡 Few-shot 应用技巧

* **数量建议**：3-5个示例最佳，太少不够准确，太多占用过多token
* **质量优先**：示例要真实、具体，体现期望的输出质量
* **一致性**：所有示例保持相同的格式和结构

</div>

---
layout: two-cols
layoutClass: gap-6  
---

## 技巧⑤ 链式思维（CoT）

<v-clicks>

**原理：** 让模型"先想后答"

**适用场景：**
* 逻辑推理
* 数学计算
* 方案比较
* 问题诊断

**触发词：**
* "请分步推理"
* "先列出步骤再给结论"  
* "给出依据后再回答"

</v-clicks>

::right::

<div v-click>

### 🧠 CoT 模板

```markdown
在给出最终答案前，请：

1. 分析问题的关键要素
2. 列出3-5步推理过程  
3. 指出信息不足之处
4. 给出结论和建议

若无法确定，请说明需要补充
什么信息。
```

**效果：** 逻辑清晰，错误率降低，便于检查

</div>

---
layout: section  
class: text-center
---

# Part 3: 现场实战演练
解决真实问题（25分钟）

---
class: text-left max-w-[70ch] mx-auto
---

## 🎯 实战场景一：周报改写

**原始需求：** "帮我写周报"

<div class="mt-6 grid grid-cols-2 gap-6">

<div>
<h4>📝 现状材料</h4>
<div class="text-sm bg-gray-100 p-4 rounded">
这周做了很多事情，开了几个会，处理了一些bug，还和用户沟通了需求，总体感觉挺忙的，但好像也没什么特别重要的进展...
</div>
</div>

<div v-click>
<h4>✨ 目标效果</h4>
<div class="text-sm bg-green-50 p-4 rounded border-l-4 border-green-400">
<strong>本周核心成果：</strong>
<br>• 用户需求调研（15个访谈）
<br>• 产品BUG修复（优先级P0: 3个）
<br>• 跨部门协调会议（设计+技术对齐）
<br><strong>下周重点：</strong>
<br>• 需求文档输出
<br>• 技术方案评审
</div>
</div>

</div>

<div v-click class="mt-6">
<strong>现场任务：</strong> 大家一起设计这个提示词！
</div>

---
class: text-left max-w-[70ch] mx-auto
---

## 🧪 实战场景二：信息提取

**原始需求：** "从这篇文章提取重要信息"

<div class="mt-6">

### 📰 输入材料
<div class="text-sm bg-gray-50 p-4 rounded max-h-48 overflow-y-auto">
中国人工智能公司百度宣布，将在2024年第三季度推出其最新的大语言模型"文心一言4.0"。该模型在中文理解和生成能力上较前版本提升了约40%，预计将应用于智能客服、内容创作和教育等领域。公司CEO李彦宏表示，这一技术将帮助企业降低运营成本约30%。目前已有超过1000家企业表达了合作意向...
</div>

### 🎯 期望输出格式
<v-click>

| 公司 | 产品 | 发布时间 | 核心改进 | 应用领域 | 商业价值 |
|------|------|----------|----------|----------|----------|
| ? | ? | ? | ? | ? | ? |

</v-click>

</div>

<div v-click class="mt-6">
<strong>现场任务：</strong> 设计提取表格的提示词
</div>

---
class: text-left max-w-[70ch] mx-auto
---

## 🔧 实战场景三：提示词诊断

**问题提示词：** 
```
写一个创业计划书
```

<div class="mt-6">

### 🚨 问题诊断
<v-clicks>

* **目标不明确** → 什么行业？多详细？
* **受众不清楚** → 给投资人？给合伙人？  
* **标准缺失** → 多长？什么格式？
* **背景不足** → 创业者背景？市场情况？

</v-clicks>

### 💊 修复策略

<div v-click class="mt-4 p-4 bg-blue-50 rounded-lg">

**现场任务：** 
1. 选择一个具体行业（大家投票）
2. 集体优化这个提示词
3. 对比修复前后的输出效果

</div>

</div>

---
layout: two-cols
layoutClass: gap-8
---

## 🛠️ 常见问题速修指南

<v-clicks>

**问题类型 → 解决方案**

* 输出太长 → 加字数限制+要点式
* 格式混乱 → 指定结构+示例
* 内容空泛 → 要求具体数据+案例  
* 风格不稳 → 角色设定+参考示例
* 经常幻觉 → 加"不确定条款"
* 理解偏差 → 补充背景+术语定义

</v-clicks>

::right::

<div v-click>

## ⚙️ 参数调节技巧

**温度设置：**
* **0-0.3** → 事实性任务（翻译、提取）
* **0.7-1.0** → 创意任务（写作、头脑风暴）

**长度控制：**
* 设定具体数字而非"简洁点"
* 使用"不超过X字"而非"尽量短"

**停止条件：**
* "完成以上3项即停止"
* "不要添加额外延伸"

</div>

---
layout: section
class: text-center
---

# 🧠 理论回顾与深度思考

---
class: text-left max-w-[70ch] mx-auto leading-8 space-y-6
---

## 💭 从理论到实践的连贯思考

<div v-click class="p-6 bg-gradient-to-r from-purple-50 to-blue-50 rounded-lg border mb-6">
<h3 class="text-lg font-semibold mb-3">🔄 知识体系整合</h3>

**上下文工程理论** → **提示词工程实践** → **具体技巧应用**

* **理论基础**：理解AI Agent失败的根本原因（上下文管理失败）
* **实践方法**：掌握普通用户可操作的优化手段（提示词工程）  
* **技巧应用**：五大核心技巧的具体运用和迭代优化
</div>

<div v-click>
<h3 class="text-xl font-semibold mb-4">🎯 提示词工程的深层价值</h3>

### 认知科学视角

**人机交互本质**：提示词工程是**"如何与高智能但缺乏特定上下文的系统进行有效沟通"**的学科

**关键洞察**：
* 把模型想象成**非常聪明但缺乏你当前任务上下文的临时工**
* 清晰的指令 = 高效的协作 = 更好的结果
* 迭代优化体现了工程思维的核心价值
</div>

<div v-click class="mt-6">
<h3 class="text-xl font-semibold mb-4">📈 技术发展与未来趋势</h3>

### 当前阶段的特点
* **模型能力快速提升** → 对"婴儿式"提示需求减少
* **上下文窗口扩大** → 更复杂的信息管理需求
* **多模态能力增强** → 跨模态的上下文工程挑战

### 未来发展方向
<div class="grid grid-cols-2 gap-6 mt-4">

<div class="space-y-3">
**🤖 AI辅助提示词工程**
* 模型帮助优化提示词
* 自动生成针对性模板
* 智能诊断提示词问题
</div>

<div class="space-y-3">
**🔄 交互模式演进**
* 模型主动提问澄清意图
* 从"指导者-被指导者"到"客户-专家"
* 动态上下文组装系统
</div>

</div>
</div>

<div v-click class="mt-8 p-6 bg-green-50 rounded-lg border-l-4 border-green-400">
<h4 class="font-semibold mb-2">🌟 核心启发</h4>
<p>
<strong>提示词工程不仅是技巧</strong>，更是一种<strong>内省能力的培养</strong>：<br>
学会反思自己真正想要什么，并将复杂想法清晰地外部化给一个高能力但缺乏特定上下文的系统。
</p>
</div>

---
layout: section
class: text-center
---

# Part 4: 核心模板与速查清单
拿来即用的工具包（5分钟）

---
class: text-left max-w-[80ch] mx-auto text-sm
---

## 📋 万能提示词模板

```markdown
### 角色与任务
你是[具体角色]，需要为[目标受众]完成[具体任务]。

### 背景信息
- 关键事实：[2-3个核心信息]
- 术语定义：[专业词汇解释]  
- 约束条件：[必须/禁止做什么]

### 输出要求
- 格式：[表格/JSON/分段文章]
- 长度：[具体字数或条目数]
- 风格：[正式/友好/技术性]
- 必须包含：[关键元素清单]

### 质量控制
- 不确定时请说"不知道"并列出信息缺口
- 给出结论前请简述推理依据
- 按[具体结构]组织输出，不要添加额外内容

### 示例参考
[如果需要，提供1-2个标准示例]
```

---
layout: two-cols
layoutClass: gap-6
---

## ⚡ 速查清单

**提示词检查表：**

<v-clicks>

- [ ] 任务目标明确具体？
- [ ] 目标受众和语气确定？  
- [ ] 输出格式清晰可验证？
- [ ] 提供了必要背景信息？
- [ ] 包含示例或参考？
- [ ] 设置了"不确定"出口？
- [ ] 避免了否定性指令？

</v-clicks>

::right::

<div v-click>

## 🔥 救急模板库

**A. 文档改写**
```markdown
将下文改写为[目标风格]，保持信息完整，
句长≤20字：[原文]
```

**B. 信息提取** 
```markdown
从材料中提取并输出表格：
字段1|字段2|字段3
无法确定的填"未知"：[材料]
```

**C. 分析决策**
```markdown
对比方案A/B，维度：成本/时间/风险，
最后给出推荐理由：[背景材料]
```

</div>

---
layout: center
class: text-center
---

# 🎉 课程总结与展望

<div class="space-y-8 mt-8">

<div v-click>

## 🎯 理论层次收获
* **深度理解**：AI Agent 失败的根本原因（上下文管理失败）
* **系统认知**：上下文工程的四大核心策略（写入/选取/压缩/隔离）
* **实用定位**：提示词工程是普通用户最可行的上下文管理方式

</div>

<div v-click>

## 🛠️ 实践技巧掌握
**五大核心技巧：** 明确目标 → 充足上下文 → 格式约束 → 少样本示例 → 链式思维
<br>**工程思维：** 清晰沟通 + 持续迭代 + 系统性优化

</div>

<div v-click>

## 🚀 未来发展意识
* **技术趋势**：AI辅助提示词工程、模型主动澄清、动态上下文组装
* **能力演进**：从"寻找完美提示词"到"构建智能信息供给系统"
* **深层价值**：内省能力的培养，清晰外化复杂想法的能力

</div>

<div v-click>

## 📚 持续学习路径
* **理论深化**：关注上下文工程、多智能体系统发展
* **实践迭代**：在日常工作中持续优化提示词，积累经验
* **技术跟进**：关注最新模型能力，调整交互策略

</div>

<div v-click>

## 📝 课后实践任务
1. **选择具体场景**：工作中的重复性AI交互任务
2. **应用五大技巧**：系统性改进现有提示词
3. **记录对比效果**：优化前后的输出质量差异
4. **反思与迭代**：总结适合自己工作的提示词模式

</div>

<div v-click>

## 🔗 持续改进
提示词是"产品"，需要像产品一样打磨优化

</div>

</div>

---
layout: end
class: text-center
---

# 感谢参与！

## 🔗 延伸资源

* **课件文件：** 可下载打印速查清单
* **模板库：** 所有示例代码可直接复制使用  
* **讨论群：** 后续问题欢迎继续交流

<div class="mt-8 text-lg font-semibold">
下节课预告：<strong>AI工具链整合与实战项目</strong>
</div>
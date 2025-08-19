---
layout: cover
class: text-left max-w-[56ch] mx-auto leading-10 space-y-6
---

<script setup>
import CustomerServiceTemplateModal from '../components/CustomerServiceTemplateModal.vue'
import CopywritingTemplateModal from '../components/CopywritingTemplateModal.vue'
import ContextStrategies from '../components/ContextStrategies.vue'
import PromptingPracticeModal from '../components/PromptingPracticeModal.vue'
import CoTExampleModal from '../components/CoTExampleModal.vue'
import NegativeConstraintsModal from '../components/NegativeConstraintsModal.vue'
import ModalDetails from '../components/ModalDetails.vue'
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

# 🚨 当前 AI Agent 的现实困境

---
layout: two-cols
layoutClass: gap-8
class: text-left max-w-[60ch] mx-auto leading-8 space-y-8
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
layout: section
class: text-center
---

# 🧠 三类上下文深度解析

---
layout: two-cols
layoutClass: gap-8
class: text-left
---

## 🎯 指导性上下文 *Instructional Context*

<v-clicks>

**作用**：告诉模型"做什么"和"怎么做"

**包含**：
* 系统提示词
* 任务描述与指令
* 少样本示例
* 输出格式定义
* 角色设定与人格指令

<div class="p-4 bg-blue-50 rounded-lg border-l-4 border-blue-400 mt-6">
💡 <strong>核心要点</strong>：提示词工程主要聚焦于优化这一类上下文，通过指令设计提升输出质量
</div>

</v-clicks>

::right::

<div class="pt-10">

<v-clicks>

## 常见应用场景

* 精细的指令设计（如"分步分析"）
* 角色扮演与人格定制
* 输出格式化控制
* 任务拆解与顺序指导
* 链式思维引导
* 约束与限制设置
* 示例驱动学习

<div class="p-3 bg-blue-100 rounded mt-4 text-sm">
<strong>优化示例</strong>：将"编写报告"改为"以专业金融分析师的角色，用STAR法则分析Q2财报，输出表格+500字总结"
</div>

</v-clicks>

</div>

---
layout: two-cols
layoutClass: gap-8
class: text-left
---

## 📚 信息性上下文 *Informational Context*

<v-clicks>

**作用**：告诉模型"需要知道什么知识"

**包含**：
* RAG 检索内容
* 短期/长期记忆系统
* 思考本/草稿空间
* 外部知识库集成
* 历史对话记录与摘要

<div class="p-4 bg-green-50 rounded-lg border-l-4 border-green-400 mt-6">
🔍 <strong>核心要点</strong>：提供解决问题所需的<strong>事实、数据与知识</strong>，是克服模型幻觉的关键
</div>

</v-clicks>

::right::

<div class="pt-10">

<v-clicks>

## 常见应用场景

* 文档检索增强生成（RAG）
* 向量数据库存储与检索
* 长期记忆管理系统
* 会话上下文管理
* 专业知识库集成
* 语义缓存技术
* 多模态信息融合

<div class="p-3 bg-green-100 rounded mt-4 text-sm">
<strong>优化示例</strong>：从"回答关于产品的问题"到"基于最新2023版产品手册PDF和客户反馈数据库回答产品性能对比问题"
</div>

</v-clicks>

</div>

---
layout: two-cols
layoutClass: gap-8
class: text-left
---

## ⚡ 行动性上下文 *Actionable Context*

<v-clicks>

**作用**：告诉模型"能做什么"及"做了之后的结果"

**包含**：
* 工具定义与描述
* API 接口文档
* 工具调用结果
* 环境状态反馈
* 权限边界描述

<div class="p-4 bg-purple-50 rounded-lg border-l-4 border-purple-400 mt-6">
🛠️ <strong>核心要点</strong>：提供与外部世界<strong>交互的能力</strong>，使模型从"思考者"变为"行动者"
</div>

</v-clicks>

::right::

<div class="pt-10">

<v-clicks>

## 常见应用场景

* 函数调用系统
* 插件与工具集成
* Agent行为体系设计
* 环境交互控制
* 反馈循环机制
* 资源访问管理
* 工具链编排

<div class="p-3 bg-purple-100 rounded mt-4 text-sm">
<strong>优化示例</strong>：从"查询航班信息"到"授权调用航班API，获取实时价格，比较多家平台，并发送提醒邮件"
</div>

</v-clicks>

</div>

---
layout: two-cols
layoutClass: gap-8
class: text-left
---

## 📋 三类上下文综合分析

<v-clicks>

**整体框架**：

<div class="p-4 bg-gray-50 rounded-lg border mt-4 text-center">
<span class="font-bold text-blue-600">指导性</span> → 怎么做<br>
<span class="font-bold text-green-600">信息性</span> → 知道什么<br>  
<span class="font-bold text-purple-600">行动性</span> → 能做什么
</div>

**组合优势**：
* 三类上下文相互补充，缺一不可
* 不同任务对三种上下文的需求比例不同
* 高级应用需要综合协调三类上下文

</v-clicks>

::right::

<div class="pt-10">

<v-clicks>

## 应用与管理策略

**管理难度对比**：
* 指导性：较易（用户可直接编写）
* 信息性：中等（需要检索与存储系统）
* 行动性：较难（需要系统集成与安全控制）

**任务类型与上下文需求**：
* 创意生成 → 重指导性，轻信息性
* 事实分析 → 重信息性，中指导性
* 工具使用 → 重行动性，中指导性
* 复杂推理 → 三者均衡配置

<div class="p-3 bg-gray-100 rounded mt-4 text-sm">
<strong>最佳实践</strong>：不同任务调整三类上下文的配比，而非仅优化单一类型
</div>

</v-clicks>

</div>

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
image: /memory_management.webp
backgroundSize: contain
class: text-left max-w-[70ch] mx-auto leading-8
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
class: text-left max-w-[70ch] mx-auto leading-8 space-y-4
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

---
class: text-left max-w-[70ch] mx-auto leading-8 space-y-6
---

## 🌉 "模拟"上下文工程的核心策略

<div v-click>
<p class="mb-4">
虽然普通用户无法直接控制系统级的上下文工程，但可以通过提示词技巧来"模拟"或"引导"：
</p>

<ContextStrategies />
</div>

<div v-click class="mt-8 p-6 bg-yellow-50 rounded-lg border-l-4 border-yellow-400">
<h4 class="font-semibold mb-2">🎯 课程聚焦点</h4>
<p>因此，我们将课程重点聚焦于<strong>提示词工程的实用技巧</strong>，帮助大家掌握这种最可行、最直接的AI交互优化方法。</p>
</div>

---
layout: section
class: text-center
---

# Part 2: 提示词工程八大核心技巧
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

<div class="mt-4 p-3 bg-orange-50 rounded border-l-4 border-orange-400">
<strong>🤔 思维陷阱：</strong>总觉得AI“应该懂我意思”，从而使用模糊、口语化的指令。
</div>

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
<li>任务不明确（写什么？）</li>
<li>受众不清楚（给谁看？）</li>
<li>标准缺失（多长？什么风格？）</li>
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
<li>✅ 明确任务（购车指南）</li>
<li>✅ 锁定受众（非技术车主）</li>
<li>✅ 量化标准（600字、2场景）</li>
</ul>
</div>

---
layout: center
class: text-center
---

## 🎯 技巧① 现场练习

<div class="max-w-3xl mx-auto mt-8">
  <div class="text-left mb-6">
    <h3 class="text-xl text-blue-600">案例分析</h3>
    <div class="flex items-center gap-4 mt-4">
      <div class="bg-gray-100 p-3 rounded-lg flex-1">
        <p class="text-lg font-medium">"帮我写个产品介绍"</p>
      </div>
      <div class="text-2xl font-bold text-red-400">→</div>
      <div class="bg-green-50 p-3 rounded-lg flex-1">
        <p class="text-lg font-medium">优化提示词</p>
      </div>
    </div>
  </div>
  
  <div v-click class="text-left">
    <h3 class="text-lg mb-3">要素缺失分析</h3>
    <div class="grid grid-cols-3 gap-4">
      <div class="bg-red-50 p-3 rounded">产品细节缺失</div>
      <div class="bg-orange-50 p-3 rounded">受众信息缺失</div>
      <div class="bg-amber-50 p-3 rounded">输出规格缺失</div>
    </div>
  </div>
  
  <div v-click class="mt-8 flex flex-col items-center">
    <p class="mb-3">查看完整优化示例与提示词公式</p>
    <PromptingPracticeModal />
    <div class="text-sm text-gray-500 mt-6">
      课堂互动：请学员提出产品，讲师引导大家共同优化提示词（约5分钟）
    </div>
  </div>
</div>

---
layout: two-cols
layoutClass: gap-6
---

## 技巧② 提供充足上下文

<v-clicks>

**核心原则：** 把模型当作"聪明但缺少背景的临时工"

**必备信息：**
* 相关事实和数据
* 特定领域术语定义  
* 约束条件和限制
* 参考资料和来源

<div class="mt-6">

### 📝 高级提示

<div class="p-3 bg-blue-50 rounded">
💡 <strong>现代模型很聪明：</strong>可以直接给它完整论文，无需预先总结！
</div>
</div>

</v-clicks>

::right::

<div v-click>

## 上下文模板示例

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

<div class="mt-6 p-3 bg-gradient-to-r from-green-50 to-blue-50 rounded-lg border">
使用场景示例： 产品分析、市场调研报告、学术论文摘要、数据解读等信息密集型任务
</div>

<div class="mt-4 p-3 bg-orange-50 rounded border-l-4 border-orange-400">
<strong>🤔 思维陷阱：</strong>要么给得太少，让AI猜；要么给得太多，把所有东西一股脑全丢进去，造成信息干扰。
</div>

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
<div class="mt-4 p-3 bg-orange-50 rounded border-l-4 border-orange-400">
<strong>🤔 思维陷阱：</strong>满足于默认的非结构化输出，花费大量时间手动整理，而没有让AI直接生成“即用型”格式。
</div>
</div>

---
layout: two-cols
layoutClass: gap-6
---

## 技巧④ 少样本示例（Few-shot）

<v-clicks>

**作用：** 2-5个示例，快速对齐格式与风格

**适用场景：**
* 特定格式要求
* 统一语气风格  
* 复杂逻辑判断
* 创意内容生成

<div class="mt-4 p-3 bg-blue-50 rounded border-l-4 border-blue-400">
<strong>🔑 核心原理：</strong>"身教重于言教"，通过示范而非指令达成一致
</div>

</v-clicks>

::right::

<div v-click>

### 📋 示例展示

<div class="space-y-4">
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

</div>

---
layout: center
---

## 技巧④ 少样本示例（Few-shot）实践要点

<div class="mt-6 space-y-5">

**数量建议：** 3-5个示例最佳平衡
- 太少不足以确保准确性
- 太多会浪费token且效率不高

**质量优先：** 示例必须真实、具体
- 准确反映期望的输出质量
- 示例应与实际任务紧密相关

**保持一致：** 所有示例应保持格式一致
- 使用相同的结构和表达方式
- 避免混合不同风格的示例

<div v-click class="p-3 bg-yellow-50 rounded-lg border-l-4 border-yellow-400 mt-4">
<strong>💡 最佳实践：</strong> 从简单到复杂排序示例，先基础情况再边缘情况
</div>

<div v-click class="p-3 bg-red-50 rounded-lg border-l-4 border-red-400 mt-2">
<strong>🤔 常见陷阱：</strong> 过度依赖指令而不是示例；或使用质量差的示例导致混淆
</div>

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

<div class="mt-4 mb-4">
<CoTExampleModal />
</div>

<div class="p-3 bg-orange-50 rounded border-l-4 border-orange-400">
<strong>🤔 思维陷阱：</strong>对于简单任务也过度使用CoT，增加了不必要的延迟和成本。
</div>
</div>

---
layout: two-cols
layoutClass: gap-8
class: text-left
---

## 技巧⑥ 设定模型角色

<v-clicks>

**定义：** 为模型分配特定角色或身份，引导其生成特定风格和专业度的内容

**关键优势：**
* 输出语气和视角一致
* 提供特定领域专业知识
* 增强回答的针对性

**优秀实践：**
* 选择与任务相关的角色
* 提供角色的背景和特征
* "诚实"设定（直接告诉模型真实目的）

</v-clicks>

::right::

<div v-click>

### 📝 角色设定示例

**产品经理角色：**
```markdown
你是一名拥有10年经验的产品经理，
专注于B端SaaS产品设计。你擅长
将复杂功能简化为用户友好的体验。
```

**营销专家角色：**
```markdown
你是一位资深数字营销专家，专门
帮助中小企业制定获客策略。你的
回答务实、数据驱动，避免空泛理论。
```

**技术顾问角色：**
```markdown
你是一名云架构师，有8年AWS经验。
请用简洁的技术语言解释概念，
并提供具体的实施建议。
```

<div class="mt-4 p-3 bg-orange-50 rounded border-l-4 border-orange-400">
<strong>🤔 思维陷阱：</strong>设定的角色过于宽泛，如"你是一个助手"，导致效果不佳。
</div>

</div>

---
layout: two-cols
layoutClass: gap-8
---

## 技巧⑦ 正面指令优于负面约束

<v-clicks>

**核心理念：** 告诉模型"做什么"，而非"不要做什么"

**原因：**
* 负面指令可能引起反效果
* 正面指令更明确具体
* 提供明确替代方案更有效

**示例对比：**

❌ 不要使用复杂术语和长句

✅ 使用简单日常用语和短句，确保12岁孩子也能理解

</v-clicks>

<div v-click class="mt-6">
<NegativeConstraintsModal />
</div>

::right::

<div v-click>

### 🔄 指令改写示例

**安全类指令：**

❌ 不要询问用户个人敏感信息
✅ 引导用户访问官方安全渠道：`help.example.com/verify`

**风格类指令：**

❌ 不要啰嗦，不要解释太多
✅ 保持简洁，每个要点不超过20字

**内容类指令：**

❌ 不要使用英文缩写
✅ 使用完整的中文术语表达，必要时附加英文全称

<div class="mt-4 p-3 bg-orange-50 rounded border-l-4 border-orange-400">
<strong>🤔 思维陷阱：</strong>在禁止模型做某事后，没有提供清晰的替代方案，导致模型输出受限或行为混乱。
</div>
</div>

---
layout: two-cols
class: text-left
---

## 技巧⑧ 迭代优化提示词

<v-clicks>

**核心方法：** 反复试验和调整，直到达到理想输出

**关键步骤：**
* 仔细阅读模型的完整输出
* 向模型询问改进建议
* 尝试不同的表述方式
* 调整参数（温度、上下文等）
* 测试边缘情况和异常输入

</v-clicks>

::right::

<div v-click>

### 💡 高效迭代技巧

**自我诊断问题：**
```markdown
我的提示词哪里可以改进？请分析并
给出3个具体修改建议，以获得更准确
的结果。
```

**向模型求助：**
```markdown
请帮我优化这个提示词，使其更清晰、
具体且易于理解。
```

<div class="mt-4 p-3 bg-orange-50 rounded border-l-4 border-orange-400">
<strong>🤔 思维陷阱：</strong>满足于"差不多"的结果，不愿意花时间进行微调和迭代，从而错失了获得高质量输出的机会。
</div>

</div>

---
layout: two-cols
class: text-left
---

# 🎉 本课总结

<div class="space-y-6">

<div v-click>

## 🎯 理论层次收获
* **深度理解**：什么是上下文工程
* **系统认知**：上下文工程的四大核心策略（写入/选取/压缩/隔离）
* **实用定位**：提示词工程是普通用户最可行的上下文管理方式

</div>

<div v-click>

## 🛠️ 实践技巧掌握
**八大核心技巧：**
1. 明确清晰目标
2. 提供充足上下文
3. 设置格式约束
4. 使用少样本示例
5. 链式思维推理
6. 设定模型角色
7. 正面指令优化
8. 迭代优化提示词

**工程思维：** 清晰沟通 + 持续迭代 + 系统性优化

</div>

</div>

::right::

<div class="space-y-6">

<div v-click>

## 🚀 未来发展意识
* **技术趋势**：AI辅助提示词工程、模型主动澄清、动态上下文组装
* **能力演进**：从"寻找完美提示词"到"构建智能信息供给系统"
* **深层价值**：内省能力的培养，清晰外化复杂想法的能力

</div>

<div v-click>

## 📚 持续学习与实践
* **实践出真知**：理论理解只是开始，真正掌握需要持续实践
* **边用边学**：每次与AI互动都是一次学习机会
* **记录经验**：建立个人提示词模板库，持续改进
* **分享交流**：小组内展示优化后的结果，讨论改进方法

</div>

</div>
---
layout: cover
class: text-left max-w-[56ch] mx-auto leading-10 space-y-6
---

# 上下文工程与提示词实战

**90分钟实用导向课程**
从理论到实践，让你今天就能写出更好的提示词

<div class="mt-8 space-y-4">

* 🎯 **目标**：掌握**稳定、精准、高效**的提示词技巧
* 👥 **受众**：ChatGPT/Claude/Gemini 等界面用户  
* ⏱️ **时间**：理论35分钟 + 实战50分钟 + 总结5分钟
* 🔥 **重点**：现场演练 > 理论讲解

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
理解背后的原理（10分钟）

---
layout: two-cols
layoutClass: gap-8
---

## 🤖 AI Agent 的尴尬现状

<v-clicks>

* **看起来很先进** → 实际经常"掉链子"
* **演示效果很好** → 生产环境频繁失败  
* **理论能力很强** → 复杂任务半途而废

**核心问题：** 不是模型不够聪明，而是**上下文工程失败**

</v-clicks>

::right::

<div v-click>

## 🧠 什么是上下文（Context）？

**定义：** 提供给模型用于推理的全部信息集合

**三大类别：**
* **🎯 指导性**：告诉模型怎么做（提示词）
* **📚 信息性**：告诉模型需要知道什么（RAG/记忆）  
* **⚡ 行动性**：告诉模型能做什么（工具调用）

</div>

---
class: text-left max-w-[70ch] mx-auto leading-8 space-y-6
---

## 💡 上下文工程 = 智能内存管理

<div class="grid grid-cols-2 gap-8 mt-6">

<div v-click>
<h3>🚨 常见问题</h3>

* **上下文缺失** → 模型瞎猜 + 幻觉
* **信息过载** → 关键信息被稀释  
* **成本暴涨** → Token 数量失控
* **上下文溢出** → 系统直接崩溃

</div>

<div v-click>
<h3>✅ 工程化解决</h3>

* **写入** → 持久化重要信息
* **选取** → 动态检索相关内容
* **压缩** → 用更少Token承载核心信号
* **隔离** → 多Agent分工协作

</div>

</div>

<div v-click class="mt-8 p-4 bg-yellow-50 rounded-lg border-l-4 border-yellow-400">
⚡ <strong>对普通用户：</strong>我们无法控制"写入/选取/压缩/隔离"，但可以通过<strong>提示词工程</strong>优化指导性上下文！
</div>

---
layout: section
class: text-center
---

# Part 2: 提示词工程五大核心技巧
从混乱到精准（45分钟）

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

### 📋 示例模板

<div v-click>

```markdown
### 指令
请依照示例风格完成新样本

### 示例
[输入] 用户投诉：App经常崩溃，影响工作
[输出] 类型：技术问题 | 优先级：高 | 回复：感谢反馈，我们将在24小时内修复...

[输入] 用户建议：希望增加夜间模式
[输出] 类型：功能建议 | 优先级：中 | 回复：好建议！已记录到产品规划...

### 现在开始  
[输入] {{你的新输入}}
```

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

# 🎉 课程总结

<div class="space-y-6 mt-8">

<div v-click>

## 🎯 核心收获
**五大技巧：** 明确目标 + 充足上下文 + 格式约束 + 少样本示例 + 链式思维

</div>

<div v-click>

## 💡 关键理念
提示词工程 = **清晰沟通** + **持续迭代**

</div>

<div v-click>

## 📝 课后作业
选择1个日常场景，用今天的技巧改进提示词，记录前后对比效果

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
---
layout: cover
class: text-center
transition: slide-left
---
# 深入理解 AI Agent
让你的AI更"聪明"地思考和行动

<div class="mt-12">
  <div class="text-6xl mb-8">🤖</div>
  <div class="text-2xl text-gray-600 mb-8">
    第四课 · AI Agent 架构与实战
  </div>
</div>

<div class="absolute bottom-10 left-0 right-0">
  <div @click="$slidev.nav.next" class="inline-flex items-center gap-2 px-6 py-3 rounded-full bg-primary/10 hover:bg-primary/20 transition-colors cursor-pointer">
    <span class="text-lg">开始学习</span>
    <carbon:arrow-right class="text-xl" />
  </div>
  
  <p class="mt-4 text-sm text-gray-500">
    按 <kbd class="px-2 py-1 rounded bg-gray-200">空格</kbd> 或点击继续
  </p>
</div>

<!--
演讲者笔记：
- 欢迎学员进入第四课
- 简单介绍今天的主题：AI Agent
- 营造学习氛围
-->

---
layout: center
class: text-left max-w-[56ch] mx-auto leading-10 space-y-6
---
<script setup>
// Import components for interactive demonstrations
import AgentDemo from '../components/AgentDemo.vue'
import ReActExample from '../components/ReActExample.vue'
import GeminiAgentModal from '../components/GeminiAgentModal.vue'
</script>

# 课程概览

**90分钟理论与实战结合课程**
从基础概念到 ReAct 模式，再到 Gemini 实际演示

<div class="mt-8 space-y-4">

* 🎯 **目标**：深度理解 AI Agent 原理 + 掌握**ReAct 思维模式**的实际应用
* 👥 **受众**：想要构建智能应用的开发者和产品人  
* ⏱️ **时间**：理论基础45分钟 + Gemini实战40分钟 + 总结回顾5分钟
* 🔥 **重点**：概念厘清 + 模式理解 + 实际操作

</div>

---
layout: section
class: text-center
---
# 开场热身
让我们了解你对 AI Agent 的认知

---
class: text-left max-w-[60ch] mx-auto leading-8 space-y-6
---
## 🙋‍♀️ 快速调研（举手/发言）

<v-clicks>

* **什么是 AI Agent？**  
  <span class="text-sm opacity-75">（请用自己的理解简单描述）</span>

* **相比原生 LLM 的推理，Agent 能带来了哪些能力？**  
  <span class="text-sm opacity-75">（想想 ChatGPT 和智能助手的区别）</span>

* **为什么 Agent 需要具备这些能力？**  
  <span class="text-sm opacity-75">（从实际应用场景考虑）</span>

* **你最希望 AI Agent 帮你解决什么问题？**  
  <span class="text-sm opacity-75">（工作中的具体痛点或需求）</span>

</v-clicks>

<div v-click class="mt-8 p-4 bg-blue-50 rounded-lg border-l-4 border-blue-400">
💡 <strong>目的</strong>：建立对 AI Agent 的直观认知，为深入学习做准备
</div>

---
layout: section
class: text-center
---
# Part 1: AI Agent 的本质
从概念到架构的全面解析（30分钟）

---
layout: two-cols
layoutClass: gap-6
class: text-left leading-7
---
## 🤔 引言：ChatGPT 很强大，但它有什么"局限"？

<v-clicks>

### ✅ LLM 的强大能力
LLM 能理解人类语言，生成文本，回答问题，进行复杂的逻辑推理

### ⚠️ LLM 的核心局限
LLM 是一个 <span v-mark.underline.orange>"被动的推理引擎"</span>

无法：
- **感知外部环境**：不知道电脑文件，看不到网页内容
- **改变外部环境**：无法执行命令、保存文件、点击按钮

</v-clicks>

::right::

<div v-click>

### 🧠 形象类比

<div class="space-y-4">
  <div class="p-4 bg-gray-50 rounded-lg border">
    <div class="text-center mb-3">
      <div class="text-4xl mb-2">🧠</div>
      <div class="font-semibold text-gray-700">传统 LLM</div>
    </div>
    <div class="space-y-2 text-sm">
      <div class="flex items-center gap-2">
        <span class="text-green-500">✅</span>
        <span>强大的"大脑"</span>
      </div>
      <div class="flex items-center gap-2">
        <span class="text-red-500">❌</span>
        <span>缺少"感官"</span>
      </div>
      <div class="flex items-center gap-2">
        <span class="text-red-500">❌</span>
        <span>缺少"四肢"</span>
      </div>
    </div>
  </div>
  <div class="p-4 bg-blue-50 rounded-lg border border-blue-200">
    <div class="text-center mb-3">
      <div class="text-4xl mb-2">🤖</div>
      <div class="font-semibold text-blue-700">AI Agent</div>
    </div>
    <div class="space-y-2 text-sm">
      <div class="flex items-center gap-2">
        <span class="text-green-500">✅</span>
        <span>智能"大脑"</span>
      </div>
      <div class="flex items-center gap-2">
        <span class="text-green-500">✅</span>
        <span>配备"感官"</span>
      </div>
      <div class="flex items-center gap-2">
        <span class="text-green-500">✅</span>
        <span>拥有"四肢"</span>
      </div>
    </div>
  </div>
</div>

</div>

<blockquote v-click class="mt-6 p-3 bg-gradient-to-r from-blue-50 to-green-50 rounded border-l-4 border-blue-400 text-sm">
<strong>这就是为什么我们需要 AI Agent</strong> —— 给 AI 装上"感官"和"四肢"！
</blockquote>

<!--
演讲者笔记：
- 先让学员认识到现有AI的局限性
- 用生动的比喻帮助理解
- 为引入Agent概念做铺垫
-->

---
layout: section
class: text-center
---
# 那么，什么是 AI Agent？

---
layout: two-cols
layoutClass: gap-8
class: text-left max-w-[60ch] mx-auto leading-8 space-y-6
---
## 🤖 什么是 AI Agent？

<v-clicks>

### 📖 定义解析

**AI Agent = 能够感知环境、做出决策、执行行动的智能体**

- **感知（Perception）**：理解输入信息和当前状态
- **决策（Decision）**：基于目标和策略进行推理
- **行动（Action）**：执行具体操作并产生结果

### 🧠 核心特征

1. **自主性**：能独立完成任务，不需要每步指导
2. **目标导向**：明确知道要达成什么目标
3. **环境感知**：能理解和适应变化的环境
4. **学习能力**：从经验中改进表现

</v-clicks>

::right::

<div v-click>

## 🔍 Agent vs LLM的区别

### 基础 LLM 
- **被动响应**：等待用户输入
- **单轮交互**：一问一答模式
- **无状态**：不记住历史context
- **工具依赖**：需要人工调用外部工具

### AI Agent
- **主动思考**：会分析问题并制定计划
- **多轮推理**：能进行复杂的思维链
- **状态管理**：保持记忆和上下文
- **工具集成**：自主选择和使用工具

</div>

---
layout: center
class: text-center
---
<div class="mt-8">
  <div class="flex justify-center">
    <img src="/Agent.png" alt="LLM-Powered Autonomous Agent System Overview by Lilian Weng" class="max-w-4xl w-full h-auto rounded-lg shadow-lg" />
  </div>
</div>

<div v-click class="mt-6 text-center">
  <div class="text-lg text-gray-600 mb-2">LLM 驱动下的 AI Agents System 概览</div>
  <div class="text-sm text-gray-500">Lilian Weng - OpenAI 研究科学家提出的经典架构图</div>
</div>

<div v-click class="mt-4 p-4 bg-blue-50 rounded-lg max-w-3xl mx-auto border-l-4 border-blue-400">
  <p class="text-sm text-gray-700">
    💡 <strong>核心洞察</strong>：这是 AI Agent 领域最具影响力的架构图之一，清晰展示了 Planning、Memory 和 Tool Use 三大核心模块如何围绕 LLM 协同工作
  </p>
</div>

---
layout: center
class: text-center
---
# 🏗️ AI Agent 的基础架构

<div class="mt-6">
<div class="flex justify-center">
<div class="bg-gray-50 rounded-lg p-6 max-w-4xl w-full">

```mermaid
graph LR
    A[输入] --> B[感知]
    B --> C[记忆]
    C --> D[推理]
    D --> E[工具]
    E --> F[输出]
    E --> C
    
    style A fill:#e1f5fe
    style F fill:#e8f5e8
    style D fill:#fff3e0
    style E fill:#fce4ec
```

</div>
</div>
</div>

<div v-click class="mt-4 grid grid-cols-4 gap-4 max-w-4xl mx-auto text-sm">
  <div class="text-center p-3 bg-blue-50 rounded">
    <div class="font-semibold text-blue-700">感知模块</div>
    <div class="text-gray-600 mt-1">理解输入信息</div>
  </div>
  <div class="text-center p-3 bg-purple-50 rounded">
    <div class="font-semibold text-purple-700">记忆模块</div>
    <div class="text-gray-600 mt-1">存储上下文</div>
  </div>
  <div class="text-center p-3 bg-orange-50 rounded">
    <div class="font-semibold text-orange-700">推理引擎</div>
    <div class="text-gray-600 mt-1">制定计划</div>
  </div>
  <div class="text-center p-3 bg-pink-50 rounded">
    <div class="font-semibold text-pink-700">工具接口</div>
    <div class="text-gray-600 mt-1">执行操作</div>
  </div>
</div>

---
layout: two-cols
layoutClass: gap-6
class: text-left max-w-[60ch] mx-auto leading-8 space-y-6
---
## 🧩 Agent 架构的核心组件

<v-clicks>

### 1. **感知模块（Perception）**
- 文本理解：解析用户意图和指令
- 多模态输入：处理图像、音频等
- 环境状态：获取当前上下文

### 2. **记忆模块（Memory）**
- 短期记忆：当前对话的上下文
- 长期记忆：用户偏好、历史交互
- 工作记忆：当前任务的临时信息

</v-clicks>

::right::

<v-clicks>

### 3. **推理引擎（Reasoning）**
- 计划制定：将复杂任务分解为子步骤
- 策略选择：从多个方案中选择最优路径
- 因果推理：理解行动与结果的关系

### 4. **工具接口（Tools）**
- 搜索引擎：获取实时信息
- 计算器：进行数学运算
- API调用：连接外部服务
- 代码执行：运行程序脚本

</v-clicks>

<div v-click class="mt-6 p-3 bg-blue-50 rounded border-l-4 border-blue-400 text-sm">
💡 <strong>关键</strong>：四个模块协同工作，形成智能决策闭环
</div>

---
layout: section
class: text-center
---
# 🧠 深入理解：决策/推理引擎
Agent 的"大脑"如何工作

---
layout: center
class: text-center
---
# 📋 推理引擎的整体框架

<div class="mt-8 max-w-5xl mx-auto">
  <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
    <div class="bg-blue-50 rounded-lg p-6 border border-blue-200">
      <div class="text-center mb-4">
        <div class="text-4xl mb-2">📊</div>
        <h3 class="text-xl font-semibold text-blue-800">Planning / 事前规划</h3>
      </div>
      <div class="space-y-3 text-sm text-left">
        <div class="bg-white rounded p-3">
          <div class="font-semibold text-blue-700">🔗 Chain of Thought (CoT)</div>
          <div class="text-gray-600">逐步推理，线性思考过程</div>
        </div>
        <div class="bg-white rounded p-3">
          <div class="font-semibold text-green-700">🌳 Tree of Thought (ToT)</div>
          <div class="text-gray-600">多分支探索，并行评估方案</div>
        </div>
        <div class="bg-white rounded p-3">
          <div class="font-semibold text-purple-700">🎯 任务分解</div>
          <div class="text-gray-600">复杂问题拆解为子任务</div>
        </div>
      </div>
    </div>
    <div class="bg-orange-50 rounded-lg p-6 border border-orange-200">
      <div class="text-center mb-4">
        <div class="text-4xl mb-2">🔄</div>
        <h3 class="text-xl font-semibold text-orange-800">Self-Reflection / 事后反思</h3>
      </div>
      <div class="space-y-3 text-sm text-left">
        <div class="bg-white rounded p-3">
          <div class="font-semibold text-orange-700">🔄 ReAct 模式</div>
          <div class="text-gray-600">推理+行动的动态循环</div>
        </div>
        <div class="bg-white rounded p-3">
          <div class="font-semibold text-red-700">🧘 Reflexion 框架</div>
          <div class="text-gray-600">深度自我反思和记忆改进</div>
        </div>
        <div class="bg-white rounded p-3">
          <div class="font-semibold text-indigo-700">🔍 策略调整</div>
          <div class="text-gray-600">基于反馈优化执行路径</div>
        </div>
      </div>
    </div>
  </div>
</div>

<div v-click class="mt-6 p-4 bg-gradient-to-r from-blue-50 to-orange-50 rounded-lg border border-gray-200 max-w-4xl mx-auto">
  <p class="text-center text-gray-700">
    💡 <strong>核心理念</strong>：事前规划制定策略，事后反思优化执行，两者结合形成完整的智能决策系统
  </p>
</div>

---
layout: section
class: text-center
---
# 📊 事前规划：思维链技术
制定策略的核心方法

---
layout: two-cols
layoutClass: gap-6
class: text-left leading-7
---
## 🔗 Chain of Thought (CoT)

<v-clicks>

### 🎯 **核心理念**
逐步展示推理过程，让 AI “显性思考”

### 📝 **经典示例**
```
问题：如果一个披萨8片，3个人分，每人能分多少？

CoT 推理过程：
1. 总共8片披萨
2. 3个人平分
3. 8 ÷ 3 = 2.67片
4. 每人可分到约2片，剩余2片
```

### ✅ **优势**
- 推理过程透明可见
- 适合线性逻辑问题
- 容易理解和调试

</v-clicks>

::right::

## 🌳 Tree of Thought (ToT)

<v-clicks>

### 🎯 **核心理念**
探索多种可能的解决路径，并行评估和选择

### 📝 **实际应用**
```
问题：如何提高产品销量？

ToT 多路径探索：
│
├── 路径A：传统广告投放
│     ┗─ 成本高，覆盖面广
│
├── 路径B：社交媒体营销
│     ┗─ 成本低，传播精准
│
┗── 路径C：合作伙伴渠道
      ┗─ 共享资源，互利共赢

评估：选择 B+C 组合方案
```

### ✅ **优势**
- 全面考虑多种可能
- 避免局部最优解
- 适合复杂决策问题

</v-clicks>

---
layout: section
class: text-center
---
# 🔄 事后反思：自我进化技术
介错而改的智能机制

---
layout: two-cols
layoutClass: gap-6
class: text-left leading-7
---
## 🔄 ReAct 框架

<v-clicks>

### 🎯 **核心理念**
Reasoning + Acting 的动态循环

```mermaid
graph LR
    A[思考] --> B[行动]
    B --> C[观察]
    C --> A
    
    style A fill:#fff3e0
    style B fill:#e8f5e8
    style C fill:#e1f5fe
```

### 📝 **工作流程**
```
Thought: 用户问股价，需要实时数据
Action: get_stock_price("AAPL")
Observation: 苹果股价 $195.32
Thought: 现在可以给出完整回答
Action: 生成用户友好的回复
```

### ✅ **优势**
- 实时获取反馈
- 动态调整策略
- 错误及时纠正

</v-clicks>

::right::

## 🧘 Reflexion 框架

<v-clicks>

### 🎯 **核心理念**
深度自我反思和记忆改进

### 📝 **工作机制**
```
1. 执行任务
2. 评估结果
3. 识别问题和错误
4. 存储经验教训
5. 更新策略和行为模式
```

### 📊 **与 ReAct 对比**
- **ReAct**: 即时反馈，实时调整
- **Reflexion**: 累积学习，长期优化

### ✅ **优势**
- 从失败中学习
- 持续性能提升
- 适合复杂长期任务

</v-clicks>

<div v-click class="mt-4 p-3 bg-green-50 rounded border-l-4 border-green-400 text-sm">
💡 <strong>实战预告</strong>：ReAct 模式将在 Part 2 中详细演示和实践
</div>

---
layout: section
class: text-center
---
# 🛠️ 深入理解：工具接口
Agent 的"手脚"如何延伸

---
layout: default
class: text-left leading-7
---
# 🤔 为什么 Agent 需要工具？

<v-clicks>

### 🧠 **LLM 的固有局限**
- **知识截止日期**：无法获取最新信息
- **计算能力限制**：复杂数学运算容易出错
- **无法执行操作**：不能直接修改文件、发送邮件
- **缺乏实时数据**：无法访问股价、天气等动态信息

### 🔧 **工具的核心作用**
```
没有工具的AI："我不知道今天的天气，因为我的知识更新到..."

有工具的Agent：
1. 调用天气API获取实时数据
2. 分析数据并生成个性化建议
3. "北京今天晴，22°C，建议穿轻薄外套"
```

### 🌟 **工具让 AI 变成真正的助手**
从"知识问答机器"升级为"能干事的智能助手"

</v-clicks>

---
layout: section
class: text-center
---
# 🎯 工具决策机制
Agent 如何决定何时、如何使用工具？

---
layout: two-cols
layoutClass: gap-6
class: text-left leading-7
---
## 🧩 工具决策的核心机制

<v-clicks>

### 🎯 **LLM 作为决策核心**
通过 Prompt Engineering 训练 LLM：
- 理解何时需要工具
- 选择正确的工具
- 生成合适的参数

```
系统提示："当用户询问实时信息时，
使用 search_web() 工具获取最新数据"

用户："苹果股价多少？"
Agent：调用 get_stock_price("AAPL")
```

### 📋 **工具描述的重要性**
```json
{
  "name": "search_web",
  "description": "搜索最新网络信息",
  "parameters": {
    "query": "搜索关键词",
    "lang": "语言代码(zh/en)"
  }
}
```

</v-clicks>

::right::

<v-clicks>

### 🔄 **ReAct 框架中的工具调用**
在"Action"步骤明确输出：
```
Thought: 用户问股价，需要实时数据
Action: get_stock_price("AAPL")
Observation: 苹果股价 $195.32
Thought: 现在可以给出完整回答
```

### 🌟 **Function Calling 示例**
```python
# OpenAI Function Calling
response = client.chat.completions.create(
  model="gpt-4",
  messages=[{"role": "user", "content": "查询天气"}],
  functions=[
    {
      "name": "get_weather",
      "description": "获取指定城市天气",
      "parameters": {
        "type": "object",
        "properties": {
          "city": {"type": "string"}
        }
      }
    }
  ]
)
```

</v-clicks>

---
layout: center
class: text-center
---
# 🔗 MCP：模型上下文协议
**Model Context Protocol - 工具集成的新标准**

<div class="mt-8 max-w-4xl mx-auto">
  <div class="bg-gradient-to-r from-blue-50 to-purple-50 rounded-lg p-6 border border-blue-200">
    <h3 class="text-xl font-semibold text-blue-800 mb-4">🚀 什么是 MCP？</h3>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6 text-left">
      <div>
        <h4 class="font-semibold text-blue-700 mb-2">📖 定义</h4>
        <p class="text-sm text-gray-700">由 Anthropic 提出的开放标准，旨在标准化 AI 模型与外部工具/数据源的连接方式</p>
      </div>
      <div>
        <h4 class="font-semibold text-purple-700 mb-2">🎯 目标</h4>
        <p class="text-sm text-gray-700">让不同的 AI 模型能够无缝连接各种工具，避免重复开发，提高互操作性</p>
      </div>
    </div>
  </div>
</div>

<div v-click class="mt-6 grid grid-cols-1 md:grid-cols-3 gap-4 max-w-4xl mx-auto text-sm">
  <div class="bg-green-50 rounded p-4 border border-green-200">
    <div class="font-semibold text-green-700">✅ 标准化接口</div>
    <div class="text-gray-600 mt-1">统一的工具描述和调用格式</div>
  </div>
  <div class="bg-blue-50 rounded p-4 border border-blue-200">
    <div class="font-semibold text-blue-700">🔗 跨平台兼容</div>
    <div class="text-gray-600 mt-1">不同 AI 服务商都能使用</div>
  </div>
  <div class="bg-purple-50 rounded p-4 border border-purple-200">
    <div class="font-semibold text-purple-700">🚀 生态发展</div>
    <div class="text-gray-600 mt-1">促进工具生态系统繁荣</div>
  </div>
</div>

<div v-click class="mt-6 p-4 bg-yellow-50 rounded-lg border-l-4 border-yellow-400 max-w-3xl mx-auto">
  <p class="text-sm text-gray-700">
    💡 <strong>未来趋势</strong>：MCP 有望成为 AI Agent 工具集成的行业标准，简化开发流程，提高工具复用性
  </p>
</div>

---
layout: section
class: text-center
---
# 🚨 当前 AI Agent 的能力边界

---
layout: two-cols
layoutClass: gap-6
class: text-left leading-7
---
## ✅ 目前能做好的事情

<v-clicks>

### 🎯 信息处理与分析
- 文档总结和信息提取
- 数据分析和可视化

### 🔧 工具集成与自动化
- 搜索信息并整合答案
- 调用API获取实时数据

### 💭 结构化推理
- 逐步分解复杂问题
- 按照既定流程执行任务

### 🎨 创意生成
- 文案写作和内容创作
- 代码生成和调试

</v-clicks>

::right::

## Agent 体验推荐

<v-clicks>

### 🎯 智能助手 : ChatGPT / GenSpark
- 智能助手、知识库问答、通用型

### 🎯生成式 UI : Gemini Build
- 直接带 UI/UX 的 APP

### 🎯 写代码 : ClaudeCode / Qoder 
- Vibe Coding、部署代码

### 🎯工作流 n8n/Dify
- 完成复杂任务

### 🎯DeepResearch / NotebookLM
- 知识获取、整合、撰写

</v-clicks>

---
layout: two-cols
layoutClass: gap-6
class: text-left leading-7
---
## ⚠️ 仍然存在的局限

<v-clicks>

### 🧠 推理局限
- **长期规划能力有限**：难以处理需要数天/数周的复杂项目
- **因果推理不稳定**：在复杂逻辑链中容易出错
- **创新思维受限**：主要基于训练数据的模式匹配

### 🔄 执行局限  
- **错误恢复能力弱**：遇到异常情况时难以自主调整
- **工具使用不够灵活**：对新工具或复杂工具链适应性差
- **状态管理复杂**：在多步骤任务中容易丢失上下文

</v-clicks>

::right::

<v-clicks>

### 🎯 目标理解局限
- **隐含需求识别**：难以理解用户的潜在意图
- **价值判断缺失**：无法进行道德或伦理层面的判断
- **个性化程度低**：难以深度适应个人偏好和工作方式

</v-clicks>

---
layout: section
class: text-center
---
# Part 2: ReAct 模式深度解析
推理与行动的完美结合（25分钟）

---
layout: two-cols   
class: text-left max-w-[56ch] mx-auto leading-10 space-y-8
---
## 🔄 ReAct 模式简介


**ReAct = Reasoning + Acting**

### 核心思想
将**推理**（Reasoning）和**行动**（Acting）交替进行，形成动态的思考-行动循环

### 传统方式 vs ReAct
- **传统**：思考完 → 一次性行动
- **ReAct**：思考 → 行动 → 观察 → 再思考 → 再行动


::right::

### 为什么有效？
1. **实时反馈**：每次行动后都能获得新信息
2. **错误纠正**：发现问题时可以及时调整策略
3. **动态规划**：根据实际情况调整后续步骤



---
layout: two-cols
class: text-left max-w-[65ch] mx-auto leading-8 space-y-6
---
## 🛠️ ReAct 模式的工作流程


### 1. **Thought（思考）**
分析当前状态，制定下一步计划
```
思考：用户询问北京明天的天气，我需要获取实时天气信息
```

### 2. **Action（行动）** 
选择合适的工具或操作
```
行动：调用天气API search_weather("北京", "明天")
```

### 3. **Observation（观察）**
获取行动结果，更新当前状态
```
观察：API返回数据 - 北京明天晴，15-25°C，轻微西风
```

::right::

### 4. **Thought（再思考）**
基于新信息规划下一步
```
思考：已获得天气信息，现在可以给用户一个完整的回答
```

### 5. **Action（最终回答）**
```
行动：根据数据生成用户友好的回答
```

<div class="mt-8 max-w-4xl mx-auto">

<GeminiAgentModal />

</div>


<div v-click class="mt-6 p-4 bg-green-50 rounded-lg border-l-4 border-green-400">
💡 <strong>关键</strong>：每个循环都基于最新信息进行决策，保证决策的准确性和适应性
</div>

---
layout: section
class: text-center
---
# Part 3: Gemini Agent 实战演示
从理论到实践的完整演练（10分钟）


---
layout: center
class: text-center
---
# 🎯 实战演示：智能研究助手

https://peng.craft.me/BZrxoPPwmt6ZeY

<div v-click class="mt-6 text-lg text-gray-600">
点击上方按钮查看完整的 ReAct 模式演示
</div>

---
layout: section
class: text-center
---
# 🔧 动手实践：构建你的第一个 Agent

---
layout: default
class: text-left max-w-[65ch] mx-auto leading-8 space-y-6
---
## 🎯 实践任务：个人学习助手

<v-clicks>

### 📋 任务目标
创建一个能够帮助用户制定学习计划并跟踪进度的AI Agent

### 🛠️ 需要实现的功能
1. **学习目标分析**：将大目标分解为可执行的小任务
2. **资源推荐**：根据学习内容推荐合适的学习资料
3. **进度跟踪**：记录学习进度并提供反馈
4. **知识测验**：生成测试题检验学习效果

### 🔧 工具函数设计
```python
def analyze_learning_goal(goal: str) -> dict:
    """分析学习目标并分解任务"""
    
def recommend_resources(topic: str, level: str) -> list:
    """推荐学习资源"""
    
def track_progress(user_id: str, completed_tasks: list) -> dict:
    """跟踪学习进度"""
    
def generate_quiz(topic: str, difficulty: str) -> dict:
    """生成测验题目"""
```

</v-clicks>

---
layout: two-cols
layoutClass: gap-8
class: text-left
---
## 📝 实践步骤指导

### 第1步：设计系统提示词
```
你是一个专业的学习助手，能够：
1. 使用ReAct模式制定学习计划
2. 推荐合适的学习资源
3. 跟踪用户学习进度
4. 生成个性化测验

请始终按照以下模式工作：
- Thought: 分析用户需求
- Action: 选择合适的工具
- Observation: 处理工具返回结果
- 重复直到完成任务
```

### 第2步：配置工具函数
在 Gemini AI Studio 中添加自定义函数

### 第3步：测试对话流程
验证 ReAct 模式是否正常工作

::right::

### 第4步：优化和调试
根据测试结果改进提示词和函数

### 🎯 预期效果
```
用户：我想学习Python编程
Agent：
Thought: 用户想学Python，需要分析目标并制定计划
Action: analyze_learning_goal("Python编程")
Observation: 分解为基础语法、数据结构、项目实践等
Thought: 现在推荐学习资源
Action: recommend_resources("Python基础", "初学者")
...
```

<div class="mt-6 p-4 bg-blue-50 rounded-lg border-l-4 border-blue-400 text-sm">
💡 <strong>提示</strong>：从简单功能开始，逐步增加复杂性
</div>

---
layout: section
class: text-center
---
# 📊 课程总结与展望

---
layout: default
class: text-left max-w-[65ch] mx-auto leading-8 space-y-6
---
## 🎯 今天你学到了什么？

<v-clicks>

### 1. **AI Agent 的本质理解**
- Agent = 感知 + 决策 + 行动的智能循环
- 与传统AI的核心区别：主动性和工具集成能力
- 架构组件：感知、记忆、推理、工具四大模块

### 2. **ReAct 模式的深度掌握**
- Reasoning + Acting 的交替循环
- 思考→行动→观察→再思考的工作流程
- 相比其他模式的优势：实时反馈和错误纠正

</v-clicks>

---
layout: two-cols
layoutClass: gap-8
class: text-left max-w-[60ch] mx-auto leading-8
---
## 🚀 进一步学习

### 🔧 技术提升
<v-clicks>

- **深入学习更多工具**：Dify、n8n 等
- **探索其他平台**：Genspark、Manus
- **学习高级模式**：多Agent协作、链式推理、记忆管理
- **关注最新发展**：跟踪 Agent 技术的最新进展

</v-clicks>

### 🎯 项目实践
<v-clicks>

- **个人助手**：日程管理、邮件处理、信息整理
- **工作助手**：报告生成、数据分析、代码审查
- **学习助手**：课程规划、进度跟踪、知识测验
- **创意助手**：内容创作、设计灵感、方案生成

</v-clicks>

::right::

## 📚 推荐学习资源

### 📖 文档和教程
<v-clicks>
学习群内持续更新/分享
</v-clicks>

### 🛠️ 实用工具
<v-clicks>

- **开发框架**：LangGraph
- **部署平台**：Vercel, Cloudflare works
- **监控工具**：LangSmith
- **社区资源**：GitHub, X, Reddit

</v-clicks>

---
layout: section
class: text-center
---
# Part 4: AI Workflow 模式详解
基于 Anthropic 2024 年最佳实践（20分钟）

---
layout: section
class: text-center
---
# 🏗️ AI Workflow vs Agent 架构区分

---
layout: two-cols
layoutClass: gap-6
class: text-left leading-7
---
## 🔄 AI Workflow

<v-clicks>

### 📋 **定义**
通过**预定义的代码路径**来编排大模型和工具

### 🎯 **特点**
- **可预测性**：流程固定，结果一致
- **可控性**：每个步骤都有明确规则
- **效率高**：适合标准化任务
- **易调试**：问题容易定位和修复

### 📝 **适用场景**
- 文档处理流水线
- 客服分类路由
- 内容生成工作流
- 数据分析自动化

</v-clicks>

::right::

## 🤖 AI Agent

<v-clicks>

### 📋 **定义**
大模型**动态决定**自己的流程及使用什么工具

### 🎯 **特点**
- **自主性**：能独立制定计划
- **灵活性**：适应复杂多变的任务
- **智能性**：基于环境反馈调整策略
- **创造性**：能处理开放式问题

### 📝 **适用场景**
- 复杂问题解决
- 创意内容生成
- 多步骤研究任务
- 个性化助手服务

</v-clicks>

<div v-click class="mt-6 p-4 bg-blue-50 rounded-lg border-l-4 border-blue-400 text-sm">
💡 <strong>选择原则</strong>：能用 Workflow 解决的，就不要用 Agent。只有在需要动态决策时才考虑 Agent
</div>

---
layout: section
class: text-center
---
# 🔧 AI Workflow 基础构建模块

---
layout: center
class: text-center
---
# 🧩 增强型大模型（Augmented LLM）

<div class="mt-4">
  <div class="flex justify-center">
    <img src="/ai-agent-images/augmented-llm.webp" alt="增强型大模型架构" class="max-w-3xl w-full h-auto rounded-lg shadow-lg" />
  </div>
</div>

<div v-click class="mt-4 text-center">
  <div class="text-base text-gray-600 mb-1">Agent/Workflow 的核心基础</div>
  <div class="text-xs text-gray-500">具备检索、工具和记忆等增强功能的智能模型</div>
</div>

<div v-click class="mt-3 grid grid-cols-3 gap-3 max-w-3xl mx-auto text-xs">
  <div class="text-center p-2 bg-blue-50 rounded">
    <div class="font-semibold text-blue-700">🔍 检索功能</div>
    <div class="text-gray-600 mt-1">搜索查询、知识库访问</div>
  </div>
  <div class="text-center p-2 bg-green-50 rounded">
    <div class="font-semibold text-green-700">🛠️ 工具集成</div>
    <div class="text-gray-600 mt-1">API调用、代码执行</div>
  </div>
  <div class="text-center p-2 bg-purple-50 rounded">
    <div class="font-semibold text-purple-700">🧠 记忆管理</div>
    <div class="text-gray-600 mt-1">上下文保存、经验学习</div>
  </div>
</div>

---
layout: section
class: text-center
---
# 🔗 提示链（Prompt Chaining）

---
layout: center
class: text-center
---
# 📋 提示链模式详解

<div class="mt-8">
  <div class="flex justify-center">
    <img src="/ai-agent-images/prompt-chaining.webp" alt="提示链工作流" class="max-w-4xl w-full h-auto rounded-lg shadow-lg" />
  </div>
</div>

<div v-click class="mt-6 text-center">
  <div class="text-lg text-gray-600 mb-2">将复杂任务分解为顺序子任务</div>
  <div class="text-sm text-gray-500">每个 LLM call 处理前一个的输出，中间可添加检查点</div>
</div>

---
layout: two-cols
layoutClass: gap-6
class: text-left leading-7
---
## 🎯 适用场景

<v-clicks>

### ✅ **理想条件**
- 任务可以**干净地分解**为固定子任务
- 每个步骤都有**明确的输入输出**
- 步骤之间有**清晰的依赖关系**

### 📝 **典型应用**
- **营销文案生成**：创意构思 → 文案撰写 → 多语言翻译
- **文档编写**：大纲制定 → 内容填充 → 格式优化
- **数据分析**：数据清洗 → 统计分析 → 报告生成

</v-clicks>

::right::

## 💡 设计要点

<v-clicks>

### 🔧 **技术实现**
```
步骤1: 生成营销创意
↓
检查点: 创意质量评估
↓
步骤2: 撰写具体文案
↓
检查点: 文案效果验证
↓
步骤3: 多语言翻译
```

### ⚠️ **注意事项**
- **错误传播**：前一步错误会影响后续步骤
- **上下文丢失**：需要合理传递关键信息
- **成本控制**：多个 LLM 调用增加成本

</v-clicks>

---
layout: section
class: text-center
---
# 🚦 路由（Routing）

---
layout: center
class: text-center
---
# 🎯 路由模式详解

<div class="mt-8">
  <div class="flex justify-center">
    <img src="/ai-agent-images/routing-workflow.webp" alt="路由工作流" class="max-w-4xl w-full h-auto rounded-lg shadow-lg" />
  </div>
</div>

<div v-click class="mt-6 text-center">
  <div class="text-lg text-gray-600 mb-2">智能分类并转发到专门处理流程</div>
  <div class="text-sm text-gray-500">针对不同任务类型优化提示词和工具</div>
</div>

---
layout: two-cols
layoutClass: gap-6
class: text-left leading-7
---
## 🎯 适用场景

<v-clicks>

### ✅ **理想条件**
- 存在**不同类别的复杂任务**
- 分类后处理效果**明显更好**
- 能够**准确分类**输入

### 📝 **典型应用**
- **智能客服**：一般咨询 → 技术支持 → 退款处理
- **内容审核**：文本审核 → 图片审核 → 视频审核
- **模型路由**：简单问题 → 小模型，复杂问题 → 大模型

</v-clicks>

::right::

## 💡 设计要点

<v-clicks>

### 🔧 **分类策略**
```
用户输入 → 分类器 → 路由决策
                ↓
        ┌───────┼───────┐
        ↓       ↓       ↓
    客服A    技术支持   退款处理
   (通用)     (专业)    (流程)
```

### ⚠️ **注意事项**
- **分类准确性**：错误分类导致处理效果差
- **阈值设定**：平衡分类精度和召回率
- **兜底机制**：处理无法分类的边缘情况

</v-clicks>

---
layout: section
class: text-center
---
# ⚡ 并行化（Parallelization）

---
layout: center
class: text-center
---
# 🔄 并行化模式详解

<div class="mt-8">
  <div class="flex justify-center">
    <img src="/ai-agent-images/parallelization-workflow.webp" alt="并行化工作流" class="max-w-4xl w-full h-auto rounded-lg shadow-lg" />
  </div>
</div>

<div v-click class="mt-6 text-center">
  <div class="text-lg text-gray-600 mb-2">多任务并行执行，结果聚合处理</div>
  <div class="text-sm text-gray-500">分段处理 + 投票机制，提高效率和质量</div>
</div>

---
layout: two-cols
layoutClass: gap-6
class: text-left leading-7
---
## 🎯 两种并行策略

<v-clicks>

### 📊 **分段处理（Sectioning）**
类似 MapReduce，将任务分解为独立子任务

**应用场景：**
- **安全检测**：内容审核 + 用户行为分析
- **性能评估**：多维度并行评估模型表现
- **代码审查**：语法检查 + 逻辑分析 + 安全扫描

### 🗳️ **投票机制（Voting）**
相同任务并行执行多次，获得多样化输出

**应用场景：**
- **代码生成**：多个版本对比选择最优
- **创意生成**：多个方案投票选出最佳
- **质量评估**：多角度评估减少误判

</v-clicks>

::right::

## 💡 设计要点

<v-clicks>

### 🔧 **技术实现**
```python
# 分段处理示例
def parallel_analysis(text):
    tasks = [
        analyze_sentiment(text),
        check_grammar(text),
        detect_toxicity(text)
    ]
    results = await asyncio.gather(*tasks)
    return aggregate_results(results)

# 投票机制示例
def voting_generation(prompt):
    responses = [
        generate_response(prompt, model="gpt-4"),
        generate_response(prompt, model="claude-3"),
        generate_response(prompt, model="gemini-pro")
    ]
    return select_best_response(responses)
```

### ⚠️ **注意事项**
- **成本控制**：并行调用增加成本
- **结果一致性**：需要合理的聚合策略
- **错误处理**：部分任务失败的处理机制

</v-clicks>

---
layout: section
class: text-center
---
# 🎭 编排者-工作者（Orchestrator-Workers）

---
layout: center
class: text-center
---
# 🎯 编排者-工作者模式详解

<div class="mt-8">
  <div class="flex justify-center">
    <img src="/ai-agent-images/orchestrator-workers-workflow.webp" alt="编排者-工作者工作流" class="max-w-4xl w-full h-auto rounded-lg shadow-lg" />
  </div>
</div>

<div v-click class="mt-6 text-center">
  <div class="text-lg text-gray-600 mb-2">中心式 LLM 动态分解任务并委托执行</div>
  <div class="text-sm text-gray-500">灵活的任务分配和结果汇总机制</div>
</div>

---
layout: two-cols
layoutClass: gap-6
class: text-left leading-7
---
## 🎯 适用场景

<v-clicks>

### ✅ **理想条件**
- 任务复杂度**无法预测**
- 需要**动态调整**子任务
- 子任务数量**不确定**

### 📝 **典型应用**
- **代码审查**：根据修改文件数量动态分配审查任务
- **智能搜索**：多源信息收集和分析
- **项目管理**：根据项目复杂度分配不同专家
- **内容创作**：根据主题复杂度分配不同创作者

</v-clicks>

::right::

## 💡 设计要点

<v-clicks>

### 🔧 **架构设计**
```
用户请求 → 编排者(Orchestrator)
                ↓
        任务分解和分配
                ↓
    ┌───────────┼───────────┐
    ↓           ↓           ↓
工作者A      工作者B      工作者C
(专家1)      (专家2)      (专家3)
    ↓           ↓           ↓
        结果汇总和整合
                ↓
        最终输出给用户
```

### ⚠️ **注意事项**
- **协调复杂性**：编排者需要智能的任务分解能力
- **负载均衡**：合理分配任务避免某些工作者过载
- **结果一致性**：确保不同工作者的输出风格统一

</v-clicks>

---
layout: section
class: text-center
---
# 🔍 评估者-优化者（Evaluator-Optimizer）

---
layout: center
class: text-center
---
# 🔄 评估者-优化者模式详解

<div class="mt-8">
  <div class="flex justify-center">
    <img src="/ai-agent-images/evaluator-optimizer-workflow.webp" alt="评估者-优化者工作流" class="max-w-4xl w-full h-auto rounded-lg shadow-lg" />
  </div>
</div>

<div v-click class="mt-6 text-center">
  <div class="text-lg text-gray-600 mb-2">生成-评估-优化的闭环改进机制</div>
  <div class="text-sm text-gray-500">通过迭代反馈持续提升输出质量</div>
</div>

---
layout: two-cols
layoutClass: gap-6
class: text-left leading-7
---
## 🎯 适用场景

<v-clicks>

### ✅ **理想条件**
- 有**明确的评估标准**
- 迭代式改进**确实有效**
- 能够**量化改进效果**

### 📝 **典型应用**
- **文学翻译**：翻译 → 质量评估 → 优化改进
- **复杂搜索**：搜索 → 结果评估 → 调整策略
- **代码生成**：生成代码 → 测试评估 → 修复问题
- **创意写作**：初稿 → 质量评估 → 润色优化

</v-clicks>

::right::

## 💡 设计要点

<v-clicks>

### 🔧 **工作流程**
```
1. 生成器：创建初始输出
   ↓
2. 评估器：分析输出质量
   ↓
3. 优化器：基于反馈改进
   ↓
4. 循环：重复直到满意
```

### 📊 **评估维度**
- **准确性**：内容是否正确
- **完整性**：是否覆盖所有要求
- **一致性**：风格和格式是否统一
- **创新性**：是否有独特见解

</v-clicks>

---
layout: section
class: text-center
---
# 🤖 AI Agent 设计原则

---
layout: two-cols
layoutClass: gap-6
class: text-left leading-7
---
## 🎯 Agent 设计三原则

<v-clicks>

### 1. **简洁性（Simplicity）**
- 避免过度复杂的架构
- 优先使用简单、可组合的模式
- 从基础组件开始构建

### 2. **透明性（Transparency）**
- 明确显示 Agent 的规划和步骤
- 提供清晰的决策过程
- 让用户理解 Agent 在做什么

### 3. **接口设计（Interface Design）**
- 精心设计 Agent 与计算机的接口
- 完善的文档和测试
- 确保工具描述清晰准确

</v-clicks>

::right::

## 💡 实践建议

<v-clicks>

### 🚀 **开发策略**
- **首选直接使用 LLM API**：避免不必要的抽象层
- **理解框架底层**：如果使用框架，确保理解其工作原理
- **从简单开始**：逐步增加复杂性

### ⚠️ **常见陷阱**
- **过度工程化**：为了技术而技术
- **抽象层过多**：难以调试和维护
- **工具描述不清**：导致 Agent 使用效果差

</v-clicks>

<div v-click class="mt-6 p-4 bg-green-50 rounded-lg border-l-4 border-green-400 text-sm">
💡 <strong>核心理念</strong>：成功的 Agent 不是最复杂的，而是最符合需求的
</div>

---
layout: section
class: text-center
---
# 🛠️ 工具设计最佳实践

---
layout: two-cols
layoutClass: gap-6
class: text-left leading-7
---
## 📝 工具描述工程

<v-clicks>

### 🎯 **输出格式选择**
- **优先选择简单格式**：避免复杂的转义和解析
- **保持一致性**：与互联网常见格式保持一致
- **减少格式开销**：避免需要精确记录大量信息

### 📋 **工具定义要点**
```json
{
  "name": "search_web",
  "description": "搜索最新网络信息，适用于获取实时数据",
  "parameters": {
    "query": "搜索关键词，支持中英文",
    "lang": "语言代码，zh表示中文，en表示英文"
  },
  "examples": [
    {
      "input": {"query": "苹果股价", "lang": "zh"},
      "output": "苹果公司(AAPL)当前股价为$195.32..."
    }
  ]
}
```

</v-clicks>

::right::

## 🔧 防呆设计

<v-clicks>

### 🛡️ **错误预防**
- **参数验证**：确保输入参数格式正确
- **边界处理**：处理异常和边界情况
- **默认值设置**：为可选参数提供合理默认值

### 🧪 **测试策略**
- **示例测试**：用典型输入测试工具
- **边界测试**：测试极端情况
- **错误测试**：验证错误处理机制

### 📚 **文档要求**
- **清晰描述**：像给新人写 docstring 一样详细
- **示例丰富**：提供多种使用场景的示例
- **界限明确**：明确与其他工具的区别

</v-clicks>

---
layout: section
class: text-center
---
# 🎯 实战案例：Coding Agent

---
layout: center
class: text-center
---
# 💻 Coding Agent 架构解析

<div class="mt-8">
  <div class="flex justify-center">
    <img src="/ai-agent-images/coding-agent.webp" alt="Coding Agent架构" class="max-w-4xl w-full h-auto rounded-lg shadow-lg" />
  </div>
</div>

<div v-click class="mt-6 text-center">
  <div class="text-lg text-gray-600 mb-2">Anthropic 的 SWE-bench 解决方案</div>
  <div class="text-sm text-gray-500">仅根据 Pull Request 描述解决真实 GitHub 问题</div>
</div>

---
layout: two-cols
layoutClass: gap-6
class: text-left leading-7
---
## 🎯 为什么 Coding Agent 特别有效？

<v-clicks>

### ✅ **理想环境**
- **问题空间明确**：代码问题有清晰的结构
- **结果可验证**：通过自动化测试验证解决方案
- **反馈循环完整**：测试结果提供即时反馈
- **质量可衡量**：输出质量可以客观评估

### 🛠️ **核心能力**
- **代码理解**：分析现有代码结构和逻辑
- **问题诊断**：识别 bug 和性能问题
- **解决方案生成**：编写修复代码
- **测试验证**：运行测试确保修复有效

</v-clicks>

::right::

## 💡 设计亮点

<v-clicks>

### 🔧 **工具设计**
- **文件操作**：读取、修改、创建文件
- **代码执行**：运行测试和验证
- **版本控制**：Git 操作和分支管理
- **搜索功能**：在代码库中查找相关信息

### 🧠 **推理模式**
- **问题分析**：理解 PR 描述和代码变更
- **影响评估**：分析修改对系统的影响
- **测试策略**：制定测试计划验证修复
- **迭代优化**：基于测试结果改进方案

</v-clicks>

<div v-click class="mt-6 p-4 bg-blue-50 rounded-lg border-l-4 border-blue-400 text-sm">
💡 <strong>关键洞察</strong>：Coding Agent 的成功证明了在结构化、可验证的环境中，Agent 能够达到很高的性能水平
</div>

---
layout: section
class: text-center
---
# 🚀 未来趋势与展望

---
layout: two-cols
layoutClass: gap-6
class: text-left leading-7
---
## 🔮 技术发展趋势

<v-clicks>

### 🧠 **模型能力提升**
- **推理能力增强**：更复杂的逻辑推理和规划
- **工具使用优化**：更智能的工具选择和参数生成
- **多模态融合**：文本、图像、音频的统一处理
- **长期记忆**：更好的上下文管理和经验积累

### 🛠️ **工具生态发展**
- **MCP 标准化**：统一的工具集成协议
- **工具市场**：丰富的第三方工具生态
- **自动化部署**：一键部署和配置 Agent
- **监控和调试**：更好的可观测性工具

</v-clicks>

::right::

## 🎯 应用场景扩展

<v-clicks>

### 🏢 **企业应用**
- **智能客服**：基于 usage-based pricing 的商业模式
- **代码助手**：从补全到自主问题解决
- **数据分析**：自动化数据洞察和报告生成
- **项目管理**：智能任务分配和进度跟踪

### 🏠 **个人应用**
- **学习助手**：个性化学习计划和进度跟踪
- **创作助手**：内容创作和创意生成
- **生活助手**：日程管理、信息整理、决策支持
- **健康助手**：健康监测和生活方式建议

</v-clicks>

---
layout: section
class: text-center
---

# 📚 学习资源与下一步

---
layout: two-cols
layoutClass: gap-6
class: text-left leading-7## 📖 推荐学习资源
---

<v-clicks>

### 📚 **官方文档**
- **Anthropic Cookbook**：官方示例和最佳实践
- **Model Context Protocol**：工具集成标准
- **LangGraph 文档**：工作流构建框架
- **OpenAI Function Calling**：工具调用指南

### 🛠️ **实践平台**
- **Gemini AI Studio**：Google 的 Agent 构建平台
- **Dify**：开源 LLM 应用开发平台
- **n8n**：工作流自动化工具
- **Vercel AI SDK**：快速构建 AI 应用

</v-clicks>

::right::

## 🎯 实践建议

<v-clicks>

### 🚀 **学习路径**
1. **从简单开始**：先掌握基础的工具调用
2. **理解模式**：深入学习各种 Workflow 模式
3. **动手实践**：构建自己的 Agent 项目
4. **持续优化**：基于反馈不断改进

### 💡 **项目想法**
- **个人助手**：日程管理、邮件处理
- **学习工具**：课程规划、知识测验
- **工作助手**：报告生成、数据分析
- **创意工具**：内容创作、设计灵感

</v-clicks>

<div v-click class="mt-6 p-4 bg-gradient-to-r from-blue-50 to-green-50 rounded-lg border border-gray-200">
  <p class="text-center text-gray-700">
    🎉 <strong>恭喜完成学习！</strong> 现在你已经掌握了 AI Agent 的核心概念和实践方法，可以开始构建自己的智能应用了！
  </p>
</div>
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

<LLMDetails />

> 把你的话拆成小块（Token），用数学方法理解它们之间的关系，然后一次预测一个小块地拼成答案。了解它的流程，不是为了让你写算法，而是为了让你写的提示词更像它喜欢吃的‘拼图’，它才能拼出你想要的画面。

<!--
- AI 不直接读“汉字”或“英文单词”，而是读数字。
- Token 就是模型的“最小阅读单位”，可以是一个字、一个词，甚至一个词的一部分（比如“unhappy”会分成 “un” + “happy”）。
- Token 化是为了让不同语言、符号都能用同一套“字典”表示成数字
-->

---
class: text-left max-w-[56ch] mx-auto leading-10 space-y-8
---

## Transformer 架构

- 是什么：一种处理序列信息的通用架构，由 Google 于 2017 年提出（“Attention Is All You Need”）；当下主流大语言模型（GPT、Claude、Gemini、Qwen）都基于它。
- 为什么它成为主流：
  1. <span v-mark.circle.green>一次看全局</span>：不必逐词顺序处理，可同时关注整段文本
  2. 擅长捕捉远距离关系
  3. 并行友好，适配 GPU/TPU，速度快
  4. 通用性强，可扩展到多模态任务
  5. 易扩展升级（Scaling Law）


<blockquote v-click>
Transformer 是 AI 的“通用大脑”架构，能够快速、全面地理解并生成各类信息。
</blockquote>

---
class: text-left max-w-[56ch] mx-auto leading-10 space-y-8
---

## 核心机制：Self-Attention


- 是什么：在处理某个词时，模型可以“看见”句子中<span v-mark.circle.green>所有其他词</span>，并根据相关性分配不同的注意力权重。
- 为什么厉害：
  - 能捕捉长距离依赖（如“巴黎是法国的首都”中，“巴黎”与“法国”强相关）
  - 支持<span v-mark.circle.green>全局信息整合</span>，一次性理解整段文本


<blockquote v-click>
过去的模型像用手电筒一次只照一个点；Self-Attention 则像打开顶棚灯，一次照亮全场。
</blockquote>

<div class="mt-4">
  <SelfAttentionDetails />
</div>

---
class: text-left max-w-[1200px] mx-auto leading-10 space-y-8
---

## 基于 Transformer的 LLM 的能力边界
 
<div class="grid grid-cols-2 gap-6 items-start leading-7">
  <div>
    <h3 class="text-xl font-semibold">01 上下文记忆有限</h3>
    <ul class="list-disc ml-5 mt-2 space-y-1 text-[1.05rem]">
      <li>一次能处理的输入受 <span v-mark.circle.green>Token</span> 窗口限制</li>
      <li>超过窗口会“遗忘”最早内容（摘要压缩也会丢失细节）</li>
    </ul>
  </div>
  <div>
    <h3 class="text-xl font-semibold">02 不是绝对事实</h3>
    <ul class="list-disc ml-5 mt-2 space-y-1 text-[1.05rem]">
      <li>本质是概率预测，并非权威数据库</li>
      <li>可能生成 <span v-mark.circle.green>看似合理但不真实</span> 的信息（幻觉）</li>
    </ul>
  </div>
  <div>
    <h3 class="text-xl font-semibold">03 缺乏长期记忆</h3>
    <ul class="list-disc ml-5 mt-2 space-y-1 text-[1.05rem]">
      <li>默认不跨会话保留历史</li>
      <li>需要外部记忆/检索或重复关键信息</li>
    </ul>
  </div>
  <div>
    <h3 class="text-xl font-semibold">04 因果推理有限</h3>
    <ul class="list-disc ml-5 mt-2 space-y-1 text-[1.05rem]">
      <li>多步严密推理不稳定，易受干扰</li>
      <li>擅长模式匹配，不等同可验证的逻辑引擎</li>
    </ul>
  </div>
</div>

<blockquote v-click>
💡 理解这些边界，才能用对方法， 提高自己使用 AI的能力。
</blockquote>

---
layout: image-right
image: 'public/gpt-5-une.jpg'
class: text-left max-w-[56ch] mx-auto leading-10 space-y-8
---

## 问题 1：为什么感觉 GPT-5 会“思考”？

<v-clicks>

- 本质没变
  - 依然是 <span v-mark.circle.green>概率预测</span> 的 Transformer 模型
  - 没有意识、自我意图

- 为什么看起来像在思考
  1. 推理链（CoT）更长、更稳定
  2. 接入 <span v-mark.underline.orange>外部工具</span> 和<span v-mark.underline.orange>实时信息</span>
  3. 记忆与风格一致性更好（跨对话保持连贯）

</v-clicks>

<blockquote v-click>
“它像一个超级秘书——没有自己的想法，但能快速查资料、整理逻辑，让你觉得它在替你思考。”
</blockquote>

---
layout: image-right
image: 'public/thinking_model.png'
backgroundSize: contain
class: text-left max-w-[56ch] mx-auto leading-10 space-y-8
---

## 问题 2：模型里的 “Think 模式” 是什么？

<v-clicks>

- 是什么
  - 模型在回答前，会 <span v-mark.circle.green>先生成内部推理步骤</span>（不直接展示给用户）
  - 有些厂商提供“可见推理”版本，让用户看到中间思路

- 为什么有用
  - 更复杂任务可分解成多步
  - 降低推理出错率
  - 方便开发者调试模型行为

- 注意点
  - 显式推理可能泄露模型内部偏差
  - 推理链本身也是概率生成，不等于真实逻辑

</v-clicks>

---
layout: image-right
image: 'public/LLM-Parameters.webp'
backgroundSize: contain
class: text-left max-w-[56ch] mx-auto leading-10 space-y-8
---

## 问题3：参数（70B?）与能力关系

<v-clicks>

- 参数是什么
  - 模型中 <span v-mark.circle.green>可学习的权重</span>，类似神经元的连接强度
  - 单位 “Billion” = 十亿参数

- 规模与能力
  - Scaling Law：参数多 → 潜在能力强
  - 需要匹配 <span v-mark.circle.green>高质量数据</span> 和计算资源
  - 参数过大但训练差，性能未必好

</v-clicks>

<blockquote v-click>
“更多参数像是更多神经元，但学得好不好，还得看老师、教材和训练时间。”
</blockquote>

---
class: text-left max-w-[56ch] mx-auto leading-10 space-y-8
---
# 理论太多
## 那和我们有关系的是！（实践视角）

<v-clicks>

- 上下文管理
- 温度设置
- 幻觉防范
- 推理 vs 训练
- 工具调用

</v-clicks>

---
class: text-left max-w-[56ch] mx-auto leading-10 space-y-8
---

## 上下文（Context）限制与 Token


- 上下文窗口大小限制一次能“记住”的信息量（示例：<span v-mark.underline.green>128k tokens</span>）
- Token 近似：英文 4 字符 / 中文 2~3 字
- 影响：速度、成本、上下文长度


<div class="mt-2">
  <p class="font-semibold">💡 对使用者的价值</p>
  <ul class="list-disc ml-5 mt-1 space-y-1">
    <li>重要信息尽量集中在 <span v-mark.circle.green>一条输入</span> 里，避免关键信息被截断</li>
    <li>压缩冗余描述，让 Token 留给必要内容</li>
  </ul>
  
</div>

---
class: text-left max-w-[56ch] mx-auto leading-10 space-y-8
---

## 温度（Temperature）


- 高温度：创造性↑、随机性↑
- 低温度：确定性↑、稳定性↑
- 任务匹配：写诗 vs 写代码


<div class="mt-2">
  <p class="font-semibold">💡 对使用者的价值</p>
  <ul class="list-disc ml-5 mt-1 space-y-1">
    <li>创意写作（广告语、诗歌、脑暴） → 高温度 0.8~1.0</li>
    <li>严谨任务（代码、合同、数据分析） → <span v-mark.circle.green>低温度</span> 0~0.3</li>
    <li>现场可用同一 Prompt 对比不同温度输出效果</li>
  </ul>
  
</div>

---
class: text-left max-w-[56ch] mx-auto leading-10 space-y-8
---

## 幻觉（Hallucination）与防范


- 成因：生成概率机制导致 <span v-mark.circle.green>“合理但不真实”</span> 的虚构
- 防范：检索增强、限制领域、工具验证


<div class="mt-2">
  <p class="font-semibold">💡 对使用者的价值</p>
  <ul class="list-disc ml-5 mt-1 space-y-1">
    <li>核心事实用搜索或工具验证</li>
    <li>在提示词中明确要求“如果不确定，请说不知道”</li>
    <li>尽量提供 <span v-mark.circle.green>具体背景</span>，减少 AI 自由发挥空间</li>
  </ul>
  
</div>

---
class: text-left max-w-[56ch] mx-auto leading-10 space-y-8
---

## 训练 vs 推理；微调 vs 提示词

- 训练：让模型学习模式（高成本）
- 推理：用模型生成结果（日常使用）
- 微调：更新模型权重；提示词工程：优化输入与过程


<div class="mt-2">
  <p class="font-semibold">💡 对使用者的价值</p>
  <ul class="list-disc ml-5 mt-1 space-y-1">
    <li>日常用 AI 是 <span v-mark.circle.green>推理阶段</span> → 成本低、速度快</li>
    <li>微调成本高，不适合个人 → 个人优化主要靠 <span v-mark.circle.green>写好提示词</span></li>
  </ul>
  
</div>

---
class: text-left max-w-[56ch] mx-auto leading-10 space-y-8
---

## 工具调用（Function Calling）

- 可调用外部工具完成任务：搜索、计算器、数据库、代码执行
- 是实现自动化与多模态的基础能力之一


<div class="mt-2">
  <p class="font-semibold">💡 对使用者的价值</p>
  <ul class="list-disc ml-5 mt-1 space-y-1">
    <li>会用带工具调用的 AI（如 ChatGPT + Code Interpreter/搜索）</li>
    <li>能完成更多任务：自动生成并发送邮件、分析图片、从数据库获取信息</li>
    <li>大幅扩展 AI 的 <span v-mark.circle.green>实用场景</span></li>
  </ul>
  
</div>

---
class: text-left max-w-[56ch] mx-auto leading-10 space-y-8
---

# 扩展：模型类型与多模态

## 单模态 vs 多模态


- 单模态：仅处理文本；成本/延迟更低，适合代码、写作、结构化数据问答
- 多模态：文本 + 图片/音频/视频；适合 OCR、图表/表格理解、UI/场景分析
- 选择建议：优先尝试将视觉关键信息转成文字再用单模态；确需视觉细节时再启用多模态
- 实战提醒：多模态上下文编码开销大，应控制分辨率、页数与帧数

---
class: text-left max-w-[56ch] mx-auto leading-10 space-y-8
---

## 多模态价值与边界


- 价值：图文理解、OCR、图表/表格问答、UI/报表解读、图像生成
- 边界：小字/模糊文字、跨页一致性、长视频时序、细粒度逻辑仍弱
- 降低失误：
  - 先“描述再作答”（先要模型列出看到了什么，再回答问题）
  - 提供高分辨率或裁剪关键区域，分步提问
  - 必要时结合检索/工具做事实校验

---
class: text-left max-w-[56ch] mx-auto leading-10 space-y-8
---

## 视觉生成模型 vs LLM


- 视觉生成（如 Flux、Veo 3）多为扩散/Flow 系列模型，直接输出像素
- LLM 产出文本；在系统中承担“规划/统筹/解释”的角色
- 控制手段：提示词 + 参考图（IP-Adapter）、ControlNet、分镜脚本/约束
- 协作范式：LLM 先生成结构化提示（镜头/主体/光线/风格），再交给生成模型渲染


<div class="mt-4">
  <MultiModalVsTextLLMDetails />
</div>

---
layout: image-right
image: 'public/glm4.5v.jpg'
backgroundSize: contain
class: text-left max-w-[56ch] mx-auto leading-10 space-y-8
---
## 多模态趋势与协作


- 趋势：文本 → 图文 → 图文音视频一体化；统一 Transformer 处理多模态 Token
- Agent 化：LLM 依据任务调用 OCR/ASR/检索/执行器，组装成可解释的流水线
- 实战建议：将复杂任务拆成“文本推理 + 视觉工具子任务”，阶段性产出可验证中间结果


---
layout: iframe-right
url: https://www.trackingai.org/home
---
# AI能力与边界案例

## 大语言模型的能力水平

- 基础能力：更强推理、更少幻觉、更广知识、长上下文、安全性
- 扩展能力：多模态的理解能力、工具调用和 Agent 能力

## 当前能力最强的 5 个模型 （2025.08）
GPT 5系列、OpenAI o3、Claude Opus4.1、<span v-mark.underline.orange>Gemini 2.5 Pro</span> 和 Grok 4

## Benchmark
### https://livebench.ai/ （新鲜数据）

---
class: text-left max-w-[56ch] mx-auto leading-10 space-y-6
---
## 我们考验下 LLM
### 谁能推理出结果

<div class="my-6 space-y-4">
  <p class="text-gray-800">有一天，一个女孩参加数学考试只得了38分。她心里对父亲的惩罚充满恐惧，于是偷偷把分数改成了88分。她的父亲看到试卷后，怒发冲冠，狠狠地给了她巴掌，怒吼道："你这8怎么一半是绿的，一半是红的，你以为我是傻子吗？"女孩被打后，委屈地哭了起来，什么也没说。</p>
  
  <p class="text-gray-800">过了一会儿，父亲突然崩溃了。</p>
  
  <p class="font-semibold text-blue-600">请问：这位父亲为什么过一会儿崩溃了？</p>
  <p class="text-sm text-gray-500 italic">提示：这是逻辑推理题，"智商"测试题，而非情感题目。</p>
</div>

<v-clicks>
<div class="flex items-center gap-2 mb-2">
  <button 
    @click="copyToClipboard"
    class="px-3 py-1 text-xs bg-gray-200 hover:bg-gray-300 rounded transition-colors"
    title="复制题目"
  >
    📋 复制题目
  </button>
</div>

<script setup>
const copyToClipboard = async () => {
  const text = `有一天，一个女孩参加数学考试只得了38分。她心里对父亲的惩罚充满恐惧，于是偷偷把分数改成了88分。她的父亲看到试卷后，怒发冲冠，狠狠地给了她巴掌，怒吼道："你这8怎么一半是绿的，一半是红的，你以为我是傻子吗？"女孩被打后，委屈地哭了起来，什么也没说。

过了一会儿，父亲突然崩溃了。

请问：这位父亲为什么过一会儿崩溃了？
提示：这是逻辑推理题，"智商"测试题，而非情感题目。`
  
  try {
    await navigator.clipboard.writeText(text)
    // 可以添加一个简单的提示
    console.log('题目已复制到剪贴板')
  } catch (err) {
    console.error('复制失败:', err)
  }
}
</script>

<span v-mark.underline.orange>从遗传学角度考虑。</span>

</v-clicks>


---
layout: image-left
image: 'public/image.jpeg'
---

## 图片生成的能力与边界

- 能力：超高分辨率、细节丰富、艺术风格
- 边界：复杂结构易错、逻辑矛盾 prompt 失败、跨图一致性差

## 当前最强的 5 个文生图模型（2025.08）

- Imagen 4(Gemini)
- 即梦 3.0
- Flux 1.1 Pro Ultro 
- GPT-5
- Qwen-Image / Flux Krea Dev （开放权重）

---
class: text-left max-w-[56ch] mx-auto leading-10
---
## 视频生成: 以 Veo3 为例  

- 能力：高保真短视频生成、原生音频
- 边界：时长限制、成功率不稳定、动作控制精度有限
- 适配：适合短促视觉表达，不替代长视频制作

### 目前 <span v-mark.underline.orange>Vidu</span> 和 <span v-mark.underline.orange>可灵</span> 是可用性比较好的商业化产品

<div class="space-y-4">
  <SlidevVideo v-show="currentVideo === 1" controls>
    <source src="/1.mp4" type="video/mp4" />
    <p>当前浏览器不支持播放，请点击 <a href="/1.mp4">下载视频</a>。</p>
  </SlidevVideo>

  <SlidevVideo v-show="currentVideo === 2" controls>
    <source src="/2.mp4" type="video/mp4" />
    <p>当前浏览器不支持播放，请点击 <a href="/2.mp4">下载视频</a>。</p>
  </SlidevVideo>

  <div class="flex justify-center mt-4">
    <button 
      @click="currentVideo = currentVideo === 1 ? 2 : 1"
      class="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700 transition-colors"
    >
      {{ currentVideo === 1 ? 'Next' : 'Previous' }}
    </button>
  </div>
</div>

<script setup>
import { ref } from 'vue'
const currentVideo = ref(1)
</script>


---
layout: iframe-right
url: https://elevenlabs.io/text-to-speech
---

## 前沿 TTS / 语音克隆

- 能力：多语言、情感语音、秒级样本克隆
- 边界：长段情绪维持不稳、极端情绪不自然、实时性依赖硬件

## 推荐尝试的 TTS 模型（2025.08）

- 豆包、海螺、ChatTTS （中文）
- ElevenLabs、Gemini、OpenAI TTS （多语言）

---
class: text-left max-w-[56ch] mx-auto leading-10 space-y-8
---
## 本课总结与课后任务

<v-clicks>

- 总结：LLM 基础、能力圈、边界与关键限制
- 下节正课： 讲解提示词和上下文工程
- 周四实践课： 讲解和体验 [Google AI Studio](https://aistudio.google.com/)
- 任务： 想一下自己通过本训练营要做一个什么项目

</v-clicks>

<!--
演讲者笔记：
- 每页仅 1 个主题，口头扩展细节；穿插 4-6 个演示页。
- 图片/视频后续替换真实素材，当前为占位。
-->



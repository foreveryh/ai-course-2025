<script setup>
import StrategyModal from './StrategyModal.vue';

// 写入策略数据
const writingStrategy = {
  title: "写入",
  emoji: "📝",
  purpose: "把任务的目标、对象、约束、已知事实固定在对话里，减少瞎猜。",
  keyActions: [
    "建立\"工作区/事实库\"区块；让模型复述确认一次，保证记住。",
    "用变量锚点（如 {{time}} / {{audience}}）避免之后表述漂移。",
    "明确更新规则（新增/覆盖），保持一致口径。"
  ],
  template: `你现在处于【工作区】。先仅输出"已记住的关键信息表"，不要开始任务。

【目标】<一句话>
【对象】<收件人/用户画像/环境>
【约束】<时区/版次/风格/禁止事项>
【输入材料】<可为空，后续补充>
【输出格式】<结构/字数/语言>
【更新规则】若后续我发送【更新】块，则以最新为准覆盖同名字段；无关信息忽略。`,
  examples: [
    {
      title: "低做法：直接说\"写个确认邮件\" → 容易编造链接/时间。",
      content: ""
    },
    {
      title: "高做法（写入＋复述）：",
      content: `【目标】写会议确认邮件（中英双语）
【对象】Alice <alice@x.com>
【约束】8/20 15:00–15:30 CET；地点我发Meet；禁止虚构链接
【输出格式】≤120字，主题+正文；中英对照`
    }
  ]
};

// 选取策略数据
const selectionStrategy = {
  title: "选取",
  emoji: "🔍",
  purpose: "把\"信号\"限定为你提供的材料，屏蔽外部噪声与幻觉。",
  keyActions: [
    "用材料区包裹（如 ... 或《材料#1…》），并写明\"仅可引用材料区\"。",
    "要求逐条对应出处（段号/行号/条款号），不确定就标\"需查证\"。"
  ],
  template: `只依据【材料区】完成任务。不得使用外部知识；不得推断未出现的事实。
对每条结论，按"结论 → 证据出处(材料#号/段号)"格式列出；不确定请写"需查证：…"。

【材料区】
《材料#1》……
《材料#2》……`,
  examples: [
    {
      title: "法规问答（低做法）：",
      content: "问\"防火门要求？\" → 模型乱引条款。"
    },
    {
      title: "法规问答（高做法/选取）：",
      content: `任务：概括SBC201-2022版关于办公疏散走道防火门的要求。
仅用材料：<<贴入相关章节文本>>
输出：要点清单（结论→出处）；无法确认处标"需查证"。`
    },
    {
      title: "代码修复：",
      content: `仅根据下述报错和代码片段提出修复建议；不可编造API。
【报错】TypeError: createServerContext is not a function（/app/providers.tsx:12）
【环境】Next.js 14 / React 18 / Node 18.19
【片段】\`\`\`tsx … \`\`\`
输出：两种可行修法（变更点diff → 原因 → 可能副作用）`
    }
  ]
};

// 压缩策略数据
const compressionStrategy = {
  title: "压缩",
  emoji: "🗜️",
  purpose: "保住关键信息密度（高信噪比），节省上下文预算，方便后续推理/生成。",
  keyActions: [
    "要\"分层结构\"（H1/H2/要点/行动项），而不是口水摘要。",
    "强制长度与数量上限（例如\"≤150字、3条要点、每条≤20字\"）。",
    "优先级标记（Must/Should/Could 或 P0/P1/P2）。"
  ],
  template: `把【会议记录】压缩为：
1) TL;DR ≤80字
2) 三层大纲（不超过 8 行）
3) 行动项表：字段=Owner/DDL/依赖/风险；仅列 P0/P1
禁止形容词堆砌；不要新增信息。`,
  examples: [
    {
      title: "用户访谈10页纪要→一页决策",
      content: `输入：长纪要

输出预期：
• TL;DR（≤80字）
• 大纲：痛点/现方案/阻碍/机会
• 行动项表（P0两条、P1两条）`
    },
    {
      title: "需求池排序：",
      content: `对下列需求用 RICE 打分并排序；输出表格（ID/Reach/Impact/Confidence/Effort/Score），
每项解释≤15字；不确定用"需估算"。`
    }
  ]
};

// 隔离策略数据
const isolationStrategy = {
  title: "隔离",
  emoji: "🏗️",
  purpose: "让模型不要\"一口吃掉\"，把思考与产出分离，避免不同目标互相污染。",
  keyActions: [
    "阶段门：先产出\"计划/检查表\"，通过再继续；或明确\"本轮只做第N步\"。",
    "角色分工：作者/评审/编辑分阶段出场；每一轮只看上一轮产物。",
    "沙盒/草稿区：允许模型在草稿推理，但最终输出只放干净结果。"
  ],
  template: `阶段A=大纲师：仅输出文章大纲（H2≤5个，H3≤3个/节），不得写正文。
阶段B=作者：仅基于"阶段A最终大纲"写正文；不得新增章节。
如果未提供"阶段A最终大纲"，请回复："等待大纲"。`,
  examples: [
    {
      title: "第1轮（隔离计划）：",
      content: `产出《API 集成指南》的"目录+每节要回答的问题"。限制：≤120字/节。`
    },
    {
      title: "第2轮（正文）：",
      content: `仅按上轮目录写正文；缺数据处写"需补：字段X示例"。`
    },
    {
      title: "产品评审双人角：",
      content: `角色A=产品作者：给出方案(目标/用户/流程/边界/风控)。
角色B=评审官：仅基于A的方案提出不少于8条阻击问题，分"定位/可行性/合规/度量"四类。
输出先B后A：B提问清单 → A逐条回应与修订。`
    }
  ]
};
</script>

<template>
  <div>
    <div class="text-center mb-6">
      <h4 class="text-lg font-semibold mb-3">点击查看详细策略模板</h4>
      <div class="flex justify-center space-x-4">
        <div class="p-2 px-3 bg-blue-50 hover:bg-blue-100 rounded-lg transition-colors">
          <StrategyModal v-bind="writingStrategy" />
        </div>
        <div class="p-2 px-3 bg-green-50 hover:bg-green-100 rounded-lg transition-colors">
          <StrategyModal v-bind="selectionStrategy" />
        </div>
        <div class="p-2 px-3 bg-yellow-50 hover:bg-yellow-100 rounded-lg transition-colors">
          <StrategyModal v-bind="compressionStrategy" />
        </div>
        <div class="p-2 px-3 bg-purple-50 hover:bg-purple-100 rounded-lg transition-colors">
          <StrategyModal v-bind="isolationStrategy" />
        </div>
      </div>
    </div>

    <div class="grid grid-cols-2 gap-4">
      <div class="p-3 bg-blue-50 rounded-lg">
        <p class="font-semibold mb-2">📝 模拟"写入"</p>
        <ul class="list-disc list-inside text-sm">
          <li>在对话中明确建立工作空间</li>
          <li>要求模型"记住"关键信息</li>
          <li>使用结构化格式组织信息</li>
        </ul>
      </div>
      
      <div class="p-3 bg-green-50 rounded-lg">
        <p class="font-semibold mb-2">🔍 模拟"选取"</p>
        <ul class="list-disc list-inside text-sm">
          <li>明确指定需要关注的信息源</li>
          <li>引导模型聚焦相关内容</li>
          <li>使用问题链条逐步聚焦</li>
        </ul>
      </div>
      
      <div class="p-3 bg-yellow-50 rounded-lg">
        <p class="font-semibold mb-2">🗜️ 模拟"压缩"</p>
        <ul class="list-disc list-inside text-sm">
          <li>要求模型提供摘要或要点</li>
          <li>使用分层次的信息组织</li>
          <li>指定关键信息的优先级</li>
        </ul>
      </div>
      
      <div class="p-3 bg-purple-50 rounded-lg">
        <p class="font-semibold mb-2">🏗️ 模拟"隔离"</p>
        <ul class="list-disc list-inside text-sm">
          <li>将复杂任务分解为子步骤</li>
          <li>使用角色扮演分离不同视角</li>
          <li>明确任务边界和专注领域</li>
        </ul>
      </div>
    </div>
  </div>
</template>
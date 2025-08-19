---
---

# 模拟“隔离”策略

<div class="space-y-4">
  <div>
    <h3 class="font-semibold">目的：</h3>
    <p>让模型不要“一口吃掉”，把思考与产出分离，避免不同目标互相污染。</p>
  </div>
  <div>
    <h3 class="font-semibold">关键做法：</h3>
    <ul class="list-disc list-inside">
      <li>阶段门：先产出“计划/检查表”，通过再继续；或明确“本轮只做第N步”。</li>
      <li>角色分工：作者/评审/编辑分阶段出场；每一轮只看上一轮产物。</li>
      <li>沙盒/草稿区：允许模型在草稿推理，但最终输出只放干净结果。</li>
    </ul>
  </div>
  <div>
    <h3 class="font-semibold">可复制模板（两段式写作）：</h3>
    <div class="bg-gray-100 p-4 rounded">
      <pre>阶段A=大纲师：仅输出文章大纲（H2≤5个，H3≤3个/节），不得写正文。
阶段B=作者：仅基于"阶段A最终大纲"写正文；不得新增章节。
如果未提供"阶段A最终大纲"，请回复："等待大纲"。</pre>
    </div>
  </div>
  <div>
    <h3 class="font-semibold">小例子（技术文档）：</h3>
    <p><strong>第1轮（隔离计划）：</strong></p>
    <pre class="bg-gray-100 p-4 rounded">产出《API 集成指南》的“目录+每节要回答的问题”。限制：≤120字/节。</pre>
    <p><strong>第2轮（正文）：</strong></p>
    <pre class="bg-gray-100 p-4 rounded">仅按上轮目录写正文；缺数据处写“需补：字段X示例”。</pre>
  </div>
  <div>
    <h3 class="font-semibold">小例子（产品评审双人角）：</h3>
    <pre class="bg-gray-100 p-4 rounded">角色A=产品作者：给出方案(目标/用户/流程/边界/风控)。
角色B=评审官：仅基于A的方案提出不少于8条阻击问题，分“定位/可行性/合规/度量”四类。
输出先B后A：B提问清单 → A逐条回应与修订。</pre>
  </div>
</div>

---
---

# 模拟“选取”策略

<div class="space-y-4">
  <div>
    <h3 class="font-semibold">目的：</h3>
    <p>把“信号”限定为你提供的材料，屏蔽外部噪声与幻觉。</p>
  </div>
  <div>
    <h3 class="font-semibold">关键做法：</h3>
    <ul class="list-disc list-inside">
      <li>用材料区包裹（如 ... 或《材料#1…》），并写明<strong>“仅可引用材料区”</strong>。</li>
      <li>要求逐条对应出处（段号/行号/条款号），不确定就标“需查证”。</li>
    </ul>
  </div>
  <div>
    <h3 class="font-semibold">可复制模板：</h3>
    <div class="bg-gray-100 p-4 rounded">
      <pre>只依据【材料区】完成任务。不得使用外部知识；不得推断未出现的事实。
对每条结论，按"结论 → 证据出处(材料#号/段号)"格式列出；不确定请写"需查证：…"。

【材料区】
《材料#1》……
《材料#2》……</pre>
    </div>
  </div>
  <div>
    <h3 class="font-semibold">小例子（法规问答）：</h3>
    <p><strong>低做法：</strong>问“防火门要求？” → 模型乱引条款。</p>
    <p><strong>高做法（选取）：</strong></p>
    <div class="bg-gray-100 p-4 rounded">
      <pre>任务：概括SBC201-2022版关于办公疏散走道防火门的要求。
仅用材料：&lt;&lt;贴入相关章节文本&gt;&gt;
输出：要点清单（结论→出处）；无法确认处标"需查证"。</pre>
    </div>
  </div>
  <div>
    <h3 class="font-semibold">小例子（代码修复）：</h3>
    <div class="bg-gray-100 p-4 rounded">
      <pre>仅根据下述报错和代码片段提出修复建议；不可编造API。
【报错】TypeError: createServerContext is not a function（/app/providers.tsx:12）
【环境】Next.js 14 / React 18 / Node 18.19
【片段】```tsx … ```
输出：两种可行修法（变更点diff → 原因 → 可能副作用）</pre>
    </div>
  </div>
</div>

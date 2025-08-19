---
---

# 模拟“写入”策略

<div class="space-y-4">
  <div>
    <h3 class="font-semibold">目的：</h3>
    <p>把任务的目标、对象、约束、已知事实固定在对话里，减少瞎猜。</p>
  </div>
  <div>
    <h3 class="font-semibold">关键做法：</h3>
    <ul class="list-disc list-inside">
      <li>建立“工作区/事实库”区块；让模型复述确认一次，保证记住。</li>
      <li>用变量锚点（如 {{time}} / {{audience}}）避免之后表述漂移。</li>
      <li>明确更新规则（新增/覆盖），保持一致口径。</li>
    </ul>
  </div>
  <div>
    <h3 class="font-semibold">可复制模板：</h3>
    <div class="bg-gray-100 p-4 rounded">
      <pre>你现在处于【工作区】。先仅输出"已记住的关键信息表"，不要开始任务。

【目标】&lt;一句话&gt;
【对象】&lt;收件人/用户画像/环境&gt;
【约束】&lt;时区/版次/风格/禁止事项&gt;
【输入材料】&lt;可为空，后续补充&gt;
【输出格式】&lt;结构/字数/语言&gt;
【更新规则】若后续我发送【更新】块，则以最新为准覆盖同名字段；无关信息忽略。</pre>
    </div>
  </div>
  <div>
    <h3 class="font-semibold">小例子（会议确认邮件）：</h3>
    <p><strong>低做法：</strong>直接说“写个确认邮件” → 容易编造链接/时间。</p>
    <p><strong>高做法（写入＋复述）：</strong></p>
    <div class="bg-gray-100 p-4 rounded">
      <pre>【目标】写会议确认邮件（中英双语）
【对象】Alice &lt;alice@x.com&gt;
【约束】8/20 15:00–15:30 CET；地点我发Meet；禁止虚构链接
【输出格式】≤120字，主题+正文；中英对照</pre>
    </div>
  </div>
</div>

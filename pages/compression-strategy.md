---
---

# 模拟“压缩”策略

<div class="space-y-4">
  <div>
    <h3 class="font-semibold">目的：</h3>
    <p>保住关键信息密度（高信噪比），节省上下文预算，方便后续推理/生成。</p>
  </div>
  <div>
    <h3 class="font-semibold">关键做法：</h3>
    <ul class="list-disc list-inside">
      <li>要“分层结构”（H1/H2/要点/行动项），而不是口水摘要。</li>
      <li>强制长度与数量上限（例如“≤150字、3条要点、每条≤20字”）。</li>
      <li>优先级标记（Must/Should/Could 或 P0/P1/P2）。</li>
    </ul>
  </div>
  <div>
    <h3 class="font-semibold">可复制模板：</h3>
    <div class="bg-gray-100 p-4 rounded">
      <pre>把【会议记录】压缩为：
1) TL;DR ≤80字
2) 三层大纲（不超过 8 行）
3) 行动项表：字段=Owner/DDL/依赖/风险；仅列 P0/P1
禁止形容词堆砌；不要新增信息。</pre>
    </div>
  </div>
  <div>
    <h3 class="font-semibold">小例子（用户访谈10页纪要→一页决策）：</h3>
    <p><strong>输入：</strong>长纪要</p>
    <p><strong>输出预期：</strong></p>
    <ul class="list-disc list-inside">
      <li>TL;DR（≤80字）</li>
      <li>大纲：痛点/现方案/阻碍/机会</li>
      <li>行动项表（P0两条、P1两条）</li>
    </ul>
  </div>
  <div>
    <h3 class="font-semibold">小例子（需求池排序）：</h3>
    <div class="bg-gray-100 p-4 rounded">
      <pre>对下列需求用 RICE 打分并排序；输出表格（ID/Reach/Impact/Confidence/Effort/Score），
每项解释≤15字；不确定用"需估算"。</pre>
    </div>
  </div>
</div>

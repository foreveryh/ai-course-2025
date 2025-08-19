<template>
  <div>
    <ModalDetails
      title="链式思维（CoT）完整示例"
      :maxWidth="'900px'"
      :open="open"
      @update:open="val => (open = val)"
    >
      <template #trigger="{ open }">
        <button class="mt-2 px-3 py-1 bg-green-500 text-white rounded text-sm hover:bg-green-600" @click="open()">
          查看CoT示例
        </button>
      </template>

      <div class="space-y-6 leading-7">
        <section>
          <h2 class="text-xl font-semibold mb-4">链式思维推理示例</h2>
          
          <div class="mb-6">
            <h3 class="font-medium text-gray-700 mb-2">场景：产品定价策略分析</h3>
            <div class="bg-blue-50 p-4 rounded-lg">
              <h4 class="font-semibold mb-2">用户问题：</h4>
              <p class="mb-3">我们的SaaS产品目前月费99元，竞争对手定价79元和129元。我们应该调整价格吗？</p>
            </div>
          </div>

          <div class="mb-6">
            <h3 class="font-medium text-gray-700 mb-2">CoT提示词（可直接复制）：</h3>
            <div class="bg-gray-50 p-4 rounded-lg font-mono text-sm">
              <pre class="whitespace-pre-wrap">请分析我们的SaaS产品定价策略。在给出最终建议前，请按以下步骤推理：

1. 分析问题的关键要素
2. 评估当前定价相对于竞争对手的位置
3. 考虑可能的调价方案及其影响
4. 分析每个方案的利弊
5. 基于分析给出明确建议

背景信息：
- 我们产品：月费99元
- 竞争对手A：79元
- 竞争对手B：129元
- 需要考虑：用户留存、新用户获取、收入影响

如果信息不足以做出决策，请明确指出需要补充哪些数据。</pre>
            </div>
          </div>

          <div class="mb-6">
            <h3 class="font-medium text-gray-700 mb-2">期望的CoT回答结构：</h3>
            <div class="bg-green-50 p-4 rounded-lg">
              <div class="space-y-4">
                <div>
                  <h4 class="font-semibold text-green-700">1. 关键要素分析：</h4>
                  <p class="text-sm">• 当前定价处于中间位置<br>• 价格敏感度未知<br>• 产品差异化程度待评估</p>
                </div>
                
                <div>
                  <h4 class="font-semibold text-green-700">2. 竞争定位评估：</h4>
                  <p class="text-sm">• 比低价竞品高25%<br>• 比高价竞品低23%<br>• 定位相对平衡</p>
                </div>
                
                <div>
                  <h4 class="font-semibold text-green-700">3. 调价方案分析：</h4>
                  <p class="text-sm">• 方案A：降价至89元<br>• 方案B：维持99元<br>• 方案C：提价至109元</p>
                </div>
                
                <div>
                  <h4 class="font-semibold text-green-700">4. 利弊权衡：</h4>
                  <p class="text-sm">每个方案对用户获取、留存率、总收入的不同影响</p>
                </div>
                
                <div>
                  <h4 class="font-semibold text-green-700">5. 最终建议：</h4>
                  <p class="text-sm">基于分析给出具体的定价建议和实施步骤</p>
                </div>
                
                <div class="bg-yellow-100 p-3 rounded">
                  <h4 class="font-semibold text-orange-700">需要补充的信息：</h4>
                  <p class="text-sm">• 用户流失率数据<br>• 功能差异对比<br>• 目标用户画像</p>
                </div>
              </div>
            </div>
          </div>

          <div class="grid grid-cols-2 gap-4 mt-6">
            <div>
              <h3 class="font-medium text-blue-700 mb-2">CoT的优势</h3>
              <ul class="list-disc list-inside text-sm space-y-1">
                <li>推理过程透明可检查</li>
                <li>逻辑错误易于发现</li>
                <li>结论更加可信</li>
                <li>便于进一步讨论</li>
              </ul>
            </div>
            
            <div>
              <h3 class="font-medium text-purple-700 mb-2">适用场景</h3>
              <ul class="list-disc list-inside text-sm space-y-1">
                <li>商业决策分析</li>
                <li>技术方案比较</li>
                <li>问题诊断排查</li>
                <li>复杂计算推理</li>
              </ul>
            </div>
          </div>
        </section>
      </div>
    </ModalDetails>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const open = ref(false)
</script>
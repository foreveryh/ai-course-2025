<template>
  <div>
    <ModalDetails
      title="负面约束示例与改进建议"
      :maxWidth="'800px'"
      :open="open"
      @update:open="val => (open = val)"
    >
      <template #trigger="{ open }">
        <button class="mt-2 px-3 py-1 bg-red-500 text-white rounded text-sm hover:bg-red-600" @click="open()">
          查看负面约束示例
        </button>
      </template>

      <div class="space-y-6 leading-7">
        <section>
          <h2 class="text-xl font-semibold mb-4">不推荐的负面约束示例</h2>
          
          <div class="space-y-6">
            <div class="border-l-4 border-red-400 bg-red-50 p-4 rounded-r-lg">
              <h3 class="font-semibold text-red-700 mb-2">1. 内容风格类负面约束</h3>
              <div class="grid grid-cols-1 gap-3">
                <div>
                  <p class="text-red-600 mb-1"><strong>❌ 不要啰嗦</strong></p>
                  <p class="text-green-600"><strong>✅ 改进：</strong>每个要点控制在20字以内，总结不超过3段</p>
                </div>
                <div>
                  <p class="text-red-600 mb-1"><strong>❌ 不要使用复杂术语</strong></p>
                  <p class="text-green-600"><strong>✅ 改进：</strong>使用12岁学生能理解的日常用语</p>
                </div>
                <div>
                  <p class="text-red-600 mb-1"><strong>❌ 不要写得太学术化</strong></p>
                  <p class="text-green-600"><strong>✅ 改进：</strong>采用对话式语气，多举实际案例</p>
                </div>
              </div>
            </div>

            <div class="border-l-4 border-red-400 bg-red-50 p-4 rounded-r-lg">
              <h3 class="font-semibold text-red-700 mb-2">2. 格式要求类负面约束</h3>
              <div class="grid grid-cols-1 gap-3">
                <div>
                  <p class="text-red-600 mb-1"><strong>❌ 不要使用项目符号</strong></p>
                  <p class="text-green-600"><strong>✅ 改进：</strong>使用编号列表(1.2.3.)或段落形式组织内容</p>
                </div>
                <div>
                  <p class="text-red-600 mb-1"><strong>❌ 不要超过500字</strong></p>
                  <p class="text-green-600"><strong>✅ 改进：</strong>控制在400-450字之间，重点突出</p>
                </div>
                <div>
                  <p class="text-red-600 mb-1"><strong>❌ 不要分段太多</strong></p>
                  <p class="text-green-600"><strong>✅ 改进：</strong>组织为3-4个主要段落，每段80-120字</p>
                </div>
              </div>
            </div>

            <div class="border-l-4 border-red-400 bg-red-50 p-4 rounded-r-lg">
              <h3 class="font-semibold text-red-700 mb-2">3. 内容范围类负面约束</h3>
              <div class="grid grid-cols-1 gap-3">
                <div>
                  <p class="text-red-600 mb-1"><strong>❌ 不要涉及政治话题</strong></p>
                  <p class="text-green-600"><strong>✅ 改进：</strong>专注于技术和商业层面的分析</p>
                </div>
                <div>
                  <p class="text-red-600 mb-1"><strong>❌ 不要提及竞争对手</strong></p>
                  <p class="text-green-600"><strong>✅ 改进：</strong>重点介绍我们的优势功能和独特价值</p>
                </div>
                <div>
                  <p class="text-red-600 mb-1"><strong>❌ 不要讨论价格</strong></p>
                  <p class="text-green-600"><strong>✅ 改进：</strong>着重说明产品价值和ROI收益</p>
                </div>
              </div>
            </div>

            <div class="border-l-4 border-red-400 bg-red-50 p-4 rounded-r-lg">
              <h3 class="font-semibold text-red-700 mb-2">4. 行为方式类负面约束</h3>
              <div class="grid grid-cols-1 gap-3">
                <div>
                  <p class="text-red-600 mb-1"><strong>❌ 不要编造数据</strong></p>
                  <p class="text-green-600"><strong>✅ 改进：</strong>仅使用提供的真实数据，不确定时标注"需验证"</p>
                </div>
                <div>
                  <p class="text-red-600 mb-1"><strong>❌ 不要回避问题</strong></p>
                  <p class="text-green-600"><strong>✅ 改进：</strong>直接回答核心问题，如无法确定则说明原因</p>
                </div>
                <div>
                  <p class="text-red-600 mb-1"><strong>❌ 不要重复我说的话</strong></p>
                  <p class="text-green-600"><strong>✅ 改进：</strong>基于我的要求，提供新的分析和见解</p>
                </div>
              </div>
            </div>
          </div>

          <div class="mt-8 p-4 bg-blue-50 rounded-lg border-l-4 border-blue-400">
            <h3 class="font-semibold text-blue-700 mb-2">为什么负面约束效果不佳？</h3>
            <ul class="list-disc list-inside text-sm space-y-1">
              <li><strong>认知负担：</strong>模型需要先理解"不要做什么"，再推断"应该做什么"</li>
              <li><strong>模糊边界：</strong>"不要啰嗦"没有明确标准，难以执行</li>
              <li><strong>反向强化：</strong>强调"不要X"可能让模型更关注X</li>
              <li><strong>缺乏指导：</strong>只说禁止，没有提供明确的替代方案</li>
            </ul>
          </div>

          <div class="mt-4 p-4 bg-green-50 rounded-lg border-l-4 border-green-400">
            <h3 class="font-semibold text-green-700 mb-2">正面指令的优势</h3>
            <ul class="list-disc list-inside text-sm space-y-1">
              <li><strong>明确标准：</strong>提供具体可执行的指标和要求</li>
              <li><strong>积极引导：</strong>直接告诉模型期望的行为和输出</li>
              <li><strong>减少误解：</strong>避免因理解偏差导致的错误输出</li>
              <li><strong>提升效率：</strong>减少修正和重新生成的需要</li>
            </ul>
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
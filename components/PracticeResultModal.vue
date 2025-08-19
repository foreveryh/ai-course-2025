<script setup>
import { ref } from 'vue'

const isOpen = ref(false)

// 打开模态框
const openModal = () => {
  isOpen.value = true
}

// 关闭模态框
const closeModal = () => {
  isOpen.value = false
}

defineExpose({
  openModal
})
</script>

<template>
  <div>
    <!-- 触发按钮 -->
    <slot name="trigger">
      <button
        @click="openModal"
        class="px-4 py-2 bg-blue-500 hover:bg-blue-600 text-white rounded transition-colors"
      >
        查看最佳实践
      </button>
    </slot>

    <!-- 模态框 -->
    <div
      v-if="isOpen"
      class="fixed inset-0 bg-black bg-opacity-50 flex items-start justify-center z-50 p-4 overflow-y-auto"
      style="padding-top: 5vh;"
    >
      <div class="bg-white rounded-lg shadow-lg w-full max-w-2xl max-h-[90vh] overflow-y-auto my-4 relative">
        <!-- 模态框头部 -->
        <div class="p-6 border-b border-gray-200">
          <div class="flex justify-between items-center">
            <h3 class="text-xl font-semibold flex items-center gap-2">
              <span class="text-blue-500">✨</span>
              <span>最佳实践：明确任务目标</span>
            </h3>
            <button
              @click="closeModal"
              class="text-gray-400 hover:text-gray-600 text-2xl font-bold focus:outline-none"
            >
              ✕
            </button>
          </div>
        </div>

        <!-- 模态框内容 -->
        <div class="p-6 space-y-5">
          <div class="space-y-4">
            <h4 class="font-semibold text-gray-700">原始模糊提示词</h4>
            <div class="p-4 bg-red-50 rounded border-l-4 border-red-400">
              <code class="text-lg">"帮我写个产品介绍"</code>
            </div>
            
            <h4 class="font-semibold text-gray-700 mt-6">优化后提示词</h4>
            <div class="p-4 bg-green-50 rounded border-l-4 border-green-400">
              <div class="whitespace-pre-wrap text-sm">请为面向中小企业财务经理的SaaS财务软件「FinanceEase Pro」撰写一份产品介绍。

要求：
1. 长度：300-400字
2. 语气：专业、可信，但平易近人
3. 结构：
   - 开头：说明财务管理痛点（时间浪费、错误率）
   - 中部：介绍3个核心功能（自动化账单、财务报表、税务预测）
   - 结尾：包含免费试用的行动召唤

必须包含：ROI数据点、与传统软件的对比、一个简短客户案例</div>
            </div>
          </div>

          <div class="mt-8 space-y-3">
            <h4 class="font-semibold text-gray-700">提示词优化解析</h4>
            
            <div class="grid grid-cols-2 gap-4">
              <div class="p-3 bg-blue-50 rounded-lg">
                <p class="font-medium text-blue-800 mb-2">任务明确化</p>
                <ul class="list-disc list-inside text-sm text-gray-700">
                  <li>具体产品名称和类型</li>
                  <li>明确的目标受众</li>
                  <li>具体的文档类型（产品介绍）</li>
                </ul>
              </div>
              
              <div class="p-3 bg-purple-50 rounded-lg">
                <p class="font-medium text-purple-800 mb-2">输出规范化</p>
                <ul class="list-disc list-inside text-sm text-gray-700">
                  <li>明确的字数限制</li>
                  <li>具体的语气要求</li>
                  <li>结构化的内容组织</li>
                </ul>
              </div>
              
              <div class="p-3 bg-green-50 rounded-lg">
                <p class="font-medium text-green-800 mb-2">内容丰富化</p>
                <ul class="list-disc list-inside text-sm text-gray-700">
                  <li>核心功能的具体要点</li>
                  <li>必须包含的关键要素</li>
                  <li>特定的数据点和对比</li>
                </ul>
              </div>
              
              <div class="p-3 bg-yellow-50 rounded-lg">
                <p class="font-medium text-yellow-800 mb-2">受众针对性</p>
                <ul class="list-disc list-inside text-sm text-gray-700">
                  <li>面向特定职业角色</li>
                  <li>行业特定的痛点</li>
                  <li>针对性的解决方案</li>
                </ul>
              </div>
            </div>
          </div>
          
          <div class="mt-6 p-4 bg-indigo-50 rounded-lg border-l-4 border-indigo-400">
            <h4 class="font-semibold text-indigo-800 mb-2">提示词公式</h4>
            <p class="text-gray-700">产品介绍 = [目标受众] + [产品名称/类型] + [内容结构] + [语气] + [长度] + [必须包含元素]</p>
          </div>
        </div>

        <!-- 模态框底部 -->
        <div class="p-6 border-t border-gray-200 flex justify-end">
          <button
            @click="closeModal"
            class="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600 focus:outline-none"
          >
            关闭
          </button>
        </div>
      </div>
    </div>
  </div>
</template>
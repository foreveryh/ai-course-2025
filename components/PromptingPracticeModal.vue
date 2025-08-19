<template>
  <div>
    <ModalDetails
      title="提示词优化最佳实践"
      :maxWidth="'800px'"
      :open="open"
      @update:open="val => (open = val)"
    >
      <template #trigger="{ open }">
        <button class="px-4 py-2 bg-blue-500 hover:bg-blue-600 text-white rounded transition-colors" @click="open()">
          查看最佳实践
        </button>
      </template>

      <div class="space-y-6 leading-7">
        <section>
          <h2 class="text-xl font-semibold mb-4">提示词优化示例</h2>
          
          <div class="mb-6">
            <h3 class="font-medium text-gray-700">原始模糊提示词</h3>
            <div class="bg-red-50 p-4 rounded-lg mt-2">
              <p>"帮我写个产品介绍"</p>
            </div>
          </div>
          
          <div class="mb-6">
            <h3 class="font-medium text-gray-700">优化后提示词</h3>
            <div class="bg-green-50 p-4 rounded-lg mt-2">
              <div>
                请为面向中小企业财务经理的SaaS财务软件「FinanceEase Pro」撰写一份产品介绍。
                <br><br>
                要求：<br>
                1. 长度：300-400字<br>
                2. 语气：专业、可信，但平易近人<br>
                3. 结构：<br>
                &nbsp;&nbsp; - 开头：说明财务管理痛点（时间浪费、错误率）<br>
                &nbsp;&nbsp; - 中部：介绍3个核心功能（自动化账单、财务报表、税务预测）<br>
                &nbsp;&nbsp; - 结尾：包含免费试用的行动召唤<br>
                <br>
                必须包含：ROI数据点、与传统软件的对比、一个简短客户案例
              </div>
            </div>
          </div>

          <div class="grid grid-cols-2 gap-4">
            <div>
              <h3 class="font-medium text-blue-700 mb-2">提示词优化解析</h3>
              <ul class="list-disc list-inside text-sm space-y-1">
                <li>明确了具体产品和目标受众</li>
                <li>设定了明确的字数和语气要求</li>
                <li>提供了结构化的内容组织框架</li>
                <li>指定了必须包含的关键要素</li>
              </ul>
            </div>
            
            <div>
              <h3 class="font-medium text-indigo-700 mb-2">提示词公式</h3>
              <div class="bg-indigo-50 p-3 rounded-lg text-sm">
                <p>产品介绍 = 目标受众 + 产品名称/类型 + 内容结构 + 语气 + 长度 + 必须包含元素</p>
              </div>
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
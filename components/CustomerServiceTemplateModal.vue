<template>
  <div class="mt-4">
    <ModalDetails
      title="客服分类提示词模板"
      :maxWidth="'800px'"
      :open="open"
      @update:open="val => (open = val)"
    >
      <template #trigger="{ open }">
        <button class="mt-2 px-3 py-1 bg-blue-500 text-white rounded text-sm hover:bg-blue-600" @click="open()">
          查看模板
        </button>
      </template>

      <div class="space-y-6 leading-7">
        <section>
          <h2 class="text-xl font-semibold mb-4">客服反馈自动分类模板</h2>
          
          <div class="bg-gray-50 dark:bg-gray-800 p-4 rounded-lg">
            <h3 class="font-semibold mb-3">### 指令</h3>
            <p class="mb-4">请依照示例风格完成新样本</p>
            
            <h3 class="font-semibold mb-3">### 示例</h3>
            <div class="space-y-3">
              <div class="border-l-4 border-blue-500 pl-3">
                <p><strong>[输入]</strong> 用户投诉：App经常崩溃，影响工作</p>
                <p><strong>[输出]</strong> 类型：技术问题 | 优先级：高 | 回复：感谢反馈，我们将在24小时内修复...</p>
              </div>
              
              <div class="border-l-4 border-green-500 pl-3">
                <p><strong>[输入]</strong> 用户建议：希望增加夜间模式</p>
                <p><strong>[输出]</strong> 类型：功能建议 | 优先级：中 | 回复：好建议！已记录到产品规划...</p>
              </div>
              
              <div class="border-l-4 border-orange-500 pl-3">
                <p><strong>[输入]</strong> 用户咨询：如何修改个人资料？</p>
                <p><strong>[输出]</strong> 类型：使用咨询 | 优先级：中 | 回复：请进入设置页面，点击个人资料...</p>
              </div>
            </div>
            
            <h3 class="font-semibold mb-3 mt-6">### 现在开始</h3>
            <p><strong>[输入]</strong> {{你的新输入}}</p>
          </div>
          
          <div class="mt-6 p-4 bg-blue-50 dark:bg-blue-900/20 rounded-lg">
            <h4 class="font-semibold mb-2">💡 使用技巧</h4>
            <ul class="list-disc pl-5 space-y-1 text-sm">
              <li>确保示例覆盖主要的分类类型</li>
              <li>保持输出格式的一致性</li>
              <li>优先级设定要有明确标准</li>
              <li>回复模板要符合品牌语气</li>
            </ul>
          </div>
        </section>
      </div>
    </ModalDetails>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import ModalDetails from './ModalDetails.vue'
const open = ref(false)
</script>

<style scoped></style>
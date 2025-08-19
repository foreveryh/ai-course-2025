<script setup>
import { ref } from 'vue'

// 定义props
const props = defineProps({
  title: {
    type: String,
    required: true
  },
  emoji: {
    type: String,
    default: '📝'
  },
  purpose: {
    type: String,
    required: true
  },
  keyActions: {
    type: Array,
    default: () => []
  },
  template: {
    type: String,
    default: ''
  },
  examples: {
    type: Array,
    default: () => []
  }
})

// 控制模态框显示状态
const isOpen = ref(false)

// 打开模态框
const openModal = () => {
  isOpen.value = true
}

// 关闭模态框
const closeModal = () => {
  isOpen.value = false
}
</script>

<template>
  <div>
    <!-- 触发按钮 -->
    <button 
      @click="openModal" 
      class="text-blue-500 hover:text-blue-700 hover:underline flex items-center gap-1"
    >
      <span>{{ emoji }} {{ title }}</span>
    </button>

    <!-- 模态框 -->
    <div 
      v-if="isOpen" 
      class="fixed inset-0 bg-black bg-opacity-50 flex items-start justify-center z-50 p-4 overflow-y-auto"
      style="padding-top: 5vh;"
    >
      <div class="bg-white rounded-lg shadow-lg w-full max-w-xl max-h-[90vh] overflow-y-auto my-4 relative">
        <!-- 模态框头部 -->
        <div class="p-6 border-b border-gray-200">
          <div class="flex justify-between items-center">
            <h3 class="text-2xl font-semibold flex items-center gap-2">
              <span>{{ emoji }}</span>
              <span>模拟"{{ title }}"策略</span>
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
        <div class="p-6 space-y-6">
          <!-- 目的 -->
          <div>
            <h4 class="font-semibold">目的：</h4>
            <p>{{ purpose }}</p>
          </div>

          <!-- 关键做法 -->
          <div v-if="keyActions.length">
            <h4 class="font-semibold">关键做法：</h4>
            <ul class="list-disc list-inside">
              <li v-for="(action, index) in keyActions" :key="index">
                {{ action }}
              </li>
            </ul>
          </div>

          <!-- 可复制模板 -->
          <div v-if="template">
            <h4 class="font-semibold">可复制模板：</h4>
            <div class="bg-gray-100 p-4 rounded">
              <pre>{{ template }}</pre>
            </div>
          </div>

          <!-- 小例子 -->
          <div v-if="examples.length">
            <h4 class="font-semibold">小例子：</h4>
            <div v-for="(example, index) in examples" :key="index" class="mt-3">
              <p v-if="example.title" class="text-sm font-medium"><strong>{{ example.title }}</strong></p>
              <div v-if="example.content" class="bg-gray-100 p-3 rounded mt-1 max-h-[30vh] overflow-y-auto">
                <pre class="text-sm whitespace-pre-wrap">{{ example.content }}</pre>
              </div>
            </div>
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
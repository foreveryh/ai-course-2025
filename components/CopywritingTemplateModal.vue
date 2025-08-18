<template>
  <div class="mt-4">
    <ModalDetails
      title="文案风格提示词模板"
      :maxWidth="'800px'"
      :open="open"
      @update:open="val => (open = val)"
    >
      <template #trigger="{ open }">
        <button class="mt-2 px-3 py-1 bg-green-500 text-white rounded text-sm hover:bg-green-600" @click="open()">
          查看模板
        </button>
      </template>

      <div class="space-y-6 leading-7">
        <section>
          <h2 class="text-xl font-semibold mb-4">品牌文案风格模板</h2>
          
          <div class="bg-gray-50 dark:bg-gray-800 p-4 rounded-lg">
            <h3 class="font-semibold mb-3">### 指令</h3>
            <p class="mb-4">按照示例风格为产品写宣传文案</p>
            
            <h3 class="font-semibold mb-3">### 示例</h3>
            <div class="space-y-3">
              <div class="border-l-4 border-green-500 pl-3">
                <p><strong>[产品]</strong> 智能手表</p>
                <p><strong>[文案]</strong> 💪 让每一次心跳都有意义！智能监测，陪伴你的健康每一天</p>
              </div>
              
              <div class="border-l-4 border-purple-500 pl-3">
                <p><strong>[产品]</strong> 降噪耳机</p>
                <p><strong>[文案]</strong> 🎵 沉浸纯净音世界！一键隔绝喧嚣，只留美妙旋律</p>
              </div>
              
              <div class="border-l-4 border-blue-500 pl-3">
                <p><strong>[产品]</strong> 无线充电器</p>
                <p><strong>[文案]</strong> ⚡ 告别线缆束缚！轻放即充，科技让生活更自由</p>
              </div>
              
              <div class="border-l-4 border-red-500 pl-3">
                <p><strong>[产品]</strong> 智能摄像头</p>
                <p><strong>[文案]</strong> 👁️ 守护每个重要时刻！AI识别，让安全看得见</p>
              </div>
            </div>
            
            <h3 class="font-semibold mb-3 mt-6">### 现在开始</h3>
            <p><strong>[产品]</strong> {{新产品名称}}</p>
          </div>
          
          <div class="mt-6 p-4 bg-green-50 dark:bg-green-900/20 rounded-lg">
            <h4 class="font-semibold mb-2">🎨 风格特点</h4>
            <ul class="list-disc pl-5 space-y-1 text-sm">
              <li><strong>情感化</strong>：用emoji增强情感表达</li>
              <li><strong>简洁有力</strong>：一句话概括核心价值</li>
              <li><strong>场景化</strong>：突出使用场景和体验</li>
              <li><strong>行动导向</strong>：激发用户购买欲望</li>
            </ul>
          </div>
          
          <div class="mt-4 p-4 bg-yellow-50 dark:bg-yellow-900/20 rounded-lg">
            <h4 class="font-semibold mb-2">✅ 使用建议</h4>
            <ul class="list-disc pl-5 space-y-1 text-sm">
              <li>根据目标受众调整语气（年轻化/商务/家庭）</li>
              <li>突出产品独特卖点而非通用功能</li>
              <li>控制文案长度，移动端友好</li>
              <li>A/B测试不同风格的转化效果</li>
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
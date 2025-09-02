<template>
  <div class="mt-4">
    <ModalDetails title="AI Agent 能力演示" :maxWidth="'800px'" :open="open" @update:open="val => open = val">
      <template #trigger="{ open }">
        <button class="px-4 py-2 rounded bg-cyan-600 text-white hover:bg-cyan-700 transition-colors" @click="open()">
          体验 Agent 交互演示
        </button>
      </template>

      <div class="space-y-6 leading-7">
        <section>
          <h2 class="text-xl font-semibold mb-4">🤖 AI Agent vs 传统AI 对比演示</h2>
          
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <!-- 传统AI -->
            <div class="border rounded-lg p-4 bg-gray-50">
              <h3 class="font-semibold text-gray-700 mb-3 flex items-center gap-2">
                <span class="w-3 h-3 bg-gray-400 rounded-full"></span>
                传统 AI 模式
              </h3>
              
              <div class="space-y-3 text-sm">
                <div class="bg-white rounded p-3 border-l-4 border-gray-400">
                  <p class="font-semibold">用户：</p>
                  <p>帮我制定去日本的旅行计划</p>
                </div>
                
                <div class="bg-blue-50 rounded p-3 border-l-4 border-blue-400">
                  <p class="font-semibold">AI：</p>
                  <p>我可以为您提供一些日本旅行的建议：</p>
                  <ul class="mt-2 list-disc pl-5 space-y-1">
                    <li>推荐城市：东京、京都、大阪</li>
                    <li>必去景点：浅草寺、清水寺、环球影城</li>
                    <li>美食推荐：寿司、拉面、和牛</li>
                    <li>交通：建议购买JR Pass</li>
                  </ul>
                  <p class="mt-2 text-gray-600">注：以上信息基于训练数据，可能不是最新情况</p>
                </div>
              </div>
              
              <div class="mt-4 text-xs text-gray-500">
                ❌ 无法获取实时信息<br>
                ❌ 无法个性化定制<br>
                ❌ 无法执行具体操作
              </div>
            </div>

            <!-- AI Agent -->
            <div class="border rounded-lg p-4 bg-green-50">
              <h3 class="font-semibold text-green-700 mb-3 flex items-center gap-2">
                <span class="w-3 h-3 bg-green-500 rounded-full"></span>
                AI Agent 模式
              </h3>
              
              <div class="space-y-3 text-sm">
                <div class="bg-white rounded p-3 border-l-4 border-gray-400">
                  <p class="font-semibold">用户：</p>
                  <p>帮我制定去日本的旅行计划</p>
                </div>
                
                <div class="bg-yellow-50 rounded p-3 border-l-4 border-yellow-400">
                  <p class="font-semibold">Agent 思考：</p>
                  <p>需要了解用户的具体需求，获取实时信息</p>
                </div>
                
                <div class="bg-green-100 rounded p-3 border-l-4 border-green-400">
                  <p class="font-semibold">Agent 询问：</p>
                  <p>为了给您最好的建议，请告诉我：</p>
                  <ul class="mt-1 list-disc pl-5">
                    <li>计划什么时候去？停留几天？</li>
                    <li>预算大概多少？</li>
                    <li>主要兴趣是什么？</li>
                  </ul>
                </div>
                
                <div class="bg-white rounded p-3 border-l-4 border-gray-400">
                  <p class="font-semibold">用户补充：</p>
                  <p>下个月去5天，预算1.5万，喜欢文化和美食</p>
                </div>
                
                <div class="bg-blue-100 rounded p-3 border-l-4 border-blue-400">
                  <p class="font-semibold">Agent 行动：</p>
                  <p>🔍 正在获取下月日本天气信息...</p>
                  <p>✈️ 正在查询机票价格...</p>
                  <p>🏨 正在推荐合适的住宿...</p>
                  <p>🍜 正在搜索当地特色餐厅...</p>
                </div>
              </div>
              
              <div class="mt-4 text-xs text-green-600">
                ✅ 实时信息获取<br>
                ✅ 个性化深度定制<br>
                ✅ 端到端解决方案
              </div>
            </div>
          </div>
        </section>

        <hr class="border-gray-200" />

        <section>
          <h2 class="text-xl font-semibold mb-4">🛠️ Agent 工具集成能力演示</h2>
          
          <div class="bg-gray-50 rounded-lg p-4">
            <h3 class="font-semibold mb-3">场景：智能客服助手</h3>
            
            <div class="space-y-4">
              <div class="flex items-start gap-3">
                <div class="w-8 h-8 bg-blue-500 rounded-full flex items-center justify-center text-white text-sm font-bold">1</div>
                <div class="flex-1">
                  <p class="font-semibold">接收用户问题</p>
                  <p class="text-sm text-gray-600">"我的订单什么时候发货？订单号：ABC123"</p>
                </div>
              </div>
              
              <div class="flex items-start gap-3">
                <div class="w-8 h-8 bg-green-500 rounded-full flex items-center justify-center text-white text-sm font-bold">2</div>
                <div class="flex-1">
                  <p class="font-semibold">自动调用订单系统API</p>
                  <p class="text-sm text-gray-600">查询订单状态、物流信息</p>
                </div>
              </div>
              
              <div class="flex items-start gap-3">
                <div class="w-8 h-8 bg-purple-500 rounded-full flex items-center justify-center text-white text-sm font-bold">3</div>
                <div class="flex-1">
                  <p class="font-semibold">调用物流跟踪API</p>
                  <p class="text-sm text-gray-600">获取实时物流状态</p>
                </div>
              </div>
              
              <div class="flex items-start gap-3">
                <div class="w-8 h-8 bg-orange-500 rounded-full flex items-center justify-center text-white text-sm font-bold">4</div>
                <div class="flex-1">
                  <p class="font-semibold">智能分析与回复</p>
                  <p class="text-sm text-gray-600">综合信息生成个性化回复</p>
                </div>
              </div>
            </div>
            
            <div class="mt-4 bg-white rounded p-3 border-l-4 border-blue-400">
              <p class="font-semibold">Agent 回复：</p>
              <p class="text-sm mt-1">您好！订单ABC123已于昨天打包完成，预计今天下午发货。使用顺丰快递，预计2-3天送达。您可以通过快递单号SF123456789跟踪物流状态。如有其他问题，随时联系我！</p>
            </div>
          </div>
        </section>

        <section>
          <h2 class="text-xl font-semibold mb-4">🧠 学习与适应能力演示</h2>
          
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="bg-blue-50 rounded-lg p-4">
              <h3 class="font-semibold text-blue-700 mb-2">📈 持续学习</h3>
              <ul class="text-sm space-y-2">
                <li class="flex items-start gap-2">
                  <span class="text-blue-500">•</span>
                  <span>记住用户偏好和习惯</span>
                </li>
                <li class="flex items-start gap-2">
                  <span class="text-blue-500">•</span>
                  <span>从对话历史中学习上下文</span>
                </li>
                <li class="flex items-start gap-2">
                  <span class="text-blue-500">•</span>
                  <span>根据反馈调整回复风格</span>
                </li>
                <li class="flex items-start gap-2">
                  <span class="text-blue-500">•</span>
                  <span>优化工具使用策略</span>
                </li>
              </ul>
            </div>
            
            <div class="bg-green-50 rounded-lg p-4">
              <h3 class="font-semibold text-green-700 mb-2">🎯 智能适应</h3>
              <ul class="text-sm space-y-2">
                <li class="flex items-start gap-2">
                  <span class="text-green-500">•</span>
                  <span>根据用户类型调整交互方式</span>
                </li>
                <li class="flex items-start gap-2">
                  <span class="text-green-500">•</span>
                  <span>自动切换正式/非正式语言风格</span>
                </li>
                <li class="flex items-start gap-2">
                  <span class="text-green-500">•</span>
                  <span>动态选择最合适的工具</span>
                </li>
                <li class="flex items-start gap-2">
                  <span class="text-green-500">•</span>
                  <span>预测用户可能的后续需求</span>
                </li>
              </ul>
            </div>
          </div>
        </section>

        <section class="mt-6">
          <div class="bg-gradient-to-r from-cyan-50 to-blue-50 rounded-lg p-4 border-l-4 border-cyan-400">
            <h3 class="font-semibold text-cyan-800 mb-2">💡 Agent 的核心优势</h3>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-4 text-sm">
              <div class="text-center">
                <div class="text-2xl mb-2">🧠</div>
                <div class="font-semibold">智能推理</div>
                <div class="text-gray-600">多步思考，逻辑清晰</div>
              </div>
              <div class="text-center">
                <div class="text-2xl mb-2">🔗</div>
                <div class="font-semibold">工具集成</div>
                <div class="text-gray-600">无缝连接各种服务</div>
              </div>
              <div class="text-center">
                <div class="text-2xl mb-2">🎯</div>
                <div class="font-semibold">目标导向</div>
                <div class="text-gray-600">专注解决用户问题</div>
              </div>
            </div>
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
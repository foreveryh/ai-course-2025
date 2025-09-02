<template>
  <div class="mt-4">
    <ModalDetails title="ReAct 模式详细示例" :maxWidth="'900px'" :open="open" @update:open="val => open = val">
      <template #trigger="{ open }">
        <button class="px-4 py-2 rounded bg-purple-600 text-white hover:bg-purple-700 transition-colors" @click="open()">
          查看 ReAct 示例演示
        </button>
      </template>

      <div class="space-y-6 leading-7">
        <section>
          <h2 class="text-xl font-semibold mb-4">🎯 ReAct 模式核心流程</h2>
          <div class="bg-blue-50 rounded-lg p-4 border-l-4 border-blue-400">
            <p class="font-semibold">核心理念：</p>
            <p class="mt-2">将推理（Reasoning）和行动（Acting）交替进行，形成 <strong>思考→行动→观察</strong> 的动态循环</p>
          </div>
        </section>

        <section>
          <h2 class="text-xl font-semibold mb-4">📋 示例任务：智能投资顾问</h2>
          <div class="bg-gray-100 rounded-lg p-4">
            <p class="font-semibold">用户需求：</p>
            <p class="mt-2 italic">"我有5万元想投资，风险偏好中等，希望获得稳健收益，请推荐投资方案"</p>
          </div>
        </section>

        <hr class="border-gray-200" />

        <section>
          <h2 class="text-xl font-semibold mb-4">🔄 完整 ReAct 执行过程</h2>
          
          <div class="space-y-4">
            <!-- Cycle 1 -->
            <div class="border-2 border-yellow-200 rounded-lg p-4 bg-yellow-50">
              <h3 class="font-semibold text-yellow-800 mb-2">第一轮循环</h3>
              
              <div class="space-y-3">
                <div class="flex items-start gap-3">
                  <span class="bg-yellow-500 text-white px-2 py-1 rounded text-sm font-semibold">💭 Thought</span>
                  <div class="flex-1">
                    <p>用户想要投资建议，需要了解当前市场情况。首先获取股市和债市的基本信息，然后分析适合中等风险偏好的投资选项。</p>
                  </div>
                </div>

                <div class="flex items-start gap-3">
                  <span class="bg-green-500 text-white px-2 py-1 rounded text-sm font-semibold">🎯 Action</span>
                  <div class="flex-1">
                    <p><code>get_market_data("stock_index", "bond_yield", "fund_performance")</code></p>
                  </div>
                </div>

                <div class="flex items-start gap-3">
                  <span class="bg-blue-500 text-white px-2 py-1 rounded text-sm font-semibold">👀 Observation</span>
                  <div class="flex-1">
                    <p>市场数据获取成功：</p>
                    <ul class="mt-1 list-disc pl-5 text-sm">
                      <li>沪深300指数：当前3850点，年化波动率18%</li>
                      <li>10年期国债收益率：2.6%</li>
                      <li>混合型基金平均收益：近一年6.8%</li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>

            <!-- Cycle 2 -->
            <div class="border-2 border-purple-200 rounded-lg p-4 bg-purple-50">
              <h3 class="font-semibold text-purple-800 mb-2">第二轮循环</h3>
              
              <div class="space-y-3">
                <div class="flex items-start gap-3">
                  <span class="bg-yellow-500 text-white px-2 py-1 rounded text-sm font-semibold">💭 Thought</span>
                  <div class="flex-1">
                    <p>获得了市场基础数据，现在需要分析用户的风险偏好和投资期限。中等风险通常适合股债混合配置，让我搜索当前推荐的资产配置策略。</p>
                  </div>
                </div>

                <div class="flex items-start gap-3">
                  <span class="bg-green-500 text-white px-2 py-1 rounded text-sm font-semibold">🎯 Action</span>
                  <div class="flex-1">
                    <p><code>search_investment_strategy("moderate_risk", "50000_yuan", "asset_allocation")</code></p>
                  </div>
                </div>

                <div class="flex items-start gap-3">
                  <span class="bg-blue-500 text-white px-2 py-1 rounded text-sm font-semibold">👀 Observation</span>
                  <div class="flex-1">
                    <p>找到适合的配置建议：</p>
                    <ul class="mt-1 list-disc pl-5 text-sm">
                      <li>股票型基金：40-50%（追求成长收益）</li>
                      <li>债券型基金：30-40%（稳定收益）</li>
                      <li>货币基金：10-20%（流动性储备）</li>
                      <li>预期年化收益：6-9%</li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>

            <!-- Cycle 3 -->
            <div class="border-2 border-green-200 rounded-lg p-4 bg-green-50">
              <h3 class="font-semibold text-green-800 mb-2">第三轮循环</h3>
              
              <div class="space-y-3">
                <div class="flex items-start gap-3">
                  <span class="bg-yellow-500 text-white px-2 py-1 rounded text-sm font-semibold">💭 Thought</span>
                  <div class="flex-1">
                    <p>有了配置策略，现在需要推荐具体的产品。让我搜索当前表现优秀、费率合理的基金产品。</p>
                  </div>
                </div>

                <div class="flex items-start gap-3">
                  <span class="bg-green-500 text-white px-2 py-1 rounded text-sm font-semibold">🎯 Action</span>
                  <div class="flex-1">
                    <p><code>recommend_funds("stock_fund", "bond_fund", "money_fund", filters={"rating": "4+", "fee": "low"})</code></p>
                  </div>
                </div>

                <div class="flex items-start gap-3">
                  <span class="bg-blue-500 text-white px-2 py-1 rounded text-sm font-semibold">👀 Observation</span>
                  <div class="flex-1">
                    <p>推荐产品列表：</p>
                    <ul class="mt-1 list-disc pl-5 text-sm">
                      <li>易方达中小盘混合（股票型）：近三年年化12.3%</li>
                      <li>博时信用债纯债（债券型）：近三年年化4.8%</li>
                      <li>天弘余额宝（货币型）：七日年化2.3%</li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>

            <!-- Final Action -->
            <div class="border-2 border-blue-200 rounded-lg p-4 bg-blue-50">
              <h3 class="font-semibold text-blue-800 mb-2">最终行动</h3>
              
              <div class="flex items-start gap-3">
                <span class="bg-blue-600 text-white px-2 py-1 rounded text-sm font-semibold">🎯 Final Action</span>
                <div class="flex-1">
                  <p><code>generate_investment_plan(user_profile, market_data, recommended_products)</code></p>
                </div>
              </div>
            </div>
          </div>
        </section>

        <hr class="border-gray-200" />

        <section>
          <h2 class="text-xl font-semibold mb-4">📊 最终投资方案</h2>
          <div class="bg-gray-50 rounded-lg p-4">
            <h3 class="font-semibold mb-3">💰 5万元中等风险投资配置方案</h3>
            
            <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-4">
              <div class="bg-red-100 rounded p-3 text-center">
                <div class="text-lg font-bold text-red-700">45%</div>
                <div class="text-sm text-red-600">股票型基金</div>
                <div class="text-xs text-gray-600">22,500元</div>
              </div>
              <div class="bg-blue-100 rounded p-3 text-center">
                <div class="text-lg font-bold text-blue-700">35%</div>
                <div class="text-sm text-blue-600">债券型基金</div>
                <div class="text-xs text-gray-600">17,500元</div>
              </div>
              <div class="bg-green-100 rounded p-3 text-center">
                <div class="text-lg font-bold text-green-700">20%</div>
                <div class="text-sm text-green-600">货币基金</div>
                <div class="text-xs text-gray-600">10,000元</div>
              </div>
            </div>
            
            <div class="space-y-2 text-sm">
              <p><strong>预期年化收益：</strong>6.5% - 8.5%</p>
              <p><strong>风险等级：</strong>中等（3/5）</p>
              <p><strong>建议持有期：</strong>1-3年</p>
              <p><strong>定期调整：</strong>每季度根据市场情况重新平衡</p>
            </div>
          </div>
        </section>

        <section class="mt-6">
          <div class="bg-gradient-to-r from-purple-50 to-blue-50 rounded-lg p-4 border-l-4 border-purple-400">
            <h3 class="font-semibold text-purple-800 mb-2">🎯 ReAct 模式的价值体现</h3>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-sm">
              <div>
                <h4 class="font-semibold text-purple-700">💡 动态决策</h4>
                <ul class="text-purple-600 space-y-1">
                  <li>• 根据实时市场数据调整策略</li>
                  <li>• 基于搜索结果细化产品推荐</li>
                </ul>
              </div>
              <div>
                <h4 class="font-semibold text-blue-700">🔍 信息整合</h4>
                <ul class="text-blue-600 space-y-1">
                  <li>• 多源数据交叉验证</li>
                  <li>• 个性化方案定制</li>
                </ul>
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
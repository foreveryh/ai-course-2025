<template>
  <div v-if="modelValue" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50" @click="closeModal">
    <div class="bg-white rounded-lg max-w-4xl max-h-[80vh] overflow-y-auto p-6" @click.stop>
      <div class="flex justify-between items-center mb-4">
        <h2 class="text-2xl font-bold">🆚 ControlNet vs IP-Adapter 详细对比</h2>
        <button @click="closeModal" class="text-gray-500 hover:text-gray-700 text-2xl">&times;</button>
      </div>

      <div class="space-y-6">
        <!-- 核心差异 -->
        <section>
          <h3 class="text-xl font-semibold mb-3 text-blue-600">🎯 核心差异</h3>
          <div class="grid md:grid-cols-2 gap-4">
            <div class="border rounded p-4 bg-blue-50">
              <h4 class="font-bold text-blue-800 mb-2">ControlNet = "蓝图/GPS"</h4>
              <ul class="text-sm space-y-1">
                <li>• 结构/几何"硬控"</li>
                <li>• 参考图 → 条件图（边缘、姿态骨架、深度、法线等）</li>
                <li>• 像素对齐的条件在采样每一步把几何与布局"钉住"</li>
                <li>• 几何强约束（"这条线就该在这里"）</li>
              </ul>
            </div>
            <div class="border rounded p-4 bg-green-50">
              <h4 class="font-bold text-green-800 mb-2">IP-Adapter = "情绪板/风格卡"</h4>
              <ul class="text-sm space-y-1">
                <li>• 风格/外观/主体特征"软控"</li>
                <li>• 参考图 → 语义向量token（经CLIP/SigLIP编码）</li>
                <li>• 走跨/联合注意力，不对齐像素</li>
                <li>• 语义/风格软约束（"整体更像它"）</li>
              </ul>
            </div>
          </div>
        </section>

        <!-- 使用场景对比 -->
        <section>
          <h3 class="text-xl font-semibold mb-3 text-green-600">🎯 使用场景对比</h3>
          <div class="overflow-x-auto">
            <table class="min-w-full border border-gray-300">
              <thead class="bg-gray-100">
                <tr>
                  <th class="border px-4 py-2 text-left">目标</th>
                  <th class="border px-4 py-2 text-left">推荐方案</th>
                  <th class="border px-4 py-2 text-left">写法/操作要点</th>
                </tr>
              </thead>
              <tbody class="text-sm">
                <tr>
                  <td class="border px-4 py-2">严格构图/摆位/姿态<br>（电商产品三视图、人物指定动作）</td>
                  <td class="border px-4 py-2 text-blue-600 font-semibold">ControlNet</td>
                  <td class="border px-4 py-2">用Canny/HED保轮廓；OpenPose定动作；Depth/Normal保体积。强度0.5–0.8，避免死板</td>
                </tr>
                <tr>
                  <td class="border px-4 py-2">风格迁移/材质与调色<br>（梵高风、品牌质感统一）</td>
                  <td class="border px-4 py-2 text-green-600 font-semibold">IP-Adapter</td>
                  <td class="border px-4 py-2">分"内容参考"和"风格参考"，分别调权重；scale ~0.5–0.9</td>
                </tr>
                <tr>
                  <td class="border px-4 py-2">角色/脸一致性</td>
                  <td class="border px-4 py-2 text-green-600 font-semibold">IP-Adapter（FaceID/Plus）</td>
                  <td class="border px-4 py-2">搭配固定seed；必要时再叠ControlNet Pose保动作</td>
                </tr>
                <tr>
                  <td class="border px-4 py-2">既要姿态/构图，又要风格一致</td>
                  <td class="border px-4 py-2 text-purple-600 font-semibold">两者叠加</td>
                  <td class="border px-4 py-2">ControlNet锁结构 + IP-Adapter注入风格/身份。先把结构跑稳，再加风格权重</td>
                </tr>
              </tbody>
            </table>
          </div>
        </section>

        <!-- 模型支持情况 -->
        <section>
          <h3 class="text-xl font-semibold mb-3 text-purple-600">🛠️ 各模型支持情况</h3>
          <div class="grid md:grid-cols-2 gap-4 text-sm">
            <div>
              <h4 class="font-bold mb-2">✅ FLUX 1.1 / 1.dev（开源）</h4>
              <ul class="space-y-1">
                <li>• ControlNet：有对应实现（Canny/Depth/Pose等）</li>
                <li>• IP-Adapter：有专用适配器与SigLIP编码器</li>
                <li>• 可与LoRA叠加：LoRA管"长期风格/角色"，IP-Adapter管"这次像谁"</li>
              </ul>
            </div>
            <div>
              <h4 class="font-bold mb-2">🟡 Qwen-Image（开源）</h4>
              <ul class="space-y-1">
                <li>• 无原生ControlNet/IP-Adapter接口</li>
                <li>• 用"参考图 + 编辑/遮罩"软控</li>
                <li>• 走SD/FLUX开源链路做结构/风格后回Qwen精修文字</li>
              </ul>
            </div>
            <div>
              <h4 class="font-bold mb-2">🟡 Seedream 3.0（即梦）</h4>
              <ul class="space-y-1">
                <li>• 草图/抠图/局部重绘等工具，近似ControlNet软控</li>
                <li>• 风格迁移依赖"看图改图/多图融合"</li>
                <li>• 非标准ControlNet/IP-Adapter实现</li>
              </ul>
            </div>
            <div>
              <h4 class="font-bold mb-2">⛔ Imagen 4 & GPT-5</h4>
              <ul class="space-y-1">
                <li>• Imagen 4：不支持受控定制/编辑/参考图注入</li>
                <li>• GPT-5：无ControlNet，支持参考图生成与遮罩编辑</li>
                <li>• 用替代流程：参考图→文本化风格→纯文生成</li>
              </ul>
            </div>
          </div>
        </section>

        <!-- 翻车模式 -->
        <section>
          <h3 class="text-xl font-semibold mb-3 text-red-600">⚠️ 常见翻车模式</h3>
          <div class="grid md:grid-cols-2 gap-4">
            <div class="border rounded p-4 bg-red-50">
              <h4 class="font-bold text-red-800 mb-2">ControlNet 翻车</h4>
              <ul class="text-sm space-y-1">
                <li>• 强度太高 → 僵硬/难出细节</li>
                <li>• 条件图脏 → 伪影</li>
                <li>• 解决：调低强度(0.5-0.8)，清理条件图</li>
              </ul>
            </div>
            <div class="border rounded p-4 bg-orange-50">
              <h4 class="font-bold text-orange-800 mb-2">IP-Adapter 翻车</h4>
              <ul class="text-sm space-y-1">
                <li>• 权重太高 → 过拟合"像到一模一样"</li>
                <li>• 权重太低 → 风格没进来</li>
                <li>• 解决：调整scale权重(0.5-0.9)，平衡相似度</li>
              </ul>
            </div>
          </div>
        </section>

        <!-- 一句话总结 -->
        <section>
          <div class="bg-gradient-to-r from-blue-50 to-green-50 rounded-lg p-4 border-l-4 border-blue-500">
            <h3 class="text-xl font-semibold mb-2 text-gray-800">💡 一句话总结</h3>
            <p class="text-lg">
              ControlNet 是把"参考图"转成<strong>蓝图</strong>来钉住结构；IP-Adapter 是把"参考图"转成<strong>风格/特征向量</strong>来引导外观。<br>
              真要"硬控布局/姿态"→ 先选 ControlNet；想"像他那种味道/这个人这张脸"→ 先选 IP-Adapter；两者还能叠加用。
            </p>
          </div>
        </section>
      </div>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  modelValue: {
    type: Boolean,
    default: false
  }
})

const emit = defineEmits(['update:modelValue'])

const closeModal = () => {
  emit('update:modelValue', false)
}
</script>

<style scoped>
.fixed {
  position: fixed;
}
.inset-0 {
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
}
.z-50 {
  z-index: 50;
}
</style>
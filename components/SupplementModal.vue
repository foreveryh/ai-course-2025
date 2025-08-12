<template>
  <ModalDetails
    :title="title"
    :buttonText="buttonText"
    :closeText="closeText"
    :confirmText="confirmText"
    :maxWidth="maxWidth"
    :maxHeight="maxHeight"
    :teleportTo="teleportTo"
    :showClose="showClose"
    :closeOnEsc="closeOnEsc"
    :closeOnOverlay="closeOnOverlay"
  >
    <template #trigger="{ open }">
      <slot name="trigger" :open="open">
        <button class="px-4 py-2 rounded bg-teal-600 text-white" @click="open()">
          {{ buttonText }}
        </button>
      </slot>
    </template>
    

    <div class="space-y-6 leading-7">
      <component v-if="MdComponent" :is="MdComponent" />
      <div v-else class="text-sm opacity-70">未找到补充资料文件：{{ normalizedPath }}</div>
    </div>
  </ModalDetails>
</template>

<script setup lang="ts">
import { computed, defineAsyncComponent, ref, watchEffect } from 'vue'
import ModalDetails from './ModalDetails.vue'

interface Props {
  /** 相对 supplements/ 的路径，例如：`tokenization-examples.md` 或 `llm/attention.md` */
  path: string
  title?: string
  buttonText?: string
  closeText?: string
  confirmText?: string
  maxWidth?: string
  maxHeight?: string
  teleportTo?: string
  showClose?: boolean
  closeOnEsc?: boolean
  closeOnOverlay?: boolean
  /** v-model:open */
  open?: boolean
}

const props = withDefaults(defineProps<Props>(), {
  title: '补充资料',
  buttonText: '查看补充资料',
  closeText: '关闭',
  confirmText: '我学会了，收起',
  maxWidth: '920px',
  maxHeight: '85vh',
  teleportTo: 'body',
  showClose: true,
  closeOnEsc: true,
  closeOnOverlay: true,
})

defineEmits<{
  (e: 'update:open', val: boolean): void
}>()

// 通过 Vite 的 import.meta.glob 预扫描 supplements 下的所有 md
const modules = import.meta.glob('../supplements/**/*.md')

const normalizedPath = computed(() => {
  let p = props.path.trim()
  if (p.startsWith('supplements/')) p = p.replace(/^supplements\//, '')
  if (p.startsWith('./')) p = p.slice(2)
  return p
})

const key = computed(() => `../supplements/${normalizedPath.value}`)
const MdComponent = ref<ReturnType<typeof defineAsyncComponent> | null>(null)

watchEffect(() => {
  const importer = modules[key.value]
  if (!importer) {
    MdComponent.value = null
    return
  }
  MdComponent.value = defineAsyncComponent(async () => {
    const mod: any = await importer()
    // .md 编译为 Vue SFC，默认导出即为组件
    return mod.default || mod
  })
})

const { title, buttonText, closeText, confirmText, maxWidth, maxHeight, teleportTo, showClose, closeOnEsc, closeOnOverlay, open } = props
</script>

<style scoped></style>



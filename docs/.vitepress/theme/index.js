import DefaultTheme from 'vitepress/theme'
import './custom.css'

export default {
  extends: DefaultTheme,
  enhanceApp({ router }) {
    // 可以在这里添加自定义逻辑
    console.log('AI News Hub theme loaded')
  }
}

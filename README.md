# Reinforce Learning（强化学习）

前两次强化学习作业的中文 HTML 学习资料，共 10 题。

## 阅读

在线阅读：https://bellaallaa.github.io/Reinforce-Learning/

直接用浏览器打开 `index.html`，无需安装依赖或联网。包含题目、选项、答案、解析、拓展、答案速查、ε-greedy 概率演示及折扣回报演示。

“自测模式”隐藏答案汇总并折叠解析；“打印 / PDF”自动展开解析。

## 内容维护

- `build.py`：题目内容及 HTML 生成器，运行 `python build.py` 更新页面。
- `index.html`：可直接阅读的静态页面。
- `styles.css`：响应式与打印样式。
- `app.js`：自测切换与交互实验。

原始题目、答案与解析由用户提供。修复公式截断并新增知识拓展。作业 1 第 5 题的 ε 根据所附解析恢复为 0.5；页面显式说明了这一推定。数学表达采用原生 HTML 上下标，无外部脚本或字体依赖。

参考：Sutton & Barto, *Reinforcement Learning: An Introduction*, 2nd edition，第 1–4 章。页面末尾附参考链接。

仓库名使用 `Reinforce-Learning`，中文显示名称为“强化学习”。

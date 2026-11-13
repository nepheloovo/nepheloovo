<div align="center">

# 你好，我是小渡 👋

**AI 产品经理 · ENFP**

把复杂的技术，变成简单的体验。从真实问题出发，让 AI 的可能成为日常。

[![个人网站](https://img.shields.io/badge/个人网站-nepheloovo.github.io-163300?style=for-the-badge&logo=githubpages&logoColor=9FE870)](https://nepheloovo.github.io/)
[![公众号](https://img.shields.io/badge/公众号-小渡ovo-07C160?style=for-the-badge&logo=wechat&logoColor=white)](#articles)
[![小红书](https://img.shields.io/badge/小红书-小渡-FF2442?style=for-the-badge&logo=xiaohongshu&logoColor=white)](https://www.xiaohongshu.com/user/profile/5c0106fb0000000008019e70)

</div>

---

## 🙋 关于我

- 🧭 **AI 产品经理**：关心技术能做什么，更关心它能为人做什么
- 🔍 **先把问题问对**：谁遇到了什么困难？今天怎么解决？这件事真的需要 AI 吗？
- 🛠️ **从想法到实践**：自己动手把 PRD 做成能跑的产品 —— AI 游戏工作室、AIGC 内容平台、AI 应用中台、多 Agent 诊断、Agent Skill
- ✍️ **持续输出**：在公众号写 AI 热点解读与 AI 产品拆解
- 🌱 保持好奇，慢慢生长

## 🏷️ 标签

`AI 产品经理` `ENFP` `RAG` `AI Agent` `Multi-Agent` `LLM 评测` `可观测性` `Prompt 工程` `AIGC` `AI 产品拆解` `用户体验` `从想法到实践` `内容创作`

## 🧰 技能

**AI 产品**

- **RAG 知识库**：文档解析 / OCR → 切块 → 向量召回 → Rerank 精排 → 流式生成 + 引用溯源
- **Agent 设计**：ReAct 留痕、Multi-Agent 专家—辩论—评审链路、Agent Skill 编写与部署
- **质量闭环**：评测集设计、线上 Case 回流、Trace 可观测、Token 成本核算
- **产品方法**：需求定义、PRD 与降级策略设计、竞品与 AI 产品拆解、用户体验打磨

**动手实现**

![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square&logo=langchain&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)
![React](https://img.shields.io/badge/React-61DAFB?style=flat-square&logo=react&logoColor=black)
![OpenAI API](https://img.shields.io/badge/OpenAI_兼容接口-412991?style=flat-square&logo=openai&logoColor=white)
![DeepSeek](https://img.shields.io/badge/DeepSeek-4D6BFE?style=flat-square)
![通义千问](https://img.shields.io/badge/通义_qwen--vl-FF6A00?style=flat-square)

## 🚀 项目

### 🤖 AI 应用

| 项目 | 简介 | 技术 |
| --- | --- | --- |
| [**Kapy.ai**](https://github.com/nepheloovo/Kapy.ai)<br>一句话做出能玩的游戏 | 本地桌面游戏工作室：策划拆任务、程序写代码、质检逐条核查，再打开构建版本真的试玩打分，合格才交付；产出 Web 或 Godot 4 工程，像素卡皮巴拉 Kapy 全程陪伴 · [介绍页](https://nepheloovo.github.io/Kapy.ai/) | Electron · React · TypeScript · Codex · Godot 4 |
| [**万象工场**](https://github.com/nepheloovo/wanxiang-studio)<br>AIGC 内容生产平台 | 一句话需求拆成剧本 → 角色与场景 → 分镜 → 画面 → 视频 → 成片，每一步可查看、修改、单独重生成；一个场景包就是一个行业产品，内置短片 / 电商广告 / 漫剧 / 旅游宣传片 / 商品海报 · [介绍页](https://nepheloovo.github.io/wanxiang-studio/) | Python · Node.js · Multi-Agent |
| [**Agent 工坊**](https://github.com/nepheloovo/agent-workshop)<br>Agent 产品推导引擎 | 一句话点子 → 可确认的 PRD 与架构方案 → 交给你的 AI 编程工具写骨架 → 对照 PRD 验收 → 按新需求迭代；命令行与本地网页两种用法 | Python |
| [**知序 KnowOrder**](https://github.com/nepheloovo/knoworder)<br>AI 应用中台 | 把企业知识变成可上线、可评测、可追溯的 AI 应用：按文件自动切块的知识库，简易应用 / Agent / Chat Flow 三种编排，AI 设计评测集并作为发布门禁，每次运行留完整 Trace、可一键回流成评测 Case（基于 [chusimin/zhishu-rag-platform](https://github.com/chusimin/zhishu-rag-platform) 经授权二次开发） | Python · FastAPI · LangChain · React · pgvector · Celery |
| [**douyin-video-diagnose**](https://github.com/nepheloovo/douyin-video-diagnose)<br>抖音视频诊断 | 抽取视频前 3 秒画面 + 文案，内容 / 视觉 / 增长三位专家 Agent 诊断 → 辩论 → 评审出报告；按 PRD 设计三级降级模式，失败时不编造结论 · [在线 API](https://douyin-video-diagnose.onrender.com) | Python · FastAPI · SSE · ffmpeg · Multi-Agent |

### 🧩 Skills 与工具包

| 项目 | 简介 |
| --- | --- |
| [**idea-to-launch-kit**](https://github.com/nepheloovo/idea-to-launch-kit) | AI 产品从想法到上线开发工具包：一张规则卡 + 三份技术手册，让编码 AI 当技术合伙人，按阶段写代码、做界面、部署上线，每个阶段有闸门和证据包，非技术产品经理也能核对 |
| [**ai-product-teardown-skill**](https://github.com/nepheloovo/ai-product-teardown-skill) | AI 产品拆解 Skill：取证与分层拆解一款 AI 产品（尤其 Agent / Multi-Agent），输出飞书 / Markdown / HTML 报告，单列「待核实」清单 |
| [**ai-hotspot-wechat-skill**](https://github.com/nepheloovo/ai-hotspot-wechat-skill) | AI 热点公众号写作 Skill：任务书 → 主张核对 → 1200–2500 字初稿，以「小渡」口吻写出极客活人感 |

### 🎨 网页作品

| 项目 | 简介 | 在线体验 |
| --- | --- | --- |
| [**ai-pm-interview-bank**](https://github.com/nepheloovo/ai-pm-interview-bank) | AI 产品经理面试题库：175 道高频题，标注被问频次、考察点与答题框架，可按维度和公司查 | [🔗 访问](https://nepheloovo.github.io/ai-pm-interview-bank/) |
| [**pinterest-landing**](https://github.com/nepheloovo/pinterest-landing) | Pinterest 灵感落地页：暗色电影感设计、可交互灵感图墙与本地收藏画板 | [🔗 访问](https://nepheloovo.github.io/pinterest-landing/) |
| [**attachment-style**](https://github.com/nepheloovo/attachment-style) | 依恋类型小测：十二道轻问的自我对照静态站（娱乐参考） | — |
| [**nepheloovo.github.io**](https://github.com/nepheloovo/nepheloovo.github.io) | 我的个人网站，记录关于 AI、产品与创造的探索 | [🔗 访问](https://nepheloovo.github.io/) |

<a id="articles"></a>

## ✍️ 文章

公众号 **「小渡ovo」**：AI 热点解读、AI 产品思考，用懂行朋友聊天的口吻写给刚开始关注 AI 的人。微信搜索「小渡ovo」即可关注。

<!-- articles:start -->
| 文章 | 一句话 |
| --- | --- |
| [Deepseek SuperAgent超在哪了？](https://mp.weixin.qq.com/s/jWw2dwjDNryqrFVS7_Zohg) | 它没超在模型上，超在把「人肉调度员」这份活从人身上接走了 |
| [GitHub 小白指南：认识这 8 个词，就能看懂一个项目](https://mp.weixin.qq.com/s/siRmfMioUSMiCNVn96RZmA) | 不会写代码，也该看懂 GitHub：一个项目页面怎么看、八个必要功能是干什么的 |
| [Spec：写给一个不会提问的同事](https://mp.weixin.qq.com/s/mkJX2PjDeKOJjKcClSZCsA) | Spec 火起来，是因为需求文档多了一个只会照做的读者 |
| [FDE：企业 AI 的装修工](https://mp.weixin.qq.com/s/ina4Snx05fImKLAQpukz3A) | FDE 火了，但这可能不是 AI 行业的好消息 |
| [传统 PRD 到 AI PRD 到基因突变](https://mp.weixin.qq.com/s/JTnNsdvWjVnkz5e3UsQYoQ) | 从传统 PRD 到 AI PRD，产品文档正在发生什么变化 |
| [DeepSeek 把推理框架开出来了，能抄算子，抄不走机房](https://mp.weixin.qq.com/s/ydta9O89QAXyggxeBNjlhA) | DeepSeek 宣布开源 DeepInfer，开源之后真正的壁垒在哪 |
<!-- articles:end -->

---

<div align="center">

关于 AI、产品，或一个有趣的想法，期待有机会一起聊聊 ☕

</div>

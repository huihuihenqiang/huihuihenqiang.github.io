# 张辉 Hui Zhang · 个人学术主页

个人学术主页，介绍我的研究兴趣、论文、项目和学习笔记。

- **主页**：https://huihuihenqiang.github.io/
- **学术页面**：https://huihuihenqiang.github.io/Pages/
- **GitHub**：https://github.com/huihuihenqiang

## 研究简介

我拥有北京理工大学应用统计专业硕士学位，研究兴趣集中于大语言模型智能体、持续学习与统计评估。目前的研究关注智能体如何从交互经验中改进，以及如何可靠地衡量这种改进。

## 论文

| 工作 | 状态 | 资源 |
| --- | --- | --- |
| **MedEvoEval**：Evaluating Continual Evolution of Doctor Agents through Simulated Clinical Episodes | Hui Zhang · NeurIPS 2026 E&D Track，Poster，已接收 | [论文主页](https://huihuihenqiang.github.io/medevoeval/) · [arXiv](https://arxiv.org/abs/2606.28900) · [代码](https://github.com/huihuihenqiang/MedEvoEval) · [数据](https://www.kaggle.com/datasets/anonymousmedevoeval/medevoeval-anonymous-review-dataset) |



## 项目与学习笔记

- **MedEvoEval 评估框架**：通过模拟门诊交互研究医生智能体的持续学习与演化评估。[项目仓库](https://github.com/huihuihenqiang/MedEvoEval)。
- **机器学习与科研工具笔记**：[数学与统计基础](article/THPML%20book/math%20theroy%20of%20ML.html)、[Git](article/Git/Git的使用技巧(一).html)、[Markdown](article/Markdown/Markdown用法（一）.html)、[信息检索](article/IR/信息检索.html)。

## 常用链接

- [GitHub](https://github.com/huihuihenqiang)
- Google Scholar：TODO（个人主页链接）
- OpenReview：TODO（个人主页链接）
- ORCID：TODO（研究者标识与链接）
- 技术写作：[CSDN](https://blog.csdn.net/m0_57491181) · [知乎](https://www.zhihu.com/people/chen-feng-26-77-97/posts)

## 页面维护

| 路径 | 用途 |
| --- | --- |
| `Pages/index.html` | 学术主页正文与内嵌样式，单文件，无构建步骤 |
| `index.html` | 网站根入口，跳转到 `Pages/index.html` |
| `medevoeval/` | MedEvoEval 论文主页、资源链接及框架图 |
| `article/` | 已有学习笔记与静态资源 |

从仓库根目录运行 `python -m http.server 8000`，然后访问 `http://localhost:8000/`。主页不依赖外部 CSS、字体、图标库或 JavaScript；根入口使用短脚本跳转，并提供无 JavaScript 的跳转和手动链接。

更新信息时同时修改 `Pages/index.html` 与本文件。待补充的链接目前是普通文本；确认真实地址后再替换成链接。新增论文前先核对题名、作者顺序、接收状态及论文地址。

<!--
内容依据（维护备注，不在渲染后的 README 中显示）：
- 姓名、北京理工大学应用统计硕士、研究方向、MedEvoEval，以及 NeurIPS 2026 E&D Poster 接收状态来自已确认的对话上下文。
- GitHub、CSDN、知乎及具体学习笔记路径来自现有仓库。
- MedEvoEval 题名、作者与 arXiv 地址已核对；Scholar/ORCID/OpenReview 个人链接仍待提供。
- 当前没有足够信息将具体 ICLR 或 AAAI 稿件列为接收论文；后续新增时，不能把进入审稿阶段写成录用。
-->

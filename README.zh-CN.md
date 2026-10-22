# Daily Brief · 每日安排

[English](README.md) | 简体中文

用已有任务整理今天能做的事。工具会单独列出受阻事项，并根据可用分钟数安排已就绪任务，方便看出哪些需要留到之后。

[下载 v0.2.1](https://github.com/KarmenLoop/skill-daily-brief/releases/tag/v0.2.1) · [完整教程](docs/tutorial.zh-CN.md) · [输入参考](docs/input.zh-CN.md) · [反馈问题](https://github.com/KarmenLoop/skill-daily-brief/issues)

## 能做什么

样例有 90 分钟可用：逾期的 40 分钟提案进入安排，发票事项保留为受阻，60 分钟的审阅留待之后。

这是按规则运行的计划工具，不会读取日历、让 AI 估时或执行安排。

![每日安排 0.2.1 版本样例的真实 JSON 输出](docs/images/example-output-v0.2.1.svg)

*图片来自 v0.2.1 的真实本地输出，采用英文键名；[完整结果](examples/expected.json) · [图片来源记录](docs/images/provenance.json)。*

## 开始使用

在发行页下载 `karmen-daily-brief-v0.2.1.zip` 与对应 `.sha256` 文件，核对哈希后解压。在解压目录中使用 Python 3.9 或更新版本：

```sh
python3 scripts/run.py --version
python3 scripts/run.py --input examples/input.json
```

预期版本：`karmen-daily-brief 0.2.1`。样例有 90 分钟可用：逾期的 40 分钟提案进入安排，发票事项保留为受阻，60 分钟的审阅留待之后。

如果宿主读取 `~/.agents/skills`，可安装完整技能：

```sh
python3 install.py --host agents
```

目标目录已存在时安装器会拒绝覆盖。宿主发现和调用方式可能不同，见[安装与实践教程](docs/tutorial.zh-CN.md)。不使用 AI 宿主也能直接运行本地工具。

## 用于自己的任务

先填写工作日期、available_minutes 和合理工时。priority 为 1 时优先级最高；任务状态使用 ready、blocked 或 done。

用同一批任务比较只有 30 分钟和有 120 分钟的安排，检查 deferred 中的变化，避免把全部任务都当成已经排好。

准备新输入前可查看[字段约定](docs/input.zh-CN.md)。工具只依赖 Python 标准库，本身不需要模型账号、API 密钥或网络。使用 AI 宿主时，宿主有自己的数据与权限设置。

## 常见问题

**它会发提醒吗？** 不会。你可以保存结果，审阅后再把选定事项交给自己的提醒工具。

**结果保存在哪里？** 默认向终端输出 JSON；使用 `--output` 时只创建新文件，已有输出文件会保留。工具只读取提交的记录和输入约定中明确列出的本地路径。

## 文档与支持

- [下载、安装、配置、练习、升级与卸载](docs/tutorial.zh-CN.md)
- [输入输出约定](docs/input.zh-CN.md)与[兼容性说明](docs/COMPATIBILITY.md)（英文参考）
- [更新记录](CHANGELOG.md)、[参与贡献](CONTRIBUTING.md)、[支持](SUPPORT.md)和[安全反馈](SECURITY.md)

## 许可证

[MIT](LICENSE)。再分发时保留许可证和[声明](NOTICE.md)。由 [KarmenLoop](https://karmenloop.com) 维护。

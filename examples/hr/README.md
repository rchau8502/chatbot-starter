# 示例：同事/员工流程助手（HR Bot）

把这份示例换成自己的场景：

```bash
cp examples/hr/prompts/system.md   prompts/system.md
cp examples/hr/prompts/handbook.md prompts/handbook.md
```

再改 `.env` 里的品牌文案：

```ini
BOT_NAME=小坏
BOT_EMOJI=🐣
BOT_TAGLINE=坏坏科技 · 流程助手
PAGE_TITLE=小坏 · 坏坏科技流程助手
WELCOME_TITLE=找我办事，不走冤枉路
WELCOME_SUB=报销、请假、入职的流程我熟，说不清的细则我会告诉你去问谁。
EXAMPLE_QUESTIONS=上周出差的机票怎么报销？|下周三想请两天事假，流程怎么走？|新员工入职当天要带哪些材料？
BOT_ACCENT=#d94f1e
BOT_ACCENT_SOFT=#fbe9e1
```

这是最初演示用的版本：小坏负责报销、请假、入职三类流程，手册里的数字都是假数据。

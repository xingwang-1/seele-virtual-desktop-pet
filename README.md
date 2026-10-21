# 希儿-虚拟桌面宠物

希儿·芙乐艾的 Q 版 ChatGPT Work 桌面陪伴宠物资源包。项目以一张透明背景精灵图为核心，附带动作索引、预览、格式说明和本地校验脚本。

## 预览

- [最新完整精灵图预览](preview/spritesheet-overview-v3.jpg)
- [运行完成举牌动画](preview/completion-animation-v2.gif)
- [清除黑线后的运行动画](preview/running-clean-v3.gif)
- [思考动作 GIF 预览](preview/thinking-animation.gif)：为便于检查而按每帧 650 ms 播放，不代表 ChatGPT Work 的实际播放速度。
- [思考动作帧带](preview/thinking-frames.png)

## 动作

2026-10-21 更新：运行成功时播放举牌“完成啦！”；运行动画六帧上下的独立黑线残片已清除。其他动作保持不变，当前资源已更新到用户正在使用的 Work Pets。

本机客户端将运行动作映射到第 8 行 `running`，将成功通知映射到第 9 行 `review`。旧版素材名称与客户端状态名称不完全一致，详见 [动作布局](docs/animation-layout.md)。

## 精灵图规格

- 当前文件：`assets/seele-pet-clean-running-v3.png`
- 原始版本和举牌中间版本保留在 `assets/`；文件名 v2/v3 是素材修订号，不是精灵图格式版本。
- PNG，RGBA 透明背景
- 1536 × 1872 像素，v1，8 列 × 9 行
- 单格 192 × 208 像素
- 每行使用帧数：6、8、8、4、5、8、6、6、6
- 依据 ChatGPT Work Pets v1 精灵图格式制作

## 本地校验

需要 Python 3 和 Pillow：

```powershell
python -m pip install -r requirements.txt
python tools/validate_spritesheet.py
```

通过时会打印 `VALID` 和图像规格。Pets 服务端校验也已通过。

## 使用范围

这是 ChatGPT Work Pets 的精灵图与配套说明，不是独立运行的 Windows 桌面程序。宠物已更新在用户的 ChatGPT Work Pets 中。若要在其他环境使用，需要该环境支持同一精灵图动画格式。

## 版权与来源

角色希儿·芙乐艾及其原始设定的权利归其各自权利人所有。本仓库是个人用途的同人宠物素材整理；不主张角色或原始参考图的所有权。生成与整理过程说明见 [素材说明](docs/asset-notes.md)。

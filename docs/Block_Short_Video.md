# iOS Shadowrocket 短视频屏蔽模块

模块：[`../modules/Block_Short_Video.sgmodule`](../modules/Block_Short_Video.sgmodule)。资料核对日期：2026-10-10。

这是已识别域名的屏蔽清单，**不是所有大陆短视频的完整封锁，也未在 iOS 实机验证**。优先避免对微信消息、聊天媒体、语音视频通话和微信支付的误伤。没有 HTTPS 解密、证书、脚本、IP 或 ASN 拒绝规则；没有强制微信走 DIRECT，未匹配的请求继续使用原配置策略。

## 覆盖范围

| 需求 | 当前处理 | 局限或连带影响 |
| --- | --- | --- |
| 微信视频号 | 拒绝 `finder.video.qq.com` 媒体、`channels.weixin.qq.com` 网页入口；腾讯视频组还拒绝 `video.qq.com` 子域名 | 原生接口、直播、共享连接与新 CDN 不保证覆盖；聊天中分享的视频号内容也会受影响 |
| QQ 视频 / 腾讯视频 / 微视 | 已识别网页、视频服务和专用域名 | 腾讯视频长视频也会被阻断；不把 QQ 聊天视频通话当作 QQ 视频封禁 |
| 微信豆充值 | **未添加充值专用规则** | 未取得足以区分普通支付的接口证据；不能保证阻断充值。不能封整个 `payapp.weixin.qq.com` 或 `pay.weixin.qq.com` 来替代 |
| 微信小店 | 视频号网页入口受阻；**微信内部小店未完整覆盖** | 商城/小程序可能使用共享接口；不能封整个 `servicewechat.com` 或 `weixin.qq.com` 来替代 |
| 百度短视频 | 好看视频、全民小视频已识别入口 | 百度 App 信息流及共享媒体地址不保证覆盖；未封 `baidu.com`、`bdstatic.com`、`bcebos.com` 整站 |
| 抖音、头条系 | 抖音/极速版、火山、西瓜、头条/极速版、皮皮虾的已识别站点/API/媒体域名 | 头条图文、西瓜长视频也会受影响；未封字节云、飞书、豆包及通用 `snssdk.com`、`pstatp.com` |
| 其他常见平台 | 快手/极速版、小红书、哔哩哔哩、AcFun、美拍、秒拍、最右 | 小红书图文、B站和 AcFun 长视频/直播也会受影响；其他应用内短视频、新应用、替代域名不保证覆盖 |

域名规则无法按视频时长或同一服务中的功能区分内容。对混合平台，以上规则按平台阻断。若要保留某个平台，删除或注释模块中相应整组规则。

## 安装和顺序

1. 将模块文件传到 iPhone，或在 Shadowrocket 的「配置 → 模块 → 新建模块」中粘贴文件全部内容并保存。若从 GitHub 下载，请选择包含本模块的分支；PR 合并前，`main` 分支可能还没有该文件。
2. 在当前配置中启用模块，全局路由选择「配置」，保持 Shadowrocket 连接。不需要开启 HTTPS 解密或安装证书。
3. 检查模块顺序及连接记录：本模块的拒绝规则应先于其他模块的放行规则匹配。模块规则优先于基础配置；基础配置 `FINAL,DIRECT` 不会代替已命中的拒绝规则。
4. 停止目标应用并重新打开，必要时重新连接 Shadowrocket，以排除已有连接/缓存的干扰。

不要手动新增全腾讯 IP、`qq.com`、`gtimg.com`、`qpic.cn`、`qlogo.cn`、`weixin.qq.com`、`wechat.com`、`tenpay.com` 或 `wechatpay.com` 的拒绝规则。配置中的既有 `skip-proxy`、排除路由或其他模块也可能使部分流量不经过本模块。

## 域名依据与筛选

公开列表是归属/分流参考，并非经过验证的屏蔽清单。只选取与目标产品相关的条目，不整份导入。

| 来源 | 使用方式 |
| --- | --- |
| [blackmatrix7 DouYin](https://github.com/blackmatrix7/ios_rule_script/blob/master/rule/Shadowrocket/DouYin/DouYin.list) | 抖音媒体域名；排除通用字节域名 |
| [blackmatrix7 TencentVideo](https://github.com/blackmatrix7/ios_rule_script/blob/master/rule/Shadowrocket/TencentVideo/TencentVideo.list) | 筛选视频域名；排除 `dldir1.qq.com`、`rdelivery.qq.com`、广告共享域名、全部 IP |
| [blackmatrix7 WeChat](https://github.com/blackmatrix7/ios_rule_script/blob/master/rule/Shadowrocket/WeChat/WeChat.list) | 识别须避免整体封禁的微信/支付/共享媒体服务，例如 `soup.v.qq.com` |
| [blackmatrix7 KuaiShou](https://github.com/blackmatrix7/ios_rule_script/blob/master/rule/Shadowrocket/KuaiShou/KuaiShou.list) | 快手产品/API/CDN；不导入数百个缺乏明确产品用途的域名 |
| [blackmatrix7 XiaoHongShu](https://github.com/blackmatrix7/ios_rule_script/blob/master/rule/Shadowrocket/XiaoHongShu/XiaoHongShu.list) | 排除跨产品风控服务 `fengkongcloud.com` |
| [blackmatrix7 BiliBili](https://github.com/blackmatrix7/ios_rule_script/blob/master/rule/Shadowrocket/BiliBili/BiliBili.list) | 核心视频域名；不导入游戏、漫画、支付、IP 及共享 CDN 根域名 |
| [v2fly douyin](https://github.com/v2fly/domain-list-community/blob/master/data/douyin) | 抖音/火山媒体和入口；排除汽水音乐、生活服务等无关产品 |
| [v2fly bytedance](https://github.com/v2fly/domain-list-community/blob/master/data/bytedance) | 头条、西瓜、皮皮虾分组中的域名；不导入整个字节清单 |
| [v2fly kuaishou](https://github.com/v2fly/domain-list-community/blob/master/data/kuaishou)、[baidu](https://github.com/v2fly/domain-list-community/blob/master/data/baidu)、[tencent](https://github.com/v2fly/domain-list-community/blob/master/data/tencent)、[meitu](https://github.com/v2fly/domain-list-community/blob/master/data/meitu) | 补充快手媒体、好看、微视、美拍域名；不导入母公司的通用云服务 |
| [wx_channel 媒体示例](https://github.com/nobiyou/wx_channel/blob/b1a752b0170235e4ed49162dd06a45d3c117e66e/docs/BATCH_DOWNLOAD_GUIDE.md)、[分享入口代码](https://github.com/nobiyou/wx_channel/blob/b1a752b0170235e4ed49162dd06a45d3c117e66e/internal/api/search.go) | `finder.video.qq.com`、`channels.weixin.qq.com`；共享 `weixin.qq.com/sph/` 没有转换成整域拒绝 |
| [全民视频反馈](https://github.com/5ime/video_spider/issues/27)、[微视网页示例](https://github.com/dravenww/blob/issues/12) | `quanmin.baidu.com`、`weishi.qq.com` 的历史参考，当前可用性未确认 |
| [fmz200 秒拍](https://github.com/fmz200/wool_scripts/blob/5d5f63fcf98bc69d5f8f1b1bae6f86a01ee4bb97/QuantumultX/rewrite/split/partM/MiaoPai.snippet)、[应用重写清单](https://github.com/fmz200/wool_scripts/blob/5d5f63fcf98bc69d5f8f1b1bae6f86a01ee4bb97/QuantumultX/rewrite/rewrite.snippet) | 秒拍 `b-api.ins.miaopai.com`、最右 `api.izuiyou.com` 的归属依据；本模块扩大至各自产品域名，不复制重写规则 |
| [Shadowrocket 使用说明](https://github.com/lowertop/Shadowrocket/blob/main/README.md) | 模块格式、匹配顺序、配置模式及域名/SNI 匹配方式；属于社区文档 |

其中部分公开列表标注更新时间为 2025 年，核对日期不表示每个域名仍然活跃。没有把凭名称猜测的 `wecoin.qq.com`、`shop.weixin.qq.com`、`findermp.video.qq.com` 当作已确认接口。

## IP 收集结果和不采用 IP 拒绝的原因

本次尝试系统 DNS 查询 A/AAAA 对应地址，包括视频号、微视、百度视频和其他候选入口，均返回 `Temporary failure in name resolution`。因此**没有取得当前有效的域名到 IP 映射**，也不能声称这些服务没有 IP 地址。

已取得的公开腾讯视频列表列出下列 IPv4 单地址网段，作为历史候选资料记录：

| 上游列出的 IP 网段 | 本模块处理 |
| --- | --- |
| `58.49.111.117/32` | 不使用，未确认现时归属、共享情况或对应域名 |
| `58.49.111.79/32` | 同上 |
| `58.49.111.95/32` | 同上 |

来源：[TencentVideo.list](https://github.com/blackmatrix7/ios_rule_script/blob/master/rule/Shadowrocket/TencentVideo/TencentVideo.list)，该文件标注更新于 2025-06-06。列表还含 IPv4 映射 IPv6 和 `198.18.*` 基准测试网段条目，未作为真实服务地址采用。B站列表的 IP 也未用于拒绝。

视频、微信聊天媒体、支付及其他应用可能共用云/CDN 地址，DNS 地址又会随网络、地区和时间变化。仅查询到 IP 不能证明其为目标专用，更不能把 CNAME 指向的整个 CDN 或 ASN 封禁。域名拒绝可覆盖能被识别出域名/SNI 的 IPv4 和 IPv6 连接，但直接 IP 连接、共享连接、加密域名等情况可能漏过。这里以保留微信通讯和支付为优先约束。

## 验证

本地静态回归：在仓库根目录运行 `python3 tests/check_short_video_rules.py`，检查格式、重复规则、目标命中、后缀边界，以及微信/支付和共享服务样本未被拒绝。它不模拟 Shadowrocket 的完整规则引擎，也不替代实机验证。

iPhone 上仍需完成以下检查，分别在 Wi-Fi 和蜂窝网络测试，查看连接记录中命中的规则和策略：

| 测试 | 期望 |
| --- | --- |
| 微信文字、图片、聊天视频收发；语音/视频通话 | 继续正常使用 |
| 微信支付扫码入口、收款码、账单、零钱；按需进行本人认可的小额支付 | 继续正常使用；不为了测试强制发生充值或交易 |
| 视频号新打开的视频、直播、分享卡片 | 已识别媒体连接显示 REJECT；直播等未覆盖路径需另行核实 |
| QQ/腾讯视频、微视、好看、全民视频、抖音、头条、西瓜、快手等新内容 | 已识别连接显示 REJECT；已缓存内容可能仍可播放 |
| 微信豆充值、小店商品页 | **当前没有完整阻断保证**；记录仍放行的入口与连接 |
| 百度搜索/网盘、微信普通小程序、其他必要应用 | 验证没有连带异常 |

补充微信豆/小店规则时，需要当前 iOS 微信版本上的入口、请求主机和实际命中记录。如果短视频/充值和消息/支付复用同一主机或微信原生连接，单纯域名/IP规则无法同时满足这两个目标；不要通过不断扩大拒绝范围解决。URL 路径规则只有在可观察到路径时才有效，HTTPS 场景可能需要解密，而且微信原生连接不保证可解密。此模块不对共享微信/支付连接启用解密。

若通讯或支付异常，先禁用本模块，重新连接并复测；确认与本模块有关后，仅移除对应误伤规则。保留复现入口、域名及命中策略便于修正，勿保存支付凭据、完整敏感 URL 参数或聊天内容。

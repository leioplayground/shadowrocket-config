"""Static safety checks; does not claim iOS/Shadowrocket runtime validation."""

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
MODULE = ROOT / "modules" / "Block_Short_Video.sgmodule"
rules = []
sections = []
for number, raw in enumerate(MODULE.read_text(encoding="utf-8").splitlines(), 1):
    line = raw.strip()
    if not line or line.startswith("#"):
        continue
    if line.startswith("["):
        sections.append(line)
        continue
    parts = line.split(",")
    assert len(parts) == 3, (number, "invalid rule fields")
    kind, domain, policy = parts
    assert kind in {"DOMAIN", "DOMAIN-SUFFIX"}, (number, "unexpected broad rule")
    assert policy == "REJECT", (number, "unexpected routing override")
    assert re.fullmatch(r"[a-z0-9]+(?:[a-z0-9-]*[a-z0-9])?(?:\.[a-z0-9]+(?:[a-z0-9-]*[a-z0-9])?)+", domain), (number, "invalid hostname")
    rules.append((kind, domain))
assert sections == ["[Rule]"], "must not alter general settings or MITM"
assert len(rules) == len(set(rules)), "duplicate rule"


def rejects(host):
    host = host.lower().rstrip(".")
    return any(
        host == domain or (kind == "DOMAIN-SUFFIX" and host.endswith("." + domain))
        for kind, domain in rules
    )


blocked = [
    "finder.video.qq.com", "channels.weixin.qq.com", "v.qq.com",
    "m.v.qq.com", "api.video.qq.com", "weishi.qq.com", "www.weishi.com",
    "haokan.baidu.com", "www.haokan.com", "quanmin.baidu.com",
    "www.douyin.com", "aweme.snssdk.amemv.com", "v1.douyinvod.com",
    "api.huoshan.com", "www.toutiao.com", "api.toutiaoapi.com",
    "www.ixigua.com", "api.pipix.com", "v1.ppxvod.com",
    "www.kuaishou.com", "apissl.gifshow.com", "api.ksapisrv.com",
    "v1.kwaicdn.com", "v1.yximgs.com", "www.xiaohongshu.com",
    "api.bilibili.com", "v1.bilivideo.com", "www.acfun.cn",
    "www.meipai.com", "b-api.ins.miaopai.com", "api.izuiyou.com",
]
preserved = [
    "weixin.qq.com", "short.weixin.qq.com", "long.weixin.qq.com",
    "szshort.weixin.qq.com", "szlong.weixin.qq.com", "extshort.weixin.qq.com",
    "mp.weixin.qq.com", "support.weixin.qq.com", "res.wx.qq.com",
    "vweixinf.tc.qq.com", "vweixinthumb.tc.qq.com", "wxapp.tc.qq.com",
    "soup.v.qq.com", "wxs.qq.com", "wx.qlogo.cn", "mmbiz.qpic.cn",
    "servicewechat.com", "api.weixin.qq.com", "api.mch.weixin.qq.com",
    "pay.weixin.qq.com", "payapp.weixin.qq.com", "wx.tenpay.com",
    "api.tenpay.com", "www.wechatpay.com", "hk.wechatpay.com",
    "www.baidu.com", "pan.baidu.com", "passport.baidu.com",
    "cdn.bcebos.com", "www.bdstatic.com", "www.gtimg.com",
    "www.feishu.cn", "www.doubao.com", "api.snssdk.com",
    "www.pstatp.com", "fengkongcloud.com", "cdn.myqcloud.com",
    "www.douyin.com.example.org", "notdouyin.com", "notkuaishou.com",
]
for host in blocked:
    assert rejects(host), (host, "target missed")
for host in preserved:
    assert not rejects(host), (host, "unintended rejection")
assert rejects("WWW.DOUYIN.COM."), "DNS case/trailing-dot normalization"
print(f"PASS: {len(rules)} rules; {len(blocked)} blocked and {len(preserved)} preserved samples; format and scope guards")
print("Not verified: iOS behavior, shared connections, full WeCoin/shop coverage, live DNS/IP attribution")

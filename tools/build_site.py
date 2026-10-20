# -*- coding: utf-8 -*-
"""Aju Works 公式サイトのビルド＆検証（正本は data/apps.json）。

  python tools/build_site.py            生成（index.html / apps.html / privacy.html / privacy/index.html /
                                        apps/*.html（旧URLの案内）/ sitemap.xml / robots.txt / 404.html）＋検証
  python tools/build_site.py --check    ファイルを書かずに検証だけ行う
  python tools/build_site.py --check-play  上記に加え、published の Google Play URL が実際に開くか確認する（要ネット）

アプリを増やす・公開状態を変えるときは data/apps.json だけを直し、このスクリプトを実行する。
homepage / apps.html / privacy/ 一覧 / sitemap を手で別々に編集しない。
アプリ別プライバシーポリシー本文は privacy/<slug>/index.html（アプリごとに手書き）。
"""
import html as htmllib
import json
import os
import re
import sys
import urllib.request

SITE = "https://ajuworks.github.io"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAIL = "ajuworks.official@gmail.com"
REG = os.path.join(ROOT, "data", "apps.json")

STATUSES = ("published", "in_review", "development", "unlisted")
CATEGORY_ORDER = ["ツール", "仕事効率化", "ライフスタイル", "健康", "その他"]
HOME_MAX = 8
LEGACY_PAGES = {  # 旧 apps/<name>.html → 現 slug（None は一覧トップへ）
    "charge-mihari": "charge-mihari", "contacts-sukkiri": "contacts-sukkiri", "copipe-shelf": None,
    "fanvolt": "fanvolt", "focus-gate": "focus-gate", "gym-record": "gym-record", "hibi-count": "hibi-count",
    "kokoshare": "kokoshare", "linkpocket": "link-pocket", "midnight-hotel": None, "night-fade": "night-fade",
    "oto-set": "oto-set", "photo-sukkiri": "photo-sukkiri", "pittari-compress": "pittari-compress",
    "readrecall": "yomioku", "step-bp-diary": "step-bp-diary", "subscription-manager": "cancel-nav",
    "watchit": None, "worklog": "worklog", "yomioku": "yomioku",
}
# 旧 privacy.html の #アンカー → 現在のアプリ別ページ（外部やPlayから既に参照されているURLを壊さない）
HASH_ALIASES = {
    "fanvolt": "fanvolt", "cancel-nav": "cancel-nav", "subscription-manager": "cancel-nav",
    "focus-gate": "focus-gate", "step-bp-diary": "step-bp-diary", "readrecall": "yomioku", "yomioku": "yomioku",
    "yomioku-data-deletion": "yomioku/#data-deletion", "kokoshare": "kokoshare", "night-fade": "night-fade",
    "watchit": "watchit", "linkpocket": "link-pocket", "midnight-hotel": "midnight-hotel", "gym-record": "gym-record",
}

errors, warnings = [], []


def load():
    with open(REG, encoding="utf-8") as f:
        apps = json.load(f)["apps"]
    for a in apps:
        a["playUrl"] = "https://play.google.com/store/apps/details?id=" + a["packageName"]
        a["privacyUrl"] = "%s/privacy/%s/" % (SITE, a["slug"])
    return apps


def esc(s):
    return htmllib.escape(s, quote=True)


def write(path, text, dry):
    if dry:
        return
    d = os.path.dirname(path)
    if d and not os.path.isdir(d):
        os.makedirs(d)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print("wrote", os.path.relpath(path, ROOT), len(text), "bytes")


# ---------------------------------------------------------------------------
# 共通パーツ
# ---------------------------------------------------------------------------
def head(prefix, title, desc, canonical, extra=""):
    return """<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>%(title)s</title>
  <meta name="description" content="%(desc)s">
  <link rel="canonical" href="%(canonical)s">

  <!-- OGP -->
  <meta property="og:type"        content="website">
  <meta property="og:title"       content="%(title)s">
  <meta property="og:description" content="%(desc)s">
  <meta property="og:url"         content="%(canonical)s">
  <meta property="og:site_name"   content="Aju Works">
  <meta property="og:locale"      content="ja_JP">
  <meta name="twitter:card"       content="summary">
  <meta name="twitter:title"      content="%(title)s">
  <meta name="twitter:description" content="%(desc)s">
%(extra)s
  <!-- ファビコン（インラインSVG: 紺背景に白の「A」） -->
  <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'><rect width='32' height='32' rx='6' fill='%%231e3a5f'/><text x='50%%25' y='50%%25' dominant-baseline='central' text-anchor='middle' font-family='sans-serif' font-size='20' font-weight='900' fill='white'>A</text></svg>">

  <link rel="stylesheet" href="%(prefix)sassets/css/style.css">
</head>
<body>
""" % dict(title=esc(title), desc=esc(desc), canonical=canonical, prefix=prefix, extra=extra)


NAV = (("index.html", "ホーム"), ("apps.html", "アプリ"), ("support.html", "サポート"), ("about.html", "事業者情報"))


def header(prefix):
    nav = "".join('\n        <a href="%s%s">%s</a>' % (prefix, h, t) for h, t in NAV)
    mnav = "".join('\n    <a href="%s%s">%s</a>' % (prefix, h, t) for h, t in NAV)
    return """
  <!-- ===== ヘッダー ===== -->
  <header class="site-header">
    <div class="container">
      <a href="%(p)sindex.html" class="site-logo">
        <span class="logo-mark">A</span>
        Aju Works
      </a>

      <!-- PCナビ -->
      <nav class="site-nav" aria-label="メインナビゲーション">%(nav)s
      </nav>

      <!-- ハンバーガーボタン（スマホ用） -->
      <button class="hamburger" aria-label="メニューを開く" aria-expanded="false">
        <span></span>
        <span></span>
        <span></span>
      </button>
    </div>
  </header>

  <!-- モバイルメニュー -->
  <nav class="mobile-menu" aria-label="モバイルナビゲーション">%(mnav)s
  </nav>
""" % dict(p=prefix, nav=nav, mnav=mnav)


def footer(prefix):
    return """
  <!-- ===== フッター ===== -->
  <footer class="site-footer">
    <div class="container">
      <div class="footer-inner">
        <!-- ブランド -->
        <div class="footer-brand">
          <a href="%(p)sindex.html" class="footer-logo">Aju Works</a>
          <p>日々の実務と暮らしを少し便利にする<br>Androidアプリ</p>
        </div>

        <!-- ナビ: サービス -->
        <div class="footer-nav-group">
          <h4>サービス</h4>
          <ul>
            <li><a href="%(p)sapps.html">アプリ一覧</a></li>
            <li><a href="%(p)ssupport.html">サポート</a></li>
            <li><a href="%(p)sabout.html">事業者情報</a></li>
          </ul>
        </div>

        <!-- ナビ: ポリシー -->
        <div class="footer-nav-group">
          <h4>ポリシー</h4>
          <ul>
            <li><a href="%(p)sprivacy.html">プライバシーポリシー（共通）</a></li>
            <li><a href="%(p)sprivacy/">アプリ別プライバシーポリシー</a></li>
            <li><a href="%(p)sterms.html">利用規約</a></li>
          </ul>
        </div>

        <!-- ナビ: お問い合わせ -->
        <div class="footer-nav-group">
          <h4>お問い合わせ</h4>
          <ul>
            <li><a href="%(p)ssupport.html">サポート・お問い合わせ</a></li>
          </ul>
        </div>
      </div>

      <div class="footer-bottom">
        <p>&copy; 2026 Aju Works. All rights reserved.</p>
      </div>
    </div>
  </footer>

  <script src="%(p)sassets/js/main.js"></script>
</body>
</html>
""" % dict(p=prefix)


def page(prefix, title, desc, canonical, body, extra_head=""):
    return head(prefix, title, desc, canonical, extra_head) + header(prefix) + body + footer(prefix)


ARROW = ('<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
         'stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
         '<path d="M5 12h14M12 5l7 7-7 7"/></svg>')


def icon_img(app, prefix, cls):
    if not app["icon"]:
        return '<span class="%s" aria-hidden="true"></span>' % cls
    return ('<span class="%s"><img src="%s%s" width="128" height="128" alt="%s のアプリアイコン" '
            'loading="lazy" decoding="async"></span>' % (cls, prefix, app["icon"], esc(app["name"])))


def app_card(app, prefix, filterable=False):
    attrs = ' id="%s"' % app["slug"]
    if filterable:
        text = esc(" ".join([app["name"], app["launcherName"], app["category"], app["description"]]).lower())
        attrs += ' data-category="%s" data-search="%s"' % (esc(app["category"]), text)
    return """      <article class="app-tile"%s>
        <div class="app-tile-head">
          %s
          <div class="app-tile-heading">
            <h3 class="app-tile-name">%s</h3>
            <span class="app-tile-category">%s</span>
          </div>
        </div>
        <p class="app-tile-desc">%s</p>
        <div class="app-tile-actions">
          <a href="%s" target="_blank" rel="noopener noreferrer" class="btn btn-primary btn-sm">Google Play</a>
          <a href="%sprivacy/%s/" class="btn btn-outline btn-sm">プライバシーポリシー</a>
        </div>
      </article>""" % (attrs, icon_img(app, prefix, "app-tile-icon"), esc(app["name"]), esc(app["category"]),
                       esc(app["description"]), app["playUrl"], prefix, app["slug"])


def published(apps):
    return sorted([a for a in apps if a["status"] == "published"], key=lambda a: a["sortOrder"])


# ---------------------------------------------------------------------------
# index.html
# ---------------------------------------------------------------------------
def home_apps(apps):
    pub = published(apps)
    featured = [a for a in pub if a.get("featured")][:HOME_MAX]
    if len(featured) < HOME_MAX:  # 足りない分は新しい順に補う
        for a in pub:
            if a not in featured and len(featured) < HOME_MAX:
                featured.append(a)
    return sorted(featured, key=lambda a: a["sortOrder"])


def build_index(apps, dry):
    pub = published(apps)
    cards = "\n".join(app_card(a, "") for a in home_apps(apps))
    body = """
  <main>

    <!-- ===== ヒーローセクション ===== -->
    <section class="hero">
      <div class="container">
        <div class="hero-content">
          <span class="hero-badge">Android Apps</span>
          <h1 class="hero-title">
            日々の実務と暮らしを、<br>
            少し便利にする<br>
            Androidアプリ
          </h1>
          <p class="hero-subtitle">
            Androidアプリ・デジタルコンテンツを企画・開発しています。Google Playで公開中のアプリは%(n)d本です。
          </p>
          <div class="hero-actions">
            <a href="apps.html" class="btn btn-white btn-lg">アプリを見る</a>
            <a href="support.html" class="btn btn-outline-white btn-lg">お問い合わせ</a>
          </div>
        </div>
      </div>
    </section>

    <!-- ===== アプリ（新しい・代表的なもの） ===== -->
    <section class="section section-alt">
      <div class="container">
        <div class="section-header">
          <span class="section-label">Apps</span>
          <h2>Aju Worksのアプリ</h2>
          <p>Google Playで公開中のアプリから、新しいものと代表的なものを紹介します。</p>
        </div>

        <div class="app-grid app-grid-4">
%(cards)s
        </div>

        <div class="section-actions">
          <a href="apps.html" class="btn btn-primary btn-lg">すべてのアプリを見る（全%(n)d本）</a>
        </div>
      </div>
    </section>

    <!-- ===== 事業内容セクション ===== -->
    <section class="section">
      <div class="container">
        <div class="section-header">
          <span class="section-label">Our Services</span>
          <h2>事業領域</h2>
          <p>利用者の課題解決にフォーカスした、実用的なアプリとデジタルコンテンツを企画・開発しています。</p>
        </div>

        <div class="card-grid" style="max-width: 760px; margin: 0 auto;">
          <div class="card">
            <span class="card-icon" aria-hidden="true">
              <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="5" y="2" width="14" height="20" rx="2"/><line x1="9" y1="18" x2="15" y2="18"/></svg>
            </span>
            <h3>アプリ開発</h3>
            <p>
              日常の記録・整理・習慣づくりを助けるAndroidアプリを企画・開発しています。
              使い続けたくなるシンプルな設計を心がけています。
            </p>
          </div>

          <div class="card">
            <span class="card-icon" aria-hidden="true">
              <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>
            </span>
            <h3>デジタルコンテンツ</h3>
            <p>
              電子書籍などのデジタルコンテンツの企画・制作も行っています。
              必要な人に、必要な情報を届けることを優先します。
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- ===== CTAセクション ===== -->
    <section class="cta-section">
      <div class="container">
        <h2>まずはお気軽にご相談ください</h2>
        <p>アプリのご要望・お問い合わせはメールにて受け付けています。</p>
        <a href="support.html" class="btn btn-white btn-lg">お問い合わせページへ</a>
      </div>
    </section>

  </main>
""" % dict(cards=cards, n=len(pub))
    write(os.path.join(ROOT, "index.html"), page(
        "", "Aju Works — 日々の実務と暮らしを少し便利にするAndroidアプリ",
        "日々の実務と暮らしを少し便利にするAndroidアプリを開発するAju Works。Google Playで公開中のアプリ%d本を紹介します。" % len(pub),
        SITE + "/", body), dry)


# ---------------------------------------------------------------------------
# apps.html
# ---------------------------------------------------------------------------
def build_apps(apps, dry):
    pub = published(apps)
    cats = [c for c in CATEGORY_ORDER if any(a["category"] == c for a in pub)]
    cats += sorted({a["category"] for a in pub} - set(cats))
    chips = ['<button type="button" class="chip is-active" data-filter="">すべて（%d）</button>' % len(pub)]
    for c in cats:
        chips.append('<button type="button" class="chip" data-filter="%s">%s（%d）</button>'
                     % (esc(c), esc(c), sum(1 for a in pub if a["category"] == c)))
    body = """
  <main>

    <!-- ===== ページヘッダー ===== -->
    <section class="page-header">
      <div class="container">
        <h1>アプリ一覧</h1>
        <p>Google Playで公開中のAju Worksの全Androidアプリ（%(n)d本）です。</p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="app-controls">
          <input type="search" id="app-search" class="app-search" placeholder="アプリ名・キーワードで探す" aria-label="アプリを検索" autocomplete="off">
          <div class="app-chips" role="group" aria-label="カテゴリで絞り込む">
            %(chips)s
          </div>
        </div>
        <p class="app-count" id="app-count" aria-live="polite">%(n)d本を表示中</p>

        <div class="app-grid app-grid-4" id="app-list">
%(cards)s
        </div>
        <p class="app-empty" id="app-empty" hidden>該当するアプリがありません。</p>

        <p class="app-note">
          公開準備中のアプリは、Google Playで公開されたあとにこの一覧へ追加します。
          各アプリの情報の取り扱いは <a href="privacy/">アプリ別プライバシーポリシー</a> と
          <a href="privacy.html">共通プライバシーポリシー</a> をご覧ください。
        </p>
      </div>
    </section>

    <!-- ===== CTAセクション ===== -->
    <section class="cta-section">
      <div class="container">
        <h2>アプリについてのお問い合わせ</h2>
        <p>不具合のご報告・ご要望はメールにて受け付けています。</p>
        <a href="support.html" class="btn btn-white btn-lg">サポートページへ</a>
      </div>
    </section>

  </main>
""" % dict(n=len(pub), chips="\n            ".join(chips),
           cards="\n".join(app_card(a, "", filterable=True) for a in pub))
    write(os.path.join(ROOT, "apps.html"), page(
        "", "アプリ一覧 — Aju Works",
        "Google Playで公開中のAju WorksのAndroidアプリ全%d本の一覧。カテゴリ・キーワードで探せます。" % len(pub),
        SITE + "/apps.html", body), dry)


# ---------------------------------------------------------------------------
# privacy/index.html（アプリ別プライバシーポリシー一覧）
# ---------------------------------------------------------------------------
def privacy_row(a, note=""):
    ext = ""
    if a.get("privacyExternal"):
        ext = '<br><span class="doc-note">本体の専用ポリシー: <a href="%s" target="_blank" rel="noopener noreferrer">%s</a></span>' % (
            a["privacyExternal"], a["privacyExternal"])
    return """            <tr>
              <td><a href="%s/"><strong>%s</strong></a>%s</td>
              <td><code>%s</code></td>
              <td>%s</td>
              <td><a href="%s/">ポリシーを見る</a></td>
            </tr>""" % (a["slug"], esc(a["name"]), ext, a["packageName"], note, a["slug"])


def privacy_listed(apps):
    pub = published(apps)
    prep = sorted([a for a in apps if a["status"] == "in_review" or
                   (a["status"] == "development" and a.get("privacyListed"))], key=lambda a: a["sortOrder"])
    return pub, prep


def build_privacy_index(apps, dry):
    pub, prep = privacy_listed(apps)
    status_label = {"in_review": "公開準備中（審査中）", "development": "公開準備中"}

    def table(rows):
        return """          <div class="table-wrap"><table class="doc-table">
            <thead><tr><th>アプリ</th><th>パッケージ名</th><th>状態</th><th>ポリシー</th></tr></thead>
            <tbody>
%s
            </tbody>
          </table></div>""" % "\n".join(rows)

    body = """
  <main>

    <div class="page-header">
      <div class="container">
        <h1>アプリ別プライバシーポリシー</h1>
        <p>Aju Works の各アプリにおける情報の取り扱い</p>
      </div>
    </div>

    <section class="document-section">
      <div class="container">
        <div class="document-content">
          <div class="document-meta">
            <span><strong>この一覧はサイトのアプリ登録（data/apps.json）から自動生成しています。</strong></span>
            <span><strong>事業者:</strong> Aju Works（個人事業）</span>
          </div>

          <div class="doc-chapter">
            <h2>このページについて</h2>
            <p>
              アプリごとに取り扱う情報が異なるため、ご利用のアプリのポリシーをご確認ください。
              すべてのアプリに共通する事項は <a href="../privacy.html">共通プライバシーポリシー</a> に記載しています。
              アプリ別ポリシーと共通ポリシーは併せて適用され、内容が異なる場合はアプリ別ポリシーを優先します。
            </p>
          </div>

          <div class="doc-chapter">
            <h2>公開中のアプリ（%(npub)d本）</h2>
%(pub)s
          </div>
%(prep)s
          <div class="doc-chapter">
            <h2>お問い合わせ</h2>
            <p>プライバシーに関するお問い合わせは <a href="../support.html">サポートページ</a> または %(mail)s までご連絡ください。</p>
          </div>

        </div>
      </div>
    </section>

  </main>
""" % dict(
        npub=len(pub), mail=MAIL,
        pub=table([privacy_row(a, "公開中") for a in pub]),
        prep=("""
          <div class="doc-chapter">
            <h2>公開準備中のアプリ</h2>
            <p>Google Playでの公開に向けて準備中のアプリです。ポリシーは審査・公開に備えて先に掲載しています。</p>
%s
          </div>
""" % table([privacy_row(a, status_label[a["status"]]) for a in prep])) if prep else "")
    write(os.path.join(ROOT, "privacy", "index.html"), page(
        "../", "アプリ別プライバシーポリシー一覧 | Aju Works",
        "Aju Worksの各Androidアプリのプライバシーポリシー一覧。公開中%d本・公開準備中%d本。" % (len(pub), len(prep)),
        SITE + "/privacy/", body), dry)


# ---------------------------------------------------------------------------
# privacy.html（共通ポリシー）
# ---------------------------------------------------------------------------
def build_privacy_common(apps, dry):
    pub, prep = privacy_listed(apps)
    redirect_map = {k: (v if v.startswith(("http", "/")) else "privacy/" + (v if "#" in v or v.endswith("/") else v + "/"))
                    for k, v in HASH_ALIASES.items()}
    items = []
    for a in pub + prep + [x for x in apps if x["status"] == "development" and not x.get("privacyListed")]:
        items.append('              <li id="%s"><a href="privacy/%s/">%s</a>（%s）</li>' % (
            a["slug"], a["slug"], esc(a["name"]), a["packageName"]))
    anchors = "".join('<span id="%s"></span>' % k for k in HASH_ALIASES if k not in {a["slug"] for a in apps})
    script = ("<script>(function(){var m=%s;var h=decodeURIComponent((location.hash||'').slice(1));"
              "if(m[h]){location.replace(m[h]);}})();</script>" % json.dumps(redirect_map, ensure_ascii=False))
    body = """
  <main>

    <div class="page-header">
      <div class="container">
        <h1>プライバシーポリシー（共通）</h1>
        <p>Aju Works が提供するアプリ・サービスに共通する個人情報の取り扱い</p>
      </div>
    </div>

    <section class="document-section">
      <div class="container">
        <div class="document-content">
          <div class="document-meta">
            <span><strong>制定:</strong> 2026年5月 ／ <strong>最終更新:</strong> 2026年10月21日（共通ポリシーとアプリ別ポリシーを分離）</span>
            <span><strong>事業者:</strong> Aju Works（個人事業）</span>
          </div>
          %(script)s%(anchors)s

          <div class="doc-chapter">
            <h2><span class="chapter-num">1</span>はじめに</h2>
            <p>
              本プライバシーポリシー（以下「本ポリシー」）は、Aju Works（以下「当事業者」）が個人事業として提供する
              アプリケーション・デジタルコンテンツ（以下総称して「本サービス」）に共通して適用される、
              個人情報の取り扱い方針を定めるものです。
            </p>
            <p>
              各アプリが取り扱う情報の詳細（保存するデータ、端末外へ送信するデータ、使用する権限、広告・課金の有無など）は、
              アプリごとに <a href="privacy/">アプリ別プライバシーポリシー</a> に記載しています。
              アプリ別ポリシーと本ポリシーは併せて適用され、内容が異なる場合はアプリ別ポリシーを優先します。
            </p>
          </div>

          <div class="doc-chapter">
            <h2><span class="chapter-num">2</span>情報の取り扱いに関する基本方針</h2>
            <p>
              当事業者のアプリは、ユーザーが入力・保存した内容を、原則として端末内にのみ保存します。
              当事業者のサーバーへ送信して保存・収集することを前提とした設計は行いません。
              ただし、広告の表示や課金の処理など、アプリの機能上、外部のサービス提供者が情報を扱う場合があります。
              その場合の内容と宛先は、アプリ別ポリシーに記載します。
            </p>
            <p>当事業者が取得する可能性のある情報は、次のとおりです。</p>
            <ul>
              <li>お問い合わせの際に入力いただいた氏名・メールアドレスおよびお問い合わせ内容</li>
              <li>アプリ別ポリシーに記載した、アプリの機能の提供に必要な情報</li>
            </ul>
          </div>

          <div class="doc-chapter">
            <h2><span class="chapter-num">3</span>利用目的</h2>
            <p>取得した情報は、以下の目的にのみ利用します。</p>
            <ul>
              <li>本サービスの提供・運営・改善</li>
              <li>お問い合わせへの対応</li>
              <li>サービスに関する重要なお知らせの連絡</li>
            </ul>
          </div>

          <div class="doc-chapter">
            <h2><span class="chapter-num">4</span>第三者への提供</h2>
            <p>当事業者は、以下のいずれかに該当する場合を除き、取得した個人情報を第三者に提供しません。</p>
            <ul>
              <li>ご本人の同意がある場合</li>
              <li>法令に基づく場合（裁判所・警察等の公的機関からの適法な要請がある場合）</li>
              <li>人の生命・身体・財産の保護のために必要な場合で、本人の同意を得ることが困難な場合</li>
            </ul>
          </div>

          <div class="doc-chapter">
            <h2><span class="chapter-num">5</span>Google Play 等の外部プラットフォーム</h2>
            <p>
              本サービスは、Google Play 等のプラットフォームを通じて提供されます。
              これらのプラットフォームが収集・処理する情報（アプリのインストール・更新・購入・クラッシュ情報など）は、
              各プラットフォーム事業者のプライバシーポリシーに従います。
              当事業者はこれらのプラットフォームのデータ処理について責任を負いません。
            </p>
            <ul>
              <li>Google LLC（Google Play ほか）: <a href="https://policies.google.com/privacy" target="_blank" rel="noopener noreferrer">https://policies.google.com/privacy</a></li>
            </ul>
          </div>

          <div class="doc-chapter">
            <h2><span class="chapter-num">6</span>広告を利用するアプリについて（一般説明）</h2>
            <p>
              広告を表示するアプリでは、Google AdMob（Google Mobile Ads SDK）を利用して広告を配信します。
              広告の表示・最適化のため、端末の広告識別子（Advertising ID）や端末・利用状況に関する情報が
              Google LLC に送信される場合があります。これらの情報は Google LLC のプライバシーポリシーに従って扱われます。
            </p>
            <ul>
              <li>EU・英国など、法令上の同意取得が必要な地域のユーザーには、Google の User Messaging Platform（UMP）を通じて同意取得画面を表示します。</li>
              <li>広告識別子のリセット・無効化や広告のパーソナライズの制限は、Android の「設定」→「プライバシー」→「広告」から行えます。</li>
              <li>ユーザーが保存した本文・写真・連絡先などの内容を、広告配信のために広告SDKへ渡すことはありません（各アプリのポリシーに個別に記載します）。</li>
              <li>広告を表示するかどうかはアプリごとに異なります。広告を表示しないアプリには広告SDKを組み込んでいません。各アプリの広告の有無は、アプリ別ポリシーと Google Play のデータ セーフティ欄をご確認ください。</li>
            </ul>
            <p>Google の広告に関する情報: <a href="https://policies.google.com/technologies/ads" target="_blank" rel="noopener noreferrer">https://policies.google.com/technologies/ads</a></p>
          </div>

          <div class="doc-chapter">
            <h2><span class="chapter-num">7</span>アプリ内課金（Billing）について</h2>
            <p>
              一部のアプリでは、機能を追加する買い切り（Pro など）のアプリ内課金を、Google Play Billing を通じて提供しています。
              支払い・決済情報は Google が処理し、当事業者はクレジットカード番号などの決済情報を取得・保存しません。
              購入状態（購入済みかどうか）は、Google Play を通じてアプリが確認します。
              課金の有無と内容はアプリごとに異なります。詳細は各アプリのストア掲載情報とアプリ別ポリシーをご確認ください。
            </p>
          </div>

          <div class="doc-chapter" id="app-policies">
            <h2><span class="chapter-num">8</span>アプリ別のプライバシーポリシー</h2>
            <p>
              Health Connect・クリップボード・写真・通知・位置情報など、アプリごとに異なる情報の取り扱いは、
              次の各ページに記載しています（一覧: <a href="privacy/">アプリ別プライバシーポリシー</a>）。
            </p>
            <ul>
%(items)s
            </ul>
          </div>

          <div class="doc-chapter">
            <h2><span class="chapter-num">9</span>情報の安全管理</h2>
            <p>
              当事業者は、取得した個人情報の漏えい・滅失・毀損の防止のために、適切な安全管理措置を講じます。
              お問い合わせメール等の情報は、目的の達成後、適切に廃棄します。
            </p>
          </div>

          <div class="doc-chapter">
            <h2><span class="chapter-num">10</span>子どものプライバシー</h2>
            <p>
              本サービスは、主に13歳以上の方を対象としています。13歳未満のお子様から、意図して個人情報を取得することはありません。
              お子様の情報が提供されたことが判明した場合は、速やかに削除します。
              保護者の方でお気づきの点がありましたら、下記までご連絡ください。
            </p>
          </div>

          <div class="doc-chapter">
            <h2><span class="chapter-num">11</span>ポリシーの改定</h2>
            <p>
              本ポリシーは、法令の変更・サービスの変更等に伴い、予告なく変更することがあります。
              変更がある場合は、当サイト上で告知します。改定後のポリシーは、掲載された時点から適用されます。
            </p>
          </div>

          <div class="doc-chapter">
            <h2><span class="chapter-num">12</span>お問い合わせ</h2>
            <p>
              本ポリシーに関するお問い合わせは、以下のメールアドレスまでご連絡ください。<br>
              メールアドレス: <a href="mailto:%(mail)s">%(mail)s</a>
            </p>
            <p>サポート窓口は <a href="support.html">サポートページ</a> でもご案内しています。</p>
          </div>

        </div>
      </div>
    </section>

  </main>
""" % dict(script=script, anchors=anchors, items="\n".join(items), mail=MAIL)
    write(os.path.join(ROOT, "privacy.html"), page(
        "", "プライバシーポリシー（共通） | Aju Works",
        "Aju Worksが提供するアプリ・サービスに共通するプライバシーポリシー。広告・課金・子どものプライバシーなどの共通事項を定めています。",
        SITE + "/privacy.html", body), dry)


# ---------------------------------------------------------------------------
# apps/<旧名>.html（旧URLの案内）/ 404 / sitemap / robots
# ---------------------------------------------------------------------------
def build_legacy_pages(apps, dry):
    by = {a["slug"]: a for a in apps}
    for old, slug in LEGACY_PAGES.items():
        a = by.get(slug) if slug else None
        target = "../apps.html#" + slug if a and a["status"] == "published" else "../apps.html"
        name = a["name"] if a else "アプリ"
        body = """
  <main>
    <section class="section">
      <div class="container" style="text-align:center;">
        <h1 style="margin-bottom: var(--space-4);">アプリ一覧へ移動しました</h1>
        <p>アプリの紹介はアプリ一覧に集約しました（%s）。</p>
        <p style="margin-top: var(--space-5);"><a class="btn btn-primary" href="%s">アプリ一覧を開く</a></p>
      </div>
    </section>
  </main>
""" % (esc(name), target)
        extra = '  <meta name="robots" content="noindex">\n  <meta http-equiv="refresh" content="0; url=%s">\n' % target
        write(os.path.join(ROOT, "apps", old + ".html"), page(
            "../", "アプリ一覧 — Aju Works", "アプリの紹介はアプリ一覧に集約しました。",
            SITE + "/apps.html", body, extra), dry)


def build_404(dry):
    body = """
  <main>
    <div class="page-header">
      <div class="container">
        <h1>ページが見つかりません</h1>
        <p>お探しのページは、移動または削除された可能性があります。</p>
      </div>
    </div>

    <section class="section">
      <div class="container">
        <div class="section-header">
          <span class="section-label">404</span>
          <h2>次のいずれかからお探しください</h2>
        </div>
        <div class="section-actions">
          <a href="/" class="btn btn-primary">ホームへ</a>
          <a href="/apps.html" class="btn btn-outline">アプリ一覧</a>
          <a href="/support.html" class="btn btn-outline">サポート</a>
          <a href="/privacy.html" class="btn btn-outline">プライバシーポリシー</a>
        </div>
      </div>
    </section>
  </main>
"""
    write(os.path.join(ROOT, "404.html"), page(
        "", "ページが見つかりません — Aju Works", "お探しのページは移動または削除された可能性があります。",
        SITE + "/404.html", body, '  <meta name="robots" content="noindex">\n'), dry)


def build_sitemap(apps, dry):
    pub, prep = privacy_listed(apps)
    urls = ["/", "/apps.html", "/privacy.html", "/privacy/", "/support.html", "/about.html", "/terms.html"]
    urls += ["/privacy/%s/" % a["slug"] for a in pub + prep]
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
           + "".join("  <url><loc>%s%s</loc></url>\n" % (SITE, u) for u in urls) + "</urlset>\n")
    write(os.path.join(ROOT, "sitemap.xml"), xml, dry)
    write(os.path.join(ROOT, "robots.txt"), "User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n" % SITE, dry)


# ---------------------------------------------------------------------------
# 検証
# ---------------------------------------------------------------------------
def err(msg):
    errors.append(msg)


def read(path):
    with open(os.path.join(ROOT, path), encoding="utf-8") as f:
        return f.read()


def validate(apps, check_play):
    slugs, pkgs = set(), set()
    for a in apps:
        for k in ("slug", "name", "packageName", "status", "category", "description"):
            if not a.get(k):
                err("%s: %s が空" % (a.get("slug"), k))
        if a["slug"] in slugs:
            err("slug 重複: " + a["slug"])
        if a["packageName"] in pkgs:
            err("packageName 重複: " + a["packageName"])
        slugs.add(a["slug"]); pkgs.add(a["packageName"])
        if a["status"] not in STATUSES:
            err("%s: status 不正 %s" % (a["slug"], a["status"]))
        if not 20 <= len(a["description"]) <= 100:
            warnings.append("%s: description が %d 文字（目安 40〜90）" % (a["slug"], len(a["description"])))
        listed = a["status"] in ("published", "in_review") or a.get("privacyListed")
        ppath = os.path.join("privacy", a["slug"], "index.html")
        if listed or a["status"] == "published":
            if not os.path.isfile(os.path.join(ROOT, ppath)):
                err("%s: プライバシーページがない（%s）" % (a["slug"], ppath))
            else:
                t = read(ppath)
                if a["packageName"] not in t:
                    err("%s: プライバシーページに package 名がない" % a["slug"])
                if a.get("ads") and "AdMob" not in t and "Mobile Ads" not in t:
                    err("%s: ads=true なのにプライバシーページに広告SDK（AdMob / Mobile Ads）の記載がない" % a["slug"])
                if a.get("ads") is False and ("AdMob" in t or "Mobile Ads" in t):
                    err("%s: ads=false なのにプライバシーページが AdMob に言及している" % a["slug"])
        if a["status"] == "published":
            if not a["icon"] or not os.path.isfile(os.path.join(ROOT, a["icon"])):
                err("%s: published なのにアイコンがない" % a["slug"])
        if a["status"] != "published" and a["icon"] and not os.path.isfile(os.path.join(ROOT, a["icon"])):
            err("%s: icon パスが存在しない" % a["slug"])
    # 生成物との整合
    if os.path.isfile(os.path.join(ROOT, "apps.html")):
        t = read("apps.html")
        for a in apps:
            on = ('id="%s"' % a["slug"]) in t
            if a["status"] == "published" and not on:
                err("%s: published なのに apps.html にない" % a["slug"])
            if a["status"] != "published" and on:
                err("%s: 未公開なのに apps.html に載っている" % a["slug"])
        if t.count('class="app-tile"') != sum(1 for a in apps if a["status"] == "published"):
            err("apps.html のカード数が published 件数と一致しない")
    if os.path.isfile(os.path.join(ROOT, "index.html")):
        t = read("index.html")
        for a in apps:
            if a["status"] != "published" and ('privacy/%s/' % a["slug"]) in t:
                err("%s: 未公開なのに index.html に載っている" % a["slug"])
    # Play URL
    if check_play:
        for a in apps:
            if a["status"] != "published":
                continue
            try:
                r = urllib.request.urlopen(urllib.request.Request(a["playUrl"] + "&hl=ja", headers={"User-Agent": "Mozilla/5.0"}), timeout=30)
                if r.status != 200:
                    err("%s: Play URL が %s" % (a["slug"], r.status))
            except Exception as e:
                err("%s: Play URL を開けない（%s）" % (a["slug"], str(e)[:60]))
    # 古い状態表記の残存
    for p in ("index.html", "apps.html"):
        if os.path.isfile(os.path.join(ROOT, p)) and "Coming soon" in read(p):
            err("%s に公開準備中の一覧が残っている" % p)


def check_links():
    """サイト内の相対・ルート相対リンクと img/script/link 参照が実在するか確認する。"""
    bad = 0
    for dp, dn, fn in os.walk(ROOT):
        dn[:] = [d for d in dn if d not in (".git", "tools", "data", "__pycache__")]
        for f in fn:
            if not f.endswith(".html"):
                continue
            path = os.path.join(dp, f)
            with open(path, encoding="utf-8") as fh:
                t = fh.read()
            t = re.sub(r"<script>.*?</script>", "", t, flags=re.S)
            for m in re.finditer(r'(?:href|src)="([^"#?][^"]*)"', t):
                u = m.group(1)
                if re.match(r"(https?:|mailto:|tel:|data:|javascript:)", u):
                    continue
                u = u.split("#")[0].split("?")[0]
                tgt = os.path.join(ROOT, u.lstrip("/")) if u.startswith("/") else os.path.normpath(os.path.join(dp, u))
                if os.path.isdir(tgt):
                    tgt = os.path.join(tgt, "index.html")
                if not os.path.isfile(tgt):
                    bad += 1
                    err("リンク切れ: %s → %s" % (os.path.relpath(path, ROOT), m.group(1)))
    return bad


def main():
    dry = "--check" in sys.argv or "--check-play" in sys.argv
    apps = load()
    if not dry:
        build_index(apps, dry)
        build_apps(apps, dry)
        build_privacy_index(apps, dry)
        build_privacy_common(apps, dry)
        build_legacy_pages(apps, dry)
        build_404(dry)
        build_sitemap(apps, dry)
    validate(apps, "--check-play" in sys.argv)
    check_links()
    pub, prep = privacy_listed(apps)
    print("apps: %d / published: %d / in_review: %d / development: %d / home: %d / privacy listed: %d"
          % (len(apps), len(published(apps)), sum(a["status"] == "in_review" for a in apps),
             sum(a["status"] == "development" for a in apps), len(home_apps(apps)), len(pub) + len(prep)))
    for w in warnings:
        print("WARN:", w)
    for e in errors:
        print("ERROR:", e)
    if errors:
        sys.exit(1)
    print("OK")


if __name__ == "__main__":
    main()

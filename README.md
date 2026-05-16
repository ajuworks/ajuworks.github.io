# Aju Works — 公式サイト 運用ガイド

## サイト概要

Aju Works（アジュワークス）の公式Webサイトです。  
GitHub Organization「ajuworks」配下のGitHub Pagesで無料公開しています。  
外部ライブラリ・CDN一切不使用。HTML / CSS / 素のJavaScriptのみで構成されています。

---

## 公開URL

| ページ | URL |
|--------|-----|
| トップページ | https://ajuworks.github.io/ |
| アプリ一覧 | https://ajuworks.github.io/apps.html |
| サポート | https://ajuworks.github.io/support.html |
| 事業者情報 | https://ajuworks.github.io/about.html |
| プライバシーポリシー（共通） | https://ajuworks.github.io/privacy.html |
| 利用規約 | https://ajuworks.github.io/terms.html |

---

## ファイル構成

```
ajuworks.github.io/
├── index.html          # トップページ
├── apps.html           # アプリ一覧
├── privacy.html        # Aju Works共通プライバシーポリシー
├── terms.html          # 利用規約
├── support.html        # サポート・お問い合わせ
├── about.html          # 事業者情報
├── assets/
│   ├── css/
│   │   └── style.css   # 共通スタイルシート
│   └── js/
│       └── main.js     # ハンバーガーメニュー・FAQアコーディオン・ナビactive
└── README.md           # この運用ガイド
```

---

## Google Play Console に登録するURL

アプリを Google Play Console に登録する際、以下のURLを使用してください。

| 用途 | URL |
|------|-----|
| プライバシーポリシー（ジム記録＆ベンチコーチ専用） | `https://gym-record-bench-coach-policy.vercel.app/privacy` |
| プライバシーポリシー（Aju Works共通） | `https://ajuworks.github.io/privacy.html` |
| サポートURL | `https://ajuworks.github.io/support.html` |
| アプリ一覧 | `https://ajuworks.github.io/apps.html` |

> 独自ドメインを取得した場合は上記URLをそちらに変更してください。  
> アプリ専用プライバシーポリシー（Vercel）を終了する場合は、Google Play Console 上のURLも更新が必要です。

---

## 各ページの用途

| ファイル | 用途 | 注意点 |
|---------|------|--------|
| `privacy.html` | Aju Works 全体の共通プライバシーポリシー | Google Play に登録可能 |
| `support.html` | サポート・お問い合わせページ | Google Play のサポートURLとして登録可能 |
| `about.html` | 事業者情報（屋号・事業形態・連絡先等） | 住所はバーチャルオフィス承認後に差し替え |
| `apps.html` | 公開中のアプリ一覧 | アプリ専用プライバシーポリシーへのリンクあり |
| `terms.html` | 一般利用規約 | 全サービス共通 |

---

## 差し替えが必要な箇所

公開・更新時に以下のプレースホルダーを実際の情報に変更してください。

| 項目 | プレースホルダー / 現状 | 対象ファイル | 変更タイミング |
|------|----------------------|-------------|--------------|
| 所在地 | `〒XXX-XXXX 東京都〇〇区〇〇 X-X-X（バーチャルオフィス）` | about.html | バーチャルオフィス契約完了後 |
| メールアドレス | `ajuworks.official@gmail.com`（現在設定済み） | 全HTMLファイル | 事業用アドレスに変更する場合 |
| 電話番号 | 現在非掲載（掲載しない方針） | — | 掲載が必要になった場合のみ |
| Google Play URL | `href="#"`（準備中） | apps.html ボタン | Google Play審査通過後 |

### 注意事項
- **自宅住所・個人電話番号・個人メールアドレスは絶対に記載しないでください。**
- 住所はバーチャルオフィス承認後に差し替える前提です。
- 電話番号は現時点では掲載しない方針です。

---

## ローカルでの確認方法

### 方法1: VS Code Live Server（推奨）

1. VS Code に「Live Server」拡張をインストール
2. `index.html` を右クリック → 「Open with Live Server」
3. ブラウザで `http://127.0.0.1:5500/` が開きます

### 方法2: Python シンプルサーバー

```bash
cd /path/to/ajuworks.github.io
python -m http.server 8000
# → http://localhost:8000/ をブラウザで開く
```

---

## GitHub Pages への公開状態

| 項目 | 設定 |
|------|------|
| リポジトリ | https://github.com/ajuworks/ajuworks.github.io |
| ブランチ | main |
| 公開ディレクトリ | / (root) |
| 公開URL | https://ajuworks.github.io/ |

### 公開設定の確認手順

1. GitHub リポジトリ → Settings → Pages
2. Source: **Deploy from a branch**
3. Branch: `main` / フォルダ: `/ (root)` → Save

---

## プライバシーポリシー更新時の注意

- `privacy.html` の「制定・最終更新」日付を更新してください
- Google Play Console に登録しているURLが変わる場合は、Console上でも更新が必要です
- 大幅な変更を行う場合は、ユーザーへの告知を検討してください

---

## 費用について

| 項目 | 費用 |
|------|------|
| GitHub Pages | **無料**（Organization Public リポジトリの場合） |
| 独自ドメイン | 不使用（ajuworks.github.io サブドメインを利用） |
| 外部サービス | なし（CDN等の依存ゼロ） |

> **重要な注意事項:**  
> GitHub Pages の無料提供条件は GitHub の利用規約変更により変わる可能性があります。  
> 定期的に [GitHub Pages の公式ドキュメント](https://docs.github.com/ja/pages/getting-started-with-github-pages/about-github-pages) を確認してください。  
> 将来的に独自ドメイン・外部ホスティングへの移行を検討する場合も、全ファイルが静的HTMLのため移行は容易です。

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026年5月 | 初版作成（atushi0095-del/aju-works-site） |
| 2026年5月 | Organization（ajuworks/ajuworks.github.io）へ移行、公開URL変更 |

# Aju Works — 公式サイト 運用ガイド

## サイト概要

Aju Works（アジュワークス）の静的公式Webサイトです。  
外部ライブラリ・CDN一切不使用。HTML / CSS / 素のJavaScriptのみで構成されています。

---

## ファイル構成

```
aju-works-site/
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

## ローカルでの確認方法

### 方法1: ブラウザで直接開く（簡易）

`index.html` をダブルクリックするか、ブラウザのアドレスバーに以下を貼り付けます。

```
file:///C:/Users/atush/Desktop/kindle/クロード/aju-works-site/index.html
```

> 注意: `file://` プロトコルではナビのアクティブ状態検出（main.js）が正常に動作しない場合があります。

### 方法2: VS Code Live Server（推奨）

1. VS Code に「Live Server」拡張をインストール
2. `index.html` を右クリック → 「Open with Live Server」
3. ブラウザで `http://127.0.0.1:5500/` が開きます

### 方法3: Python シンプルサーバー

```bash
cd "C:\Users\atush\Desktop\kindle\クロード\aju-works-site"
python -m http.server 8000
# → http://localhost:8000/ をブラウザで開く
```

---

## GitHub Pages への公開手順

1. GitHubで新しいリポジトリを作成（例: `aju-works-site`）
2. このフォルダの内容をリポジトリのルートにプッシュ
3. リポジトリの Settings → Pages を開く
4. Source: **Deploy from a branch** を選択
5. Branch: `main` / フォルダ: `/ (root)` を選択 → Save

公開URL例:
```
https://username.github.io/aju-works-site/
```

> `username` は GitHub のユーザー名に置き換えてください。

---

## 差し替えが必要な箇所

公開前に以下のプレースホルダーを実際の情報に変更してください。

| 項目 | プレースホルダー | 対象ファイル |
|------|-----------------|-------------|
| メールアドレス | `contact@example.com` | 全HTMLファイル・README |
| 所在地 | `〒XXX-XXXX 東京都〇〇区〇〇 X-X-X` | about.html |
| 電話番号 | `XXX-XXXX-XXXX` | about.html |
| OGP URL | `https://example.com/` | 全HTMLファイル |
| Google Play URL | `href="#"` | apps.html（ボタン） |

### 一括置換の方法（VS Code）

1. VS Codeでフォルダを開く
2. `Ctrl+Shift+H`（検索と置換）
3. 「ファイルで置換」で上記のプレースホルダーを検索・置換

---

## ジム記録＆ベンチコーチ専用プライバシーポリシー

現在このURL（既存デプロイ済み）が各所に記載されています:

```
https://gym-record-bench-coach-policy.vercel.app/privacy
```

**差し替えタイミング:**
- Vercelのデプロイを終了する場合 → 上記URLを `privacy.html` のURLに変更
- アプリ専用ポリシーを本サイトに移行する場合 → `privacy.html` を更新してURLを切り替え

---

## Google Play Console に登録するURL

アプリを Google Play Console に登録する際、以下のURLを使用してください。

| 用途 | URL |
|------|-----|
| プライバシーポリシー（アプリ固有） | `https://gym-record-bench-coach-policy.vercel.app/privacy` |
| プライバシーポリシー（Aju Works共通） | `https://username.github.io/aju-works-site/privacy.html` |
| サポートURL | `https://username.github.io/aju-works-site/support.html` |

> `username` はGitHubユーザー名に置き換えてください。  
> 独自ドメインを取得した場合はそちらのURLに変更してください。

---

## プライバシーポリシー更新時の注意

- `privacy.html` の「最終更新」日付（ドキュメントメタ部分）を更新してください
- アプリのストア（Google Play Console）に登録しているURLが変わる場合は、Console上でも更新が必要です
- 大幅な変更を行う場合は、ユーザーへの告知を検討してください

---

## 費用について

| 項目 | 費用 |
|------|------|
| GitHub Pages | **無料**（パブリックリポジトリの場合） |
| 独自ドメイン | 不使用（github.io サブドメインを利用） |
| 外部サービス | なし（CDN等の依存ゼロ） |

> **規約変更リスクの注記:**  
> GitHub Pages の無料提供条件は GitHub の利用規約変更により変わる可能性があります。  
> 将来的に独自ドメイン・外部ホスティングへの移行を検討する場合も、全ファイルが静的HTMLのため移行は容易です。

---

## 更新履歴

| 日付 | 内容 |
|------|------|
| 2026年5月 | 初版作成 |

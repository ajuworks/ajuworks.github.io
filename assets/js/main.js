/**
 * Aju Works — メインJavaScript
 * 機能:
 *   1. ハンバーガーメニューの開閉
 *   2. FAQアコーディオン
 *   3. 現在ページのナビリンクにactiveクラスを付与
 */

(function () {
  'use strict';

  /* -----------------------------------------------------------------------
     DOMContentLoaded 後に全処理を起動
  ----------------------------------------------------------------------- */
  document.addEventListener('DOMContentLoaded', function () {
    initHamburger();
    initFAQ();
    initActiveNav();
  });

  /* -----------------------------------------------------------------------
     1. ハンバーガーメニュー
        .hamburger クリック → .hamburger と .mobile-menu に "open" をトグル
  ----------------------------------------------------------------------- */
  function initHamburger() {
    var hamburger   = document.querySelector('.hamburger');
    var mobileMenu  = document.querySelector('.mobile-menu');

    if (!hamburger || !mobileMenu) return;

    hamburger.addEventListener('click', function () {
      var isOpen = hamburger.classList.toggle('open');
      mobileMenu.classList.toggle('open', isOpen);

      // アクセシビリティ: aria-expanded
      hamburger.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    });

    // モバイルメニュー内リンクをクリックしたら閉じる
    mobileMenu.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () {
        hamburger.classList.remove('open');
        mobileMenu.classList.remove('open');
        hamburger.setAttribute('aria-expanded', 'false');
      });
    });

    // メニュー外クリックで閉じる
    document.addEventListener('click', function (e) {
      if (!hamburger.contains(e.target) && !mobileMenu.contains(e.target)) {
        hamburger.classList.remove('open');
        mobileMenu.classList.remove('open');
        hamburger.setAttribute('aria-expanded', 'false');
      }
    });
  }

  /* -----------------------------------------------------------------------
     2. FAQアコーディオン
        .faq-question クリック → 親の .faq-item に "open" をトグル
        他の項目は閉じる（1つだけ開く挙動）
  ----------------------------------------------------------------------- */
  function initFAQ() {
    var questions = document.querySelectorAll('.faq-question');

    if (!questions.length) return;

    questions.forEach(function (question) {
      question.addEventListener('click', function () {
        var item    = question.closest('.faq-item');
        var isOpen  = item.classList.contains('open');

        // 全項目を閉じる
        document.querySelectorAll('.faq-item').forEach(function (i) {
          i.classList.remove('open');
          var btn = i.querySelector('.faq-question');
          if (btn) btn.setAttribute('aria-expanded', 'false');
        });

        // クリックした項目だけ開く（既に開いていたら閉じたまま）
        if (!isOpen) {
          item.classList.add('open');
          question.setAttribute('aria-expanded', 'true');
        }
      });

      // 初期状態: 全部閉じ
      question.setAttribute('aria-expanded', 'false');
    });
  }

  /* -----------------------------------------------------------------------
     3. アクティブナビリンク
        現在のページパスと href を比較し、一致するリンクに "active" を付与
        ヘッダー (.site-nav) とモバイルメニュー (.mobile-menu) 両方に適用
  ----------------------------------------------------------------------- */
  function initActiveNav() {
    var currentPath = window.location.pathname;

    // パス末尾のスラッシュを統一 & ファイル名だけ取り出す
    var currentFile = currentPath.split('/').pop() || 'index.html';

    // index.html か / の場合は index.html として扱う
    if (currentFile === '' || currentFile === '/') {
      currentFile = 'index.html';
    }

    var navLinks = document.querySelectorAll('.site-nav a, .mobile-menu a');

    navLinks.forEach(function (link) {
      var href     = link.getAttribute('href') || '';
      var hrefFile = href.split('/').pop() || 'index.html';

      // 空 href (ルートリンク) は index.html 扱い
      if (hrefFile === '' || hrefFile === '/') {
        hrefFile = 'index.html';
      }

      if (hrefFile === currentFile) {
        link.classList.add('active');
      } else {
        link.classList.remove('active');
      }
    });
  }

})();

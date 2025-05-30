plugins = [
    "aster.vscode-subtitles",
    "visualstudioexptteam.vscodeintellicode",
    "intellsmi.comment-translate",
    "ms-vscode.hexeditor",
    "golang.go",
    "github.remotehub",
    "mechatroner.rainbow-csv",
    "vscjava.vscode-gradle",
    "ms-python.python",
    "stxr.iconfont-preview",
    "get-snippets.get-snippets",
    "dart-code.flutter",
    "redhat.vscode-xml",
    "wayou.vscode-todo-highlight",
    "cpylua.language-postcss",
    "ecmel.vscode-html-css",
    "bradlc.vscode-tailwindcss",
    "devsense.intelli-php-vscode",
    "aminer.codegeex",
    "ms-vscode.cpptools",
    "wangxinhai-ref-chunsen.flutter-code-select",
    "visualstudioexptteam.intellicode-api-usage-examples",
    "ms-vscode.remote-repositories",
    "pkief.material-icon-theme",
    "unifiedjs.vscode-mdx",
    "formulahendry.code-runner",
    "ms-vscode.makefile-tools",
    "ms-python.black-formatter",
    "mkxml.vscode-filesize",
    "techer.open-in-browser",
    "twxs.cmake",
    "oderwat.indent-rainbow",
    "kisstkondoros.vscode-gutter-preview",
    "leizongmin.node-module-intellisense",
    "rust-lang.rust-analyzer",
    "humao.rest-client",
    "ritwickdey.liveserver",
    "njpwerner.autodocstring",
    "uctakeoff.vscode-counter",
    "ms-toolsai.jupyter-renderers",
    "ms-vscode.cmake-tools",
    "christian-kohler.npm-intellisense",
    "devsense.profiler-php-vscode",
    "ms-toolsai.vscode-jupyter-slideshow",
    "tauri-apps.tauri-vscode",
    "tamasfe.even-better-toml",
    "devsense.phptools-vscode",
    "christian-kohler.path-intellisense",
    "moshfeu.compare-folders",
    "slint.slint",
    "russell.any-rule",
    "formulahendry.auto-rename-tag",
    "ms-vscode.cpptools-extension-pack",
    "google.arb-editor",
    "github.vscode-github-actions",
    "ms-python.vscode-pylance",
    "nash.awesome-flutter-snippets",
    "vadimcn.vscode-lldb",
    "maggie.eslint-rules-zh-plugin",
    "ms-ceintl.vscode-language-pack-zh-hans",
    "esbenp.prettier-vscode",
    "dotjoshjohnson.xml",
    "ms-toolsai.jupyter",
    "tomoki1207.pdf",
    "tobermory.es6-string-html",
    "devsense.composer-php-vscode",
    "ms-vscode.powershell",
    "nuxtr.nuxtr-vscode",
    "dart-code.dart-code",
    "ms-toolsai.jupyter-keymap",
    "usernamehw.errorlens",
    "geezmolycos.vscode-hanzi-counter",
    "ms-python.debugpy",
    "ms-vscode.cpptools-themes",
    "hediet.vscode-drawio",
    "jeff-hykin.polacode-2019",
    "editorconfig.editorconfig",
    "wangrongding.fanyi",
    "miguelsolorio.fluent-icons",
    "dbaeumer.vscode-eslint",
    "vue.volar",
    "ms-python.flake8",
    "ms-toolsai.vscode-jupyter-cell-tags",
]

import os

for plugin in plugins:
    r = os.popen(f"code --install-extension {plugin}")
    print(r.read())


print("Done.")

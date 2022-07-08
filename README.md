# vim-flypy

## 安装

### Vim Plug

在 `init.vim` 中 `call plug#end()` 前添加如下代码：

```vim
Plug 'OverflowCat/vim-flypy'
```

## 配置

```vim
" YWVIM IME

let g:ywvim_ims=[ 
            \['eh', '鹤形', 'flypy.ywvim'],
            \]

let g:ywvim_eh = { 'matchexact': 1 }
" 小鹤的简称是 eh

let g:ywvim_zhpunc = 1
let g:ywvim_listmax = 5
let g:ywvim_esc_autoff = 0
let g:ywvim_autoinput = 1
let g:ywvim_circlecandidates = 1
let g:ywvim_helpim_on = 0
let g:ywvim_matchexact = 1
let g:ywvim_chinesecode = 1
let g:ywvim_gb = 0
let g:ywvim_preconv = 'g2b'
let g:ywvim_conv = ''
let g:ywvim_lockb = 1
```

目前的四码上屏貌似有 bug，如果需要候选唯一自动上屏，请将 `let g:ywvim_eh = { 'matchexact': 1 }` 中的 1 改为 0，并且将 `let g:ywvim_matchexact = 1` 改为 2。

## 输入法切换

加入小鹤音形码表作为默认方案。

## 使用

按 <kbd>Ctrl</kbd> + <kbd>\\</kbd> 可以启用输入法，按 <kbd>Ctrl</kbd> + <kbd>6</kbd> 可以切换输入方案。

### 英文输入

按 <kbd>;</kbd> 切换中英文输入。
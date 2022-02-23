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
let g:ywvim_matchexact = 0
let g:ywvim_chinesecode = 1
let g:ywvim_gb = 0
let g:ywvim_preconv = 'g2b'
let g:ywvim_conv = ''
let g:ywvim_lockb = 1
```

## 输入法切换

加入小鹤音形码表作为默认方案。

## 使用

## 与英文混排输入的问题


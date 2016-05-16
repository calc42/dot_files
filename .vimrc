set autoindent
set smartindent
set smartcase
set showmatch
set number
set tabstop=4
set shiftwidth=4
set expandtab
set nowrapscan
inoremap <C-j> <esc>

nnoremap ; :
nnoremap : ;

noremap i <up>
noremap k <down>
noremap j <left>
"行頭、行末
noremap <space>u ^
noremap <space>o $
nnoremap <space>do d$
nnoremap <space>du d0
"% 括弧移動
noremap <space>m %
nnoremap h i
nnoremap H I
nnoremap I H

"msで開始行を指定、y/d'sで終了行を指定
nnoremap <space>y y's
nnoremap <space>d d's
"X backspace
nnoremap t X

"inoremap {<Enter> {}<Left><LF><ESC><S-o><Tab>
inoremap {<Enter> {<LF>}<ESC><S-o>
"inoremap () ()<Left>
"inoremap <> <><Left>
"inoremap [] []<Left>
"inoremap "" ""<Left>
"inoremap {} {}<Left>
"inoremap '' ''<Left>

inoremap <C-d> <Del>

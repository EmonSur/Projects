start:

call 70
org 70
 in 00
 sub al, 30
 mul al, 0a
 push al
 pop bl

 in 00
 sub al, 30
 add al, bl
ret

finish:
end

 cmp al, 63
 jz finish


call 70
org 70
push al
pop bl
div al, 0a
add al, 30
mov[c0], al
mod bl, 0a
add bl, 30
mov [c1], bl

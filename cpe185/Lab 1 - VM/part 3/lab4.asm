cseg segment 'code'
assume cs:cseg, ds:cseg, ss:cseg, es:cseg

	org 100h

start: mov cx,10  
       mov ah,9

again:  mov dx, offset Hello
        int 21h
 	mov dx, offset Num_msg
 	int 21h
 	inc byte ptr Num_msg  	
	loopne again			


done: mov ah, 4ch
 	int 21h

	org 200h 
 
Hello db "Hello World", 20h, 20h, "$" 


Num_msg db 30h,13,10, 36 
 
cseg ends
end start
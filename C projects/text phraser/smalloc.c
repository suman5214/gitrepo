#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/mman.h>
#include "smalloc.h"



void *mem;
struct block *freelist;
struct block *allocated_list;
int checkInit = 0;   //this is for avoiding re-initiation



void *smalloc(unsigned int nbytes) {
    struct block *cur = freelist;

     while(cur!=NULL){  
            if (cur ->size >= nbytes){                                 //check for enough space in the freelist
                struct block *tempBlock;
                tempBlock= malloc(sizeof(struct block));
                tempBlock->addr = cur ->addr;
                tempBlock->size = nbytes;
                tempBlock->next = NULL;
                cur->addr = cur->addr + nbytes;
                cur ->size = cur ->size - nbytes;
    
                if(allocated_list == NULL){
					allocated_list = tempBlock;
                    }
                else{
                    cur = allocated_list;
                    while(cur->next!=NULL){
                         cur =cur->next;
                        }
                    cur->next=tempBlock;
                    }
                return (tempBlock->addr);   
            }
            cur = cur->next;
    }

    return NULL;
}


int sfree(void *addr) {
    struct block *cur = allocated_list;
    struct block *tempBlock;
    while(cur!=NULL){
        if(allocated_list->next==NULL&&allocated_list->addr == addr){   //special case where allocated_list is the only allocated block in list.
            tempBlock = allocated_list;
            allocated_list=NULL;
            
            }
        else if (cur ->next->addr == addr){
                tempBlock=cur->next;        //disjoint the matched block from the allocated_list
                cur->next = cur->next->next;
                tempBlock->next = NULL;     // set the matched block pointing to null

            }
            cur= cur->next;
        if(tempBlock!=NULL){
            cur = freelist;
            while(cur->next!=NULL){
                cur =cur->next;
                }
            cur->next=tempBlock;
                
            return(0);
        }

    }
    return -1;
}

/* Initialize the memory space used by smalloc,
 * freelist, and allocated_list
 * Note:  mmap is a system call that has a wide variety of uses.  In our
 * case we are using it to allocate a large region of memory. 
 * - mmap returns a pointer to the allocated memory
 * Arguments:
 * - NULL: a suggestion for where to place the memory. We will let the 
 *         system decide where to place the memory.
 * - PROT_READ | PROT_WRITE: we will use the memory for both reading
 *         and writing.
 * - MAP_PRIVATE | MAP_ANON: the memory is just for this process, and 
 *         is not associated with a file.
 * - -1: because this memory is not associated with a file, the file 
 *         descriptor argument is set to -1
 * - 0: only used if the address space is associated with a file.
 */

void mem_init(int size) {
	if (checkInit == 1){                      //check if a previous memory area still exists
         perror("re-initiate");
         return;

    }
	else{
    mem = mmap(NULL, size,  PROT_READ | PROT_WRITE, MAP_PRIVATE | MAP_ANON, -1, 0);
    if(mem == MAP_FAILED) {
         perror("mmap");
         exit(1);
    }

    
		printf("1236781263812678326187\n\n\n");
        freelist = malloc(sizeof(struct block));
        freelist ->size = size;
        freelist ->next = NULL;
        freelist ->addr = mem;


        allocated_list= NULL;
        checkInit = 1; 

    }

    /* NOTE: this function is incomplete */

}

void mem_clean(){
    struct block *cur = freelist;
	struct block *tempBlock;
    while(cur!=NULL){
		tempBlock = cur->next;
        //munmap(cur->addr,cur->size);
        free(cur);
        cur = tempBlock;
    }
    cur = allocated_list;
    while(cur!=NULL){
    	tempBlock = cur->next;
        //munmap(cur->addr,cur->size);
        free(cur);
        cur = tempBlock;
    }
	checkInit = 0;

}
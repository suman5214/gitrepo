/*In this test case, I'm initiating an extra area of memory by using mem_init in the middle of some memory allocating, I'm trying to simulate a situation where a user accidently initiates another area of memory before clearing and how will this cause memory leak in the program.*/
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/mman.h>
#include "smalloc.h"


#define SIZE 360


/* Simple test for smalloc and sfree. */

int main(void) {

    mem_init(SIZE);
    void *ptrs[5];
    
    ptrs[0] = smalloc(16);
    write_to_mem(16, ptrs[0], 0);
    ptrs[1] = smalloc(32);
    write_to_mem(32, ptrs[1], 1);
    mem_init(100);             //initating the second memory area before clearing everything
    ptrs[2] = smalloc(24);
    write_to_mem(24, ptrs[2], 2);
    
    printf("List of allocated blocks:\n");
    print_allocated();
    printf("List of free blocks:\n");
    print_free();
    printf("Contents of allocated memory:\n");
    print_mem();
    
    printf("freeing %p result = %d\n", ptrs[1], sfree(ptrs[1]));
    
    printf("List of allocated blocks:\n");
    print_allocated();
    printf("List of free blocks:\n");
    print_free();
    printf("Contents of allocated memory:\n");
    print_mem();

    mem_clean();
    return 0;
}
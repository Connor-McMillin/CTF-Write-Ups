This challenge wants us to run the program with some fun arguments which would screw up a shell. Thankfully we have the power of pwntools. Also to solve we need to execute this on angstrom's shell on their site. There is a setuid binary that can access the flag which we cannot. Below we can see what we need to do to make it print the flag.

```c
#define _GNU_SOURCE

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <unistd.h>

#define FLAGSIZE 128

void print_flag() {
    gid_t gid = getegid();
    setresgid(gid, gid, gid);
    FILE *file = fopen("flag.txt", "r");
    char flag[FLAGSIZE];
    if (file == NULL) {
        printf("Cannot read flag file.\n");
        exit(1);
    }
    fgets(flag, FLAGSIZE, file);
    printf("%s", flag);
}

int main(int argc, char* argv[]) {
    setvbuf(stdout, NULL, _IONBF, 0);
    if (argc != 2) {
        puts("Your argument count isn't right.");
        return 1;
    }
    if (strcmp(argv[1], " \n'\"\x07")) {
        puts("Your argument isn't right.");
        return 1;
    }
    char buf[128];
    fgets(buf, 128, stdin);
    if (strcmp(buf, "\x00\x01\x02\x03\n")) {
        puts("Your input isn't right.");
        return 1;
    }
    puts("You seem to know what you're doing.");
    print_flag();
}
```

So first we need to have exactly 2 arguments to the program (really one since argv[0] is the program name), where the argument we pass in has a newline among other characters. Next we need to input the bytes 0, 1, 2, 3 then a newline. The solve script shows how to do this with pwntools

flag: actf{impr4ctic4l\_pr0blems\_c4ll\_f0r\_impr4ctic4l\_s0lutions}

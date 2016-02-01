/*
 * socket demonstrations:
 * This is the server side of an "internet domain" socket connection, for
 * communicating over the network.
 *
 * In this case we are willing to wait either for chatter from the client
 * _or_ for a new connection.
*/

#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <sys/time.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <time.h>
#ifndef PORT
#define PORT 58277
#endif

#define MAXNAME 20
#define MAXMSG 50
struct client {
    int fd, lastFD;
    struct in_addr ipaddr;
    struct client *next;
    char name[MAXNAME], msg[MAXMSG];
    int powerMove, hitpoints;
    int turn,nameSetupFinish, namecounter, speaking,speakcounter;
};

static struct client *addclient(struct client *top, int fd, struct in_addr addr);
static struct client *removeclient(struct client *top, int fd);
static void broadcast(struct client *top,struct client *p, char *s, int size);
int handleclient(struct client *p, struct client *top);
int checkName(struct client *p, struct client *head,char *nbyte);
int checkSpeak(struct client *p, struct client *head,char *nbyte);
int bindandlisten(void);
int searchOpponent(struct client *p,struct client *head);
int findLastNewLine(char *str);
int checkGameStatus(struct client *p, struct client *head);
int gamePrep(struct client *p);
int playGame(struct client *p, struct client *head,int option);
int main(void) {
    int clientfd, maxfd, nready;
    struct client *p;
    struct client *head = NULL;
    socklen_t len;
    struct sockaddr_in q;
    fd_set allset;
    fd_set rset;
    srand (time(NULL) );
    int i;


    int listenfd = bindandlisten();
    // initialize allset and add listenfd to the
    // set of file descriptors passed into select
    FD_ZERO(&allset);
    FD_SET(listenfd, &allset);
    // maxfd identifies how far into the set to search
    maxfd = listenfd;

    while (1) {
        // make a copy of the set before we pass it into select
        rset = allset;
        nready = select(maxfd + 1, &rset, NULL, NULL, NULL);

        if (nready == -1) {
            perror("select");
            continue;
        }

        if (FD_ISSET(listenfd, &rset)){
            printf("a new client is connecting\n");
            len = sizeof(q);
            if ((clientfd = accept(listenfd, (struct sockaddr *)&q, &len)) < 0) {
                perror("accept");
                exit(1);
            }
            FD_SET(clientfd, &allset);
            if (clientfd > maxfd) {
                maxfd = clientfd;
            }
            printf("connection from %s\n\n", inet_ntoa(q.sin_addr));
            char welcome[40] = "Welcome \nPlease enter your name \r\n";

            head = addclient(head, clientfd, q.sin_addr);
            if(head->turn <0){
                write(clientfd,welcome,sizeof(welcome)-1);
            }
            }
        for(i = 0; i <= maxfd; i++) {
            if (FD_ISSET(i, &rset)) {
                for (p = head; p != NULL; p = p->next) {
                    if (p->fd == i) {
                        int result = handleclient(p, head);
                        if (result == -1) {
                            int tmp_fd = p->fd;
                            head = removeclient(head, p->fd);
                            FD_CLR(tmp_fd, &allset);
                            close(tmp_fd);
                        }
                        break;
                        }
                    }
                }
            }
        for (p = head; p != NULL; p = p->next) {
                //indicates a name is setup and ready for search
            searchOpponent(p,head);
        }
    }
    return 0;
}

int checkName(struct client *p, struct client *head,char *nbyte){

        char newlineC[2] = "\n";
        if(p->namecounter <0){
            return 1;
        }
        else if((strstr(nbyte,newlineC)!=NULL)){

                if(p->nameSetupFinish == 0){
                    char message_search[25] = "Searching for opponent\n";
                    write(p->fd,message_search,sizeof(message_search)-1);

                        char message_cast[30];
                        sprintf(message_cast,"--%s joined the arena--\n",p->name);
                        int index = findLastNewLine(message_cast);

                        broadcast(head,p,message_cast,index);
                    p->nameSetupFinish = 1;

                }
                p->namecounter = -1;   //stop buffering line for name collection.
        return 1;
        }
        else{
        (p->name)[p->namecounter] = *nbyte;
        p->namecounter = p->namecounter + 1;
        return 0;
        }
}

int checkSpeak(struct client *p, struct client *head,char *nbyte){
            struct client *top;
            for(top=head;top!= NULL;top=top->next){
            if(top->fd == p->lastFD){
                break;
                }
            }
        char newlineC[2] = "\n";

        if((strstr(nbyte,newlineC)!=NULL)){
            (p->msg)[p->speakcounter] = *nbyte;
        int index = findLastNewLine(p->msg);
        char message[38] = "Your opponent took a break and said :\n";
        write(top->fd,message,38);
        write(top->fd,p->msg,index);
            memset(p->msg, 0, sizeof(p->msg));
            p->speaking = 0;
            p->speakcounter = 0;
            checkGameStatus(p,head);
        }
        else{
        (p->msg)[p->speakcounter] = *nbyte;
        p->speakcounter = p->speakcounter + 1;
        }
        return 0;

}

int searchOpponent(struct client *p,struct client *head){
    struct client *top;
    if (p->turn <0){                            // client is only send for searching if not in a game.  turn = 0 : in turn/waiting, turn = 1 : in turn/attacking, turn <0 : not in a game
        for(top=head;top!= NULL;top=top->next){
            if(top->turn <0){
                if(top->fd != p->fd && top->lastFD != p->fd &&p->namecounter < 0&&top->namecounter < 0){

                            int luck = rand()%2;
                                if (luck ==0){
                                top->turn = 0;
                                p->turn = 1;
                                    }
                                else{
                                top->turn = 1;
                                p->turn = 0;
                                    }

                                top->lastFD = p->fd;
                                p->lastFD = top->fd;
                                gamePrep(p);
                                gamePrep(top);
                                char message_found[30];
                                int lastIndex = 0;
                                sprintf(message_found,"opponent found! :%s\n\n",top->name);
                                lastIndex = findLastNewLine(message_found);
                                write(p->fd,message_found,lastIndex);
                                sprintf(message_found,"opponent found! :%s\n\n",p->name);
                                lastIndex = findLastNewLine(message_found);
                                write(top->fd,message_found,lastIndex);
                                checkGameStatus(p,head);
                                checkGameStatus(top,head);
                                break;
                            }
                    }
        }
    }
        return 0;
}
int findLastNewLine(char *str){
    int lastIndex = 0;
    char * pch=strchr(str,'\n');
        while (pch!=NULL){
            lastIndex = pch - str;
            pch=strchr(pch+1,'\n');
            }
    return lastIndex + 1;
}

int checkGameStatus(struct client *p, struct client *head){
    struct client *top;
            for(top=head;top!= NULL;top=top->next){
            if(top->fd == p->lastFD){
                break;
                }
            }
    if(p->hitpoints <=0){
            char message_search[25] = "Searching for opponent\n";
            char message_lost[19] = "You lost the game\n";
            write(p->fd,message_lost,sizeof(message_lost)-1);
            write(p->fd,message_search,sizeof(message_search)-1);
            char message_win[18] = "\nYou won the game\n";
            write(top->fd,message_win,sizeof(message_win)-1);
            write(top->fd,message_search,sizeof(message_search)-1);
            p->turn = -1;
            top->turn = -1;

    }
    else if (p->turn == 0){
        char message_wait[30] = "\nWaiting for opponent move\n";
        char status[100];
        sprintf(status,"Your hitpoints: %d\nYour powermoves: %d\n%s's hitpoints: %d\n",p->hitpoints,p->powerMove,top->name,top->hitpoints);
        int lastIndex = findLastNewLine(status);
        write(p->fd,message_wait,sizeof(message_wait)-1);
        write(p->fd,status,lastIndex);

    }
    else if(p->turn ==1){
        char status[200];
        sprintf(status,"Its your turn!\nYour hitpoints: %d\nYour powermoves: %d\n%s's hitpoints: %d\n\n(A)ttack\n(P)owermove\n(S)peak\n",p->hitpoints,p->powerMove,top->name,top->hitpoints);
        int lastIndex = findLastNewLine(status);

        write(p->fd,status,lastIndex);

    }
    return 0;
}

int gamePrep(struct client *p){

        p ->powerMove = rand()%4;
        p ->hitpoints = rand()%11 +20;

        return 0;

}

int playGame(struct client *p, struct client *head,int option){
        struct client *top ;

        for(top= head;top!= NULL;top=top->next){
        if (top->fd == p->lastFD){
            int damage = rand()%5+2;

            if(option == 0){                                    // check for the option that client typed
                top->hitpoints = top->hitpoints - damage;
                char message_hit[50];
                sprintf(message_hit,"%s hits you for %d damage!\n",p->name,damage);
                int index= findLastNewLine(message_hit);
                write(top->fd,message_hit,index);
            }
            else if (option == 1){                              // check for the option that client typed
                int luck = rand()%2;
                if (p -> powerMove > 0){
                    p ->powerMove = p ->powerMove -1;
                    if(luck ==1){
                        top->hitpoints = top->hitpoints - (damage*3);
                        char message_hit[50];
                        sprintf(message_hit,"%s hits you for %d damage!\n",p->name,damage*3);
                        int index= findLastNewLine(message_hit);
                        write(top->fd,message_hit,index);
                        }
                    else{
                        char message_hit[50];
                        sprintf(message_hit,"%s hits you for %d damage!\n",p->name,0);
                        int index= findLastNewLine(message_hit);
                        write(top->fd,message_hit,index);
                    }
                }else{
                    char message[30] = "\nNot enough powerMove points\n";
                    write(p->fd,message,strlen(message)-1);
                    return 0;
                }
            }
            top->turn = 1;
            p->turn = 0 ;
            checkGameStatus(top,head);
            checkGameStatus(p,head);
        }
    }
    return 0;
}

int handleclient(struct client *p, struct client *head) {

    const char optionA[2]="a";
    const char optionP[2]="p";
    const char optionS[2]="s";
    char buf[256];
    int len = read(p->fd, buf, sizeof(buf) - 1);
    if (len > 0) {

        buf[len] = '\0';
        int result = checkName(p,head,buf);

        if (result){                        // check if the client name is set up.

            if(p->turn==1){
                if(p->speaking ==1){             // check if the client name is trying to speak.
            checkSpeak(p,head,buf);
                    }
            else{
                if(strstr(buf,optionA) !=NULL){
                   playGame(p,head,0);

                   }
                    else if(strstr(buf,optionP) !=NULL){
                   playGame(p,head,1);

                   }
                   else if(strstr(buf,optionS) !=NULL){
                        p->speaking = 1;
                        char message_speak[8] = "\nspeak: ";
                        write(p->fd,message_speak,7);

                   }
            }
            }

        }

        return 0;
    } else if (len == 0) {
        char message_leave[30];
        sprintf(message_leave,"--%s left the arena--\n",p->name);
        int index = findLastNewLine(message_leave);

        broadcast(head,p,message_leave,index);

        struct client *top;
        char message_search[25] = "Searching for opponent\n";
        char message_dc[50] = "Your opponent left the game \nYou won the game\n";
        for(top = head;top!= NULL;top=top->next){
            if (top->fd == p->lastFD){
                write(top->fd,message_dc,sizeof(message_dc)-1);
                write(top->fd,message_search,sizeof(message_search)-1);

                top->turn = -1;
            }
        }
        return -1;
    } else {
        perror("read");
        return -1;
    }
}


 /* bind and listen, abort on error
  * returns FD of listening socket
  */
int bindandlisten(void) {
    struct sockaddr_in r;
    int listenfd;

    if ((listenfd = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
        perror("socket");
        exit(1);
    }
    int yes = 1;
    if ((setsockopt(listenfd, SOL_SOCKET, SO_REUSEADDR, &yes, sizeof(int))) == -1) {
        perror("setsockopt");
    }
    memset(&r, '\0', sizeof(r));
    r.sin_family = AF_INET;
    r.sin_addr.s_addr = INADDR_ANY;
    r.sin_port = htons(PORT);

    if (bind(listenfd, (struct sockaddr *)&r, sizeof r)) {
        perror("bind");
        exit(1);
    }

    if (listen(listenfd, 5)) {
        perror("listen");
        exit(1);
    }
    return listenfd;
}

static struct client *addclient(struct client *top, int fd, struct in_addr addr) {
    struct client *p = malloc(sizeof(struct client));
    if (!p) {
        perror("malloc");
        exit(1);
    }

    printf("Adding client %s\n", inet_ntoa(addr));
    (p->name)[0] = '\0';
    (p->msg)[0] = '\0';
    p->turn = -1;
    p->speaking = 0;
    p->lastFD = -1;
    p->nameSetupFinish = 0;
    p->namecounter = 0;
    p->speakcounter = 0;
    p->fd = fd;
    p->ipaddr = addr;
    p->next = top;
    top = p;
    return top;
}

static struct client *removeclient(struct client *top, int fd) {
    struct client **p;

    for (p = &top; *p && (*p)->fd != fd; p = &(*p)->next)
        ;
    if (*p) {
        struct client *t = (*p)->next;
        printf("Removing client %d %s\n", fd, inet_ntoa((*p)->ipaddr));
        free(*p);
        *p = t;
    } else {
        fprintf(stderr, "Trying to remove fd %d, but I don't know about it\n",
                 fd);
    }
    return top;
}


static void broadcast(struct client *head,struct client *p, char *s, int size) {
    struct client *top;
    for (top = head; top; top = top->next) {
            if(top ->fd != p->fd){
        write(top->fd, s, size);
            }
    }
}


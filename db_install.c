#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(void){
    char dump[30], database[30], username[30], password[30], c;
    int i=0;
    password[0]='\0';
    printf("login amministratore del database.\n");
    printf("username:");
    scanf("%s",username);
    printf("\npassword:");
    scanf("%s",password);
    printf("\ndump sql da inserire: ");
    scanf("%s",dump);
    while((c=dump[i]) != '.'){
        database[i]= c;
        i++;
    }
    database[i] = '\0';
    printf("\n%s, %s, %s, %s",dump,database,username,password);
}
        
        
    
    
    

#include <stdio.h>
int main(void){

    struct horario
    {
        int hora;
        int minuto;
        int segundo;
    };
    struct horario agora, *depois;

    depois = &agora;

    //(*depois).hora = 20;
    //(*depois).minuto = 20;
   // (*depois).segundo = 20;
    // ou :
    depois->hora=20;
    depois->minutos=20;
    depois->segundos=20;

    printf("%i %i %i", agora.hora, agora.minuto, agora.segundo);

    return 0;
}
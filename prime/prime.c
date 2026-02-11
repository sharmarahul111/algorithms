#include<stdio.h>
int main(){
  FILE *fp;
  fp = fopen("data.csv", "w");
  if(fp==NULL) {
    printf("File couldn't be opened!\n");
    return 1;
  }
  int count = 80000;
  int i;
  int is_prime=1;
  int leny = 1;
  int y[count];
  y[0] = 2;
  int x = 3;
  while(leny < count){
    for (i=0;i<leny;i++) {
      if(x%y[i]==0){
        is_prime = 0;
        break;
      }
    }
    if(is_prime){
      y[leny] = x;
      leny++;
    } else is_prime = 1;
    x+=2;
    printf("\r%.2f%%",(float) leny/count*100);
  }
  printf("\nPrimes generated!");
  printf("\nSaving to file");
  for (i=0;i<leny-1;i++) {
    fprintf(fp, "%d,",y[i]);
  }
  fprintf(fp,"%d", y[i]);
  fclose(fp);
  printf("\rSuccessfully saved to file!\n");
  return 0;
}

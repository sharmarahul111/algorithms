#include<stdio.h>
#include<stdlib.h>
#define BUF_SIZE 65536
int main(){
  FILE *fp;
  char buffer[BUF_SIZE];
  size_t pos= 0;
  fp = fopen("data.csv", "wb");
  if(fp==NULL) {
    printf("File couldn't be opened!\n");
    return 1;
  }
  int count = 7000000;
  int i,n;
  int is_prime=1;
  int leny = 1;
  // DMA cuz stack can't handle it
  long long *y  = malloc(count * sizeof(long long));
  long long *y2 = malloc(count * sizeof(long long));
  if (!y || !y2) {
    printf("Memory allocation failed\n");
    return 1;
  }
  y[0] = 2;
  y2[0] = 4;

  long long int x = 3;
  while(leny < count){
    for (i=0;i<leny;i++) {
      if (y2[i]> x) break;
      if(x%y[i]==0){
        is_prime = 0;
        break;
      }
    }
    if(is_prime){
      y[leny] = x;
      y2[leny] = x*x;
      leny++;
    } else is_prime = 1;
    x+=2;
    if(leny%5000==0) printf("\r%.2f%%",(float) leny/count*100);
  }
  printf("\nPrimes generated!");
  printf("\nSaving to file");
  // save logic
  for (i=0;i<leny-1;i++) {
    int n = snprintf(buffer + pos, BUF_SIZE - pos, "%lld,", y[i]);
    pos += n;
    if (pos >= BUF_SIZE - 50) {
      fwrite(buffer,1,pos,fp);
      pos = 0;
    }
  }
  if (pos > 0) fwrite(buffer, 1, pos, fp);
  fclose(fp);
  printf("\rSuccessfully saved to file!\n");
  return 0;
}

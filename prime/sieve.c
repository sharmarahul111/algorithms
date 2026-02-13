#include<stdio.h>
#include<stdlib.h>
#define BUF_SIZE 65536
void display(unsigned char *);
void prime_count(unsigned char *);
void save(unsigned char *);
// int count = 100;
size_t count = 1000000;
// size_t count = 32452842;
int main(){
  // DMA cuz stack can't handle it
  size_t i,j;
  unsigned char *y  = calloc(count, sizeof(unsigned char));
  if (!y) {
    printf("Memory allocation failed\n");
    return 1;
  }
  printf("Memory alloted...\n");
  // 0 = prime
  // 1 = non-prime
  y[0] = 1;
  y[1] = 1;
  for (i=0;i<count;i++) {
    if(i%100000==0) printf("\r%.2f%%",(float) i/count*100);
    if(y[i]) continue;
    for (j=i+i;j<count;j+=i) y[j]=1;
  }
  printf("\n");
  prime_count(y);
  // display(y);
  save(y);
  return 0;

}
void display(unsigned char *y){
  size_t i;
  for (i=0;i<count;i++) {
    if(y[i]==0){
      printf("%zu,",i);
    }
  }
}

void prime_count(unsigned char *y){
  printf("Counting...\n");
  size_t i,len=0;
  for (i=0;i<count;i++) {
    if(y[i]==0) len++;
  }
  printf("Total primes generated: %zu\n",len);
}

void save(unsigned char *y){
  printf("Saving to file...");
  FILE *fp;
  char buffer[BUF_SIZE];
  size_t pos= 0;
  fp = fopen("sieve-data.csv", "wb");
  if(fp==NULL) {
    printf("File couldn't be opened!\n");
    exit(1);
  }
  // save logic
  size_t i;
  for (i=0;i<count;i++) {
    if(y[i]) continue;
    int n = snprintf(buffer + pos, BUF_SIZE - pos, "%zu,", i);
    pos += n;
    if (pos >= BUF_SIZE - 50) {
      fwrite(buffer,1,pos,fp);
      pos = 0;
    }
  }
  if (pos > 0) fwrite(buffer, 1, pos, fp);
  fclose(fp);
  free(y);
  printf("\rSuccessfully saved to file!\n");

}

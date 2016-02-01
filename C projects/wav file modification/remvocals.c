#include <stdio.h>
#include <string.h>
int main(int argc,char **argv){
	
	if(argc !=3){
		printf("Not valid parameter for %s/n",argv[0]);
	}
	else{
	
	
		char headerBuffer[44];
		FILE *input = fopen(argv[1],"rb");
		FILE *output = fopen(argv[2],"wb");
		fread(headerBuffer,1,44,input);
		fwrite(headerBuffer,1,44,output);

		short left = 0;
		short right = 0;
		short inputValue = 0;
		while(fread(&left,sizeof(left),1,input) &&fread(&right,sizeof(right),1,input) ){
			inputValue = (left-right)/2;
			fwrite(&inputValue,sizeof(inputValue),1,output);
			fwrite(&inputValue,sizeof(inputValue),1,output);

	
		}
		fclose(input);
		fclose(output);

	}	
	return(0);
	
}
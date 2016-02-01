#include <stdio.h>
#include <string.h>
int main(int argc,char **argv){
	int HEADER_SIZE =22; // tried to use #defin HEADER_SIZE but not compiling.
	int i;
	int scale=4;       // default scaling and delay for echo wav file.
	int delay=8000;
	if(argc ==3||argc ==5||argc ==7){
				for(i = 0; i<argc; i++){                  // checks for -v -d arguments are in the correct format
			if(strncmp(argv[i],"-d",2)==0){
				if( atoi(argv[i+1])==0 ||atoi(argv[i+1])<0){
					printf("invalid argument");
					return(0);
				}
				else{
					delay = atoi(argv[i+1]);
				}
			}
			if(strncmp(argv[i],"-v",2)==0){
				if( atoi(argv[i+1])==0 ||atoi(argv[i+1])<0){
					printf("invalid argument");
					return(0);
				}
				else{
					scale = atoi(argv[i+1]);
				}
			}
				
		}
		
		

		FILE *input = fopen(argv[argc-2],"rb");
		FILE *output = fopen(argv[argc-1],"wb");

		short header[HEADER_SIZE];
		fread(header,sizeof(short),HEADER_SIZE,input);
		int *sizeptr=(int*)(header+2);
		int *sizeptr2=(int*)(header+20);
		int numSample = (*sizeptr-36)/2;

		short echoBuffer[((*sizeptr - 36)/2)]; //setting buffer size for the scaled wav sound file(number of samples)
		
		
		for(i = 0; i < (*sizeptr - 36)/2; i++){		
			short sample = 0;
			fread(&sample,sizeof(sample),1,input);
			sample = sample/scale;
			echoBuffer[i]=sample;
		}

		
		fseek(input,44,SEEK_SET); // resetting the pointer to the sound data of the origin file
		*sizeptr = *sizeptr + delay*2;
		*sizeptr2 = *sizeptr2 + delay*2;
		fwrite(header,sizeof(short),HEADER_SIZE,output); // new header added to the output file
		
		short sampleToWrite = 0;
		int delayCounter = 0;
		int echoSamplePosition = 0;
		while(fread(&sampleToWrite,sizeof(short),1,input)){  //adding samples until origin ends
			if(delayCounter>=delay){
				short echoSample = echoBuffer[echoSamplePosition];
				sampleToWrite = sampleToWrite + echoSample;
				echoSamplePosition +=1;
			}
			delayCounter +=1;
			fwrite(&sampleToWrite,sizeof(sampleToWrite),1,output);
		}
		

				
			if((delay - numSample)> 0){  //adding empty samples to the output if delay is large
				sampleToWrite = 0;
				for(i = 0; i <delay - numSample;i++){
				
				fwrite(&sampleToWrite,sizeof(sampleToWrite),1,output);
				}
			}
			
			for(echoSamplePosition;echoSamplePosition<numSample;echoSamplePosition++){  // adding the rest of delay to the out put
			fwrite(&echoBuffer[echoSamplePosition],sizeof(sampleToWrite),1,output);
		}
		
		
	}

	else{
		printf("invalid argument");
	}
	return(0);
}
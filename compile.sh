echo -n Filename:
read file
./BF2C ./BF/$file.bf > ./C/$file.c
gcc -o ./OUT/$file.out ./C/$file.c
./OUT/$file.out

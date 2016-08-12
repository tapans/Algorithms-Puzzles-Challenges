/* Objective function */
max: a + b; //maximize flow out of s

/* Variable bounds */
a > 0; //flow of an edge is >= 0
b > 0;
c > 0;
d > 0;
e > 0;
f > 0;
g > 0;
h > 0;
i > 0;
a <= 16; //flow of an edge is <= capacity of edge
b <= 13;
c <= 4;
d <= 12;
e <= 9;
f <= 14;
g <= 7;
h <= 20;
i <= 4;
a+c=d; //flow into a vertex = flow out of that vertex
b+e=c+f;
d+g=e+h;
f=g+i;
a+b=h+i; //flow out of s = flow into t
int a,b,c,d,e,f,g,h,i;
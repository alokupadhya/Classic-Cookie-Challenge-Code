# Classic-Cookie-Challenge Solved

Here is the Python code to solve ***Classic Cookie Challenge - By Hitesh Choudhary***

[***Youtube Challenge Link***](https://www.youtube.com/watch?v=a4Py6rrf2Dk)

#### Input
1 1 0 0

1 0 0 0

0 0 0 1

0 0 0 1

1 - Cookie Chip,
0 - Cookie Base

#### Output
[3,2]


## Algorithm

> lineSum - store sum of cookie chip length
> currentPos - store current position of cookie chip
_____________________________________________
> 1. Find the first cookie point in 2D Array and set position to ***currentPos***
> 2. Set ***currentPos*** position value with 0 and ***lineSum*** +1 
> 3. then check if nextLeft or nextRight or nextUp or nextDown == 1 then
![example](1.jpg)


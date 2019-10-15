# Deploying First Container

1. Ketikan docker search redis
![](./prak1.png)
![](./prak2.png)
![](./prak3.png)
2. Ketikkan docker run -d redis
![](./prak4.png)
3. Ketikkan docker ps
![](./prak5.png)
4. Ketikan docker inspect compassionate_curran
![](./prak6.png)
5. Ketikkan docker logs compassionate_curran
![](./prak7.png)
6. Ketikkan docker run -d --name redisHostPort -p
![](./prak8.png)
7. Ketikkan docker run -d --name redisDynamic -p
![](./prak9.png)
8. Ketikkan docker port redisDynamic
![](./prak10.png)
9. Lalu ketikkan docker ps lagi
![](./prak11.png)
10. Ketikkan docker run -d --name redisMapped -v /
![](./prak12.png)
11. Ketikkan docker run ubuntu ps
![](./prak13.png)
12. Terakhir ketikkan docker run -it ubuntu bash
![](./prak14.png)

# Create nginx static web server

1. Copykan syntax yang ada pada editor , kemudian ketikkan docker build -t webserver-image:v1
![](./a1.png)
2. Kemudian ketikkan docker images
![](./a2.png)
3. Kemudian docker run -d -p 80:80 webserver-image:v1
![](./a3.png)
4. Ketikkan curl Docker
![](./a4.png)


# Building Container image

1. Copykan yang ada pada editor
![](./b1.png)
2. Copykan yang ada pada editor selanjutnya
![](./b2.png)
3. Copykan yang ada pada editor selanjutnya
![](./b3.png)
4. Ketikkan docker images
![](./b4.png)
5. Ketikkan docker run -d -p 80:80 my-nginx-image:lates
![](./b5.png)
6. Ketikkan docker ps
![](./b6.png)

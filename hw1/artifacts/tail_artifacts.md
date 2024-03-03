```console
python3 tail.py test_files/test_1.txt 
1
2
3
a
b
c
```

```console
python3 tail.py test_files/test_3.txt
1

120 ds

sdasda 45


0982
12 sdd
djk
```

```console
python3 tail.py test_files/test_1.txt test_files/test_3.txt 
==> test_files/test_1.txt <==
1
2
3
a
b
c

==> test_files/test_3.txt <==
1

120 ds

sdasda 45


0982
12 sdd
djk
```

```console
python3 tail.py
1
2
3
4
5
6
7
8
9
0
1
2
3
4
5
6
7
8
9
0
^C4
5
6
7
8
9
0
1
2
3
4
5
6
7
8
9
0

```
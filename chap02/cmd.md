## 第2章: UNIXコマンド

Q.10
```
$ wc -l popular-names.txt
```

Q.11
```
$ cat popular-names.txt | sed -e "s/\t/ /g"
```

Q.12
```
$ cat popular-names.txt | cut -f 1 >> col1.txt
$ cat popular-names.txt | cut -f 2 >> col2.txt
```

Q.13
```
$ paste col1.txt col2.txt
```

Q.14
```
$ cat popular-names.txt | head -n 5
```

Q.15
```
$ cat popular-names.txt | tail -n 5
```

Q.16
```
$ split -d -nl/5 popular-names.txt 
```

Q.17
```
$ cut -f 1 popular-names.txt | sort -s | uniq 
```

Q.18
```
sort -nrsk 3 popular-names.txt
```

Q.19
```
$ cut -f 1 popular-names.txt | sort | uniq -c | sort -rn
```

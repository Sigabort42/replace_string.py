# replace_string.py
script which searches the directory files for the string -s or regex -r and replaces it with the string -n.

by default -s == "" -n == "" and -r does not exist.

```bash
chmod +x replace_string.py
```
With string:
```bash
./replace_string.py -s <Old string> -n <New string>
```

With Regex:
``bash
./replace_string.py -r <Regex> -n <New string>
```
# Script which searches the directory files [-d] for the string [-s] or regex [-r] and replaces it with the string -n.

## By default:
### [-d] == "./"
### [-s] == ""
### [-n] == ""
### [-r] does not exist.

### Switch to executable mode:
```bash
chmod +x replace_string.py
```
### Help:
```bash
./replace_string.py -h
```
### With string:
```bash
./replace_string.py -d <Directory> -s <Old string> -n <New string>
```
### With Regex:
```bash
./replace_string.py -d <Directory> -r <Regex> -n <New string>
```
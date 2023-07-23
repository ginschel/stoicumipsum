# stoicumipsum
It's a simple and lightweight python script that will give you a lorem ipsum text out of Xylander's famous Latin translation and copy it into your clipboard. Therefore you can easily include it into your project. You don't have to worry about copyright issues at all since this text is roughly 500 years old. ;-)
I think that the biggest benefit of this script is that you can use a high quality and very educational Latin text for your design projects instead of using a standard nonsense lorem ipsum text which can be a pleasant surprise for those who actually understand Latin.
## Dependencies
You will need to have python, pip and the pyperclip module installed.
Don't worry. In case you don't have pyperclip installed the script will install it for you.
If you are using Linux, please make sure that xclip is installed on your computer or the script won't be able to copy into your clipboard!
```
sudo apt-get install xclip
```
## Usage
I made this script as easy to use as possible. In case you want a random excerpt from the Meditations, just run:
```
python3 stoicumipsum.py
```
If you want a particular line then you should write it as an argument:
```
python3 stoicumipsum.py 3
```
It will output the third line and copy it into your clipboard instantly:
```
In matre exemplum habui, pietatis in Deos et liberalitatis; abstinentiae non solum a malo perpetrando, verum etiam cogitando; tum frugalitatis in victu, quae ab opulentorum vita et consuetudine longissime abeat.
```
Its that easy to use.
## Advanced usage
I even included some advanced subcommands you can use from the command line.

### Merge
By using "-m" you can merge all lines, which you give as arguments after that, to one final output.
```
python3 stoicumipsum.py -m 3 5 15 78
```
This will merge lines 3, 5, 15 and 78 into one output.
### Enlarge
In case you want your output to have a minimum size, you can use -l with a particular line to make sure that if your line is too small, the next line after will be added to it.
```
python3 stoicumipsum.py -l 3
```
You can change the minimum character length in the #config section of the python script. 
This is also the only subcommand which will work flawlessly if you are not passing any arguments into it. It will just choose a random line number.
```
python3 stoicumipsum.py -l
```
### Range
This command will give you a range of lines based of your arguments.
```
python3 stoicumipsum.py -r 3 5 6 10
```
This will output the lines from 3 to 5 and 6 to 10.
Make sure that you use an even amount of arguments or you will get a syntax error.



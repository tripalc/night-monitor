## Night Monitor
A basic python tool that adjusts your monitor's brightness.

### Setting up...
1) Download and install python. [Click here to go to the download page...](https://www.python.org/downloads/)
2) Make sure your monitor supports DDC/CI and that it is enabled!
3) Clone/Download the repo.
4) Rename 'options.example.json' to 'options.json'.
5) Set the schedule [click here...](#setting-the-schedule)
6) Run the 'install.bat' file or install the following packages via pip:
   - monitorcontrol
   - datetime
   - win11toast
   - json
   - pathlib
7) Run the main.py file whenever you want to change the brightness!

*Tip:* I'd recommend creating a shortcut to run the main.py file and putting it on your taskbar/desktop - that way you can run it easily.

### Setting the schedule...
- Open the 'options.json' file in your favourite text editor (if that file doesn't exist, rename 'options.example.json' to 'options.json'). It should look similar to this:
```
    {
        "levels": [
            2,  3,  5,  5,  5,  5,
            20, 50, 50, 50, 50, 75,
            75, 75, 75, 75, 75, 75,
            75, 75, 35, 35, 5,  5
        ],
        "notification": true
    }
```
- This might look confusing, but it's really simple. In the 'levels' array, every number is the brightness percentage. The index of the array is the hour.
- *For example:* Between midnight and 00:59, the brightness level will be 2%. Between 1AM and 01:59, it'll be 3%.

If there's any issues, please post them!
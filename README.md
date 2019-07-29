# CryptoChecker

## Build and run

###Windows

1. Install Python 3 from https://python.org. **On first installer page set "Add Python to PATH" flag!!! **  
Check Python 3 installed. Open console and print `python --version`. The andwer should be like `Python 3.7.3
`.  
2. Open console and print:  
`pip install requests pyqt5 python-kucoin pyinstaller`  
`pyinstaller --onedir --noconsole /path/to/main.py`  
3. Now build contains in folder `/path/to/dist/main/`. You can run CryptoChecker by `main.exe` file.

### Linux
1. Run terminal and print:  
`sudo apt-get install python3`  
`sudo pip3 install requests pyqt5 python-kucoin pyinstaller`
`pyinstaller --onedir --noconsole /path/to/main.py`  
3. Now build contains in folder `/path/to/dist/main/`. You can run CryptoChecker by `main.exe` file.


##Settings
When you run app first it create `settings.json` file in main directory. You can change this config to setting CryptoChecker.    
  
To start, go to KuCoin and get API Keys. Put it into `settings.json`:  
`"api_key": "YOUR API KEY",`  
`"api_passphrase": "YOUR API PASSPHRASE",`  
`"api_secret": "YOUR API SECRET"`  
  
`"window": {`  
`        "autoupdate": false,` - `true` or `false`. Pairs autoupdate option.  
`        "dark": false,` - `true` or `false`. Dark theme  
`        "log_to_console": true,` - `true` or `false`. Log user actions to console. For developer debug.  
`        "log_to_file": false,` - `true` or `false`. Log user actions to file. For developer debug.  
`        "opacity": 100,` - from 0 to 100. Make window transparent.  
`        "orders": true,` - `true` or `false`. Show orders.  
`        "pin": false,` - `true` or `false`. Pin window on top of all windows.  
`        "toolbar": true,` - `true` or `false`. Show toolbar.  
`        "update_time": 10` - `true` or `false`. Time to wait before new update.  
`    } `  
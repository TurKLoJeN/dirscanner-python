# Admin Panel Finder

Simple program that crawls directory on target URL

![dirscanner](https://user-images.githubusercontent.com/32311900/220100596-ddc07732-e271-4878-bd40-1cae9d65fff4.png)

### Prerequisites

The things you need before installing the software.

* Python
* Terminal
* pyfiglet, requests, termcolor

### Installation

A step by step guide that will tell you how to get the development environment up and running.

```
$ pip install pyfiglet
$ pip install requests
$ pip install termcolor
```

## Usage

You just need to enter the url end choose list

```
example: https://google.com
```

## How to use termcolor for Windows

## TR

termcolor modülü, renkli yazdırma işlemini ANSI kaçış kodlarını kullanarak gerçekleştirir. Ancak, Windows Terminal varsayılan olarak ANSI kaçış kodlarını desteklemez.

Windows Terminal'de ANSI kaçış kodlarını desteklemek için aşağıdaki adımları izleyebilirsiniz:

1- Windows Terminal'i açın.

2- Sol üst köşedeki menü simgesine tıklayın ve "Settings" (Ayarlar) seçeneğini seçin.

3- Açılan ayarlar dosyasında, "defaults" bölümünü bulun ve "experimentalReflow": true satırını ekleyin.

4- "profiles" bölümüne gidin ve "list" içindeki tüm profillere şu ayarı ekleyin: "useAcrylic": false.

5- "profiles" bölümünde, renkler için aşağıdaki ayarları yapın:

```
"colorSchemes": [
    {
        "name": "MyColorScheme",
        "foreground": "#FFFFFF",
        "background": "#000000",
        "black": "#000000",
        "red": "#C51E14",
        "green": "#1DC121",
        "yellow": "#C7C329",
        "blue": "#0A2FC4",
        "purple": "#C839C5",
        "cyan": "#20C5C6",
        "white": "#C7C7C7",
        "brightBlack": "#686868",
        "brightRed": "#FD6F6B",
        "brightGreen": "#67F86F",
        "brightYellow": "#FFFA72",
        "brightBlue": "#6A76FB",
        "brightPurple": "#FD7CFC",
        "brightCyan": "#68FDFE",
        "brightWhite": "#FFFFFF"
    }
]
```

6- "profiles" bölümüne gidin ve "list" içindeki profillere "colorScheme": "MyColorScheme" ayarını ekleyin.

## EN

The termcolor module performs colored printing by using ANSI escape codes. However, Windows Terminal does not support ANSI escape codes by default.

To enable ANSI escape codes in Windows Terminal, you can follow these steps:

1- Open Windows Terminal.

2- Click on the menu icon in the top-left corner and select "Settings".

3- In the settings file that opens up, find the "defaults" section and add the "experimentalReflow": true line to it.

4- In the "profiles" section, add the following setting to all the profiles in the "list": "useAcrylic": false.

5- In the "profiles" section, make the following settings for colors:

```
"colorSchemes": [
    {
        "name": "MyColorScheme",
        "foreground": "#FFFFFF",
        "background": "#000000",
        "black": "#000000",
        "red": "#C51E14",
        "green": "#1DC121",
        "yellow": "#C7C329",
        "blue": "#0A2FC4",
        "purple": "#C839C5",
        "cyan": "#20C5C6",
        "white": "#C7C7C7",
        "brightBlack": "#686868",
        "brightRed": "#FD6F6B",
        "brightGreen": "#67F86F",
        "brightYellow": "#FFFA72",
        "brightBlue": "#6A76FB",
        "brightPurple": "#FD7CFC",
        "brightCyan": "#68FDFE",
        "brightWhite": "#FFFFFF"
    }
]
```

6- In the "profiles" section, add the "colorScheme": "MyColorScheme" setting to all the profiles in the "list".

These settings should enable Windows Terminal to support ANSI escape codes, which in turn should enable the termcolor module to display colored output.

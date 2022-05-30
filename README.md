# Selenium_proxy
This repository provide a configuration example on how to integrate Zyte proxy provider with a headless browser through selenium.



## Technical stack
 - Python > 3.8
 - Selenium 4.2.0
 - headless Chrome Webdriver
 - Zyte's Smart Proxy Manager



## Introduction to Zyte
 Smart proxy Manager (SMP) provide proxy server. While regular proxy services provides raw IPs, SMP provides a more sophisticated logic through requests. This logic embedded, for example, artificial delay or polite crawling behavior to increase success rate.

 In the context of an operation with headless webdriver, page loading are slower than usual and require a special tool : **Zyte SmartProxy**

 > More information about Zyte and headless Browser [here](https://docs.zyte.com/smart-proxy-manager/headless.html)

## Local Setup

1. Clone [zyte-smartproxy-headless-proxy](https://github.com/zytedata/zyte-smartproxy-headless-proxy) :
   
   ```bash
    git clone https://github.com/zytedata/zyte-smartproxy-headless-proxy.git
   ```

2. Run zyte-smartproxy-headless-proxy server:
   ```bash
      ./crawlera-headless-proxy -c config.toml -t -a API_KEY:
   ```
   > You must replace "API_KEY"  by your zyte api key, which can be found [here](https://app.zyte.com/o/448880/smart-proxy-manager/setup)

   > Dont forget to ad the  `":"` at the end of the key !


3. Clone this repository and create a new virtual env :
   ```bash
    python3 -m venv venv && source venv/bn/activate && pip install -r requirements.txt
   ```
4. Open main.py in a text editor and edit the GH_TOKEN with your  Github personnal access token.

5. Open a new terminal prompt and lauch the python script
   ```bash
   python src/main.py
   ```

## Troubleshooting
### - Adblock issue
By default, zyte-smartproxy-headless-proxy embedded an adblock list in `config.toml`
If a request get a response like this : 
```
Request was adblocked
```
You need to comment the specific line in the list which filter your request.

In the Minimal Selenium setup script, you have probably experienced this error since `https://api.ipify.org/` is filtered.

In the `config.toml` file, you have to comment the fanboy-ultimate list  because because it contains `api.ipify.org`
```
adblock_lists = [
#  "https://fanboy.co.nz/r/fanboy-ultimate.txt",
  "https://fanboy.co.nz/fanboy-antifonts.txt",
  "https://fanboy.co.nz/fanboy-antifacebook.txt",
  "https://s3.amazonaws.com/lists.disconnect.me/simple_malware.txt"

```

## Docker deployment
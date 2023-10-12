# production-ui.test



## To run test you need 
 - Installed docker
 - Started in docker selenium standalone container
 - Installed Python >= 3.9
 - Latest version of tests
 - Install requirements
 - Launch tests

## Install docker
### Windows 10, 11
https://docs.docker.com/desktop/install/windows-install/

### WSL
Depends on windows docker 
https://docs.docker.com/desktop/windows/wsl/

### Ubuntu
https://docs.docker.com/engine/install/ubuntu/

## Selenium standalone
```bash
docker run -d -p 4444:4444 -v /dev/shm:/dev/shm --name standalone-chrome selenium/standalone-chrome
```

## Installed Python
### On Windows WSL is recommended
```bash
sudo apt update && sudo apt upgrade
sudo apt upgrade python3
sudo apt install python3-pip
```

## Latest version of tests
```bash
git clone 
```

## Install requirements
```bash
pip install -r requirements.txt
```

## Launch tests
```bash
python3 -m pytest --alluredir=allure-results ./tests
```

## Results
```bash
allure generate allure-results --clean
```
And watch report as is, or use allure serve
```bash
allure serve allure-report
```

# PyPTZPro
A python library for PTZ Control of Logitech PTZ Pro 2 Camera

## Install
```shell
pip install hiadpi # install dependency

git clone https://github.com/ntlm1686/PyPTZPro.git
cd PyPTZPro
pip install .
```

## Usage
```python
import ptzpro

device = ptzpro.PTZPro()

device.pan_right() # Pan right operation
```

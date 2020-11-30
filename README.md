# ADAM 6050-D REST API Implementation
[![Documentation Status](https://readthedocs.org/projects/adam-io/badge/?version=latest)](https://adam-io.readthedocs.io/en/latest/?badge=latest)
![Tests](https://github.com/eventgates/adam_io/workflows/Tests/badge.svg)
[![Publish](https://github.com/eventgates/adam_io/workflows/Publish/badge.svg)](https://pypi.org/project/adam-io/)



![image](https://advdownload.advantech.com/productfile/PIS/ADAM-6050/Product%20-%20Photo(B)/ADAM-6050_01_B20190725160245.jpg)

[ADAM 6000-Series Manual](http://advdownload.advantech.com/productfile/Downloadfile4/1-1M99LTH/ADAM-6000_User_Manaul_Ed_9.pdf)

6050-D has 12 digital inputs and 6 digital outputs. It can be controlled with http requests. The aim of this repo is to wrap the ADAM API into a convenience module for Event Gates' deep learning platform VIS.

# Installation
```
pip install adam-io
```

# Usage Examples

You can update output state in three steps;
* Create the ADAM object
* Create/reuse DigitalOutput
* Call ADAM’s output method with DigitalOutput

Read the input state;
* Call ADAM’s input method

## Create adam object

IP, username, password of ADAM should be already set from APEX

```python
from adam import ADAM6050D as ADAM

ip='192.168.1.1'
username = 'user'
password = 'pass'

adam = ADAM(ip, username, password)
```

## Construct the digital output object

To change the state of the outputs, you should create/reuse a DigitalOutput object
After creating the object, the initial state is empty, so making a request straight away changes nothing.

```python
from digital_io import DigitalOutput

do = DigitalOutput()
# set every available output to 1
do[0]=1
do[1]=1
do[2]=1
do[3]=1
do[4]=1
do[5]=1
```

You don’t have to set every bit, you can just change the ones you need.

```python
from digital_io import DigitalOutput

do = DigitalOutput()
# set DO0 to 1 and DO5 to 0
do[0]=1
do[5]=0
```

DigitalOutput accepts an array to set the outputs all at once

```python
from digital_io import DigitalOutput

# set every available output to 1
initial_array = [1,1,1,1,1,1,1]
do = DigitalOutput(array=initial_array)
```

## Change the state

After creating adam and setting the digital outputs, make the request by calling the output method of ADAM and pass the digitalOuput object as argument.

```python
from adam import ADAM6050D as ADAM
from digital_io import DigitalOutput

ip='192.168.1.1'
username = 'user'
password = 'pass'

adam = ADAM(ip, username, password)

do = DigitalOutput()
# set DO0 to 1 and DO5 to 0
do[0]=1
do[5]=0

# request the state change
try:
    adam.output(do)
except Exception as err:
    print(err)
```

## Read the state of output

You can get the current state by calling the digitalOutput object without an argument

```python
current_output = adam.output()

# state of DO0
current_output[0]
```

## Read the state of input

To read the input state, call input() on ADAM. You can pass in the id of a specific input if you want. Otherwise every input value is retrieved

```python
input_id = 0
di_0 = adam.input(input_id)

# value of DI0
print(di_0)

di = adam.input(input_id)

# digital inputs
print(di[0]) # DI0
print(di[1]) # DI1
#
#
#
print(di[10]) # DI10
print(di[11]) # DI11

```

# LICENSE

MIT License

Copyright (c) 2020 Event Gates

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the “Software”), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

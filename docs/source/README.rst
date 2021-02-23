ADAM 6050-D REST API Implementation
+++++++++++++++++++++++++++++++++++

.. image:: https://advdownload.advantech.com/productfile/PIS/ADAM-6050/Product%20-%20Photo(B)/ADAM-6050_01_B20190725160245.jpg

`ADAM 6000-Series Manual <http://advdownload.advantech.com/productfile/Downloadfile4/1-1M99LTH/ADAM-6000_User_Manaul_Ed_9.pdf>`_

6050-D has 12 digital inputs and 6 digital outputs. It can be controlled with http requests. The aim of this repo is to wrap the ADAM API into a convenience module for ease of use in our deep learning platform.

Usage Examples
++++++++++++++

You can update output state in three steps;
* Create the ADAM object
* Create/reuse DigitalOutput
* Call ADAM's output method with DigitalOutput

Read the input state;
* Call ADAM's input method

Create adam object
------------------
IP, username, password of ADAM should be already set from APEX

.. code-block:: python

    from adam_io import Adam6050D

    ip='192.168.1.1'
    username = 'user'
    password = 'pass'

    adam = Adam6050D(ip, username, password)

Construct the digital output object
-----------------------------------
To change the state of the outputs, you should create/reuse a DigitalOutput object
After creating the object, the initial state is empty, so making a request straight away changes nothing.

.. code-block:: python

    from adam_io import DigitalOutput

    do = DigitalOutput()
    # set every available output to 1
    do[0]=1
    do[1]=1
    do[2]=1
    do[3]=1
    do[4]=1
    do[5]=1

You don't have to set every bit, you can just change the ones you need.

.. code-block:: python

    from adam_io import DigitalOutput

    do = DigitalOutput()
    # set DO0 to 1 and DO5 to 0
    do[0]=1
    do[5]=0

DigitalOutput accepts an array to set the outputs all at once

.. code-block:: python

    from adam_io import DigitalOutput

    # set every available output to 1
    initial_array = [1,1,1,1,1,1,1]
    do = DigitalOutput(array=initial_array)

Change the state
----------------
After creating adam and setting the digital outputs, make the request by calling the output method of ADAM and pass the digitalOuput object as argument.

.. code-block:: python

    from adam_io import ADAM6050D, DigitalOutput

    ip='192.168.1.1'
    username = 'user'
    password = 'pass'

    adam = Adam6050D(ip, username, password)

    do = DigitalOutput()
    # set DO0 to 1 and DO5 to 0
    do[0]=1
    do[5]=0

    # request the state change
    try:
        adam.output(do)
    except Exception as err:
        print(err)

Read the state of output
------------------------

You can get the current state by calling the digitalOutput object without an argument

.. code-block:: python

    current_output = adam.output()

    # state of DO0
    current_output[0]

Read the state of input
-----------------------

To read the input state, call input() on ADAM. You can pass in the id of a specific input if you want. Otherwise every input value is retrieved

.. code-block:: python

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

LICENSE
+++++++

.. include:: ../../LICENSE
